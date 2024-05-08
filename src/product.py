import random
import redis
from flask_restful import abort, reqparse, Resource

r = redis.Redis(host='localhost', port=6379, decode_responses=True)
parser = reqparse.RequestParser()
parser.add_argument("type")
parser.add_argument("price")


class Product(Resource):
    def get(self, product_id):
        pid = f"product:{product_id}"
        product = r.hgetall(pid)

        if len(product) == 0:
            abort(404, message=f"{pid} doesn't exist")
        return product, 200

    def post(self, product_id=None):
        args = parser.parse_args()
        product_id = f"product:{random.getrandbits(32)}"

        r.hset(product_id, mapping=args)
        return f"New product created: {product_id}", 201

    def put(self, product_id):
        pid = f"product:{product_id}"
        args = parser.parse_args()
        product = r.exists(pid)

        if not product:
            abort(404, message=f"{pid} doesn't exist")

        with r.pipeline() as pipe:    
            for k, v in args.items():
                if v is not None:
                    pipe.hset(pid, k , v)
            pipe.execute()

        updated_product = r.hgetall(pid)
        return updated_product, 200

    def delete(self, product_id):
        r.delete(f"product:{product_id}")
        return '', 204

class ProductList(Resource):
    def get(self):
        result = {}
        
        for key in r.keys():
            product = r.hgetall(key)
            result[key] = product

        return result, 200
