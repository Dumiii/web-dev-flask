import random
import redis
from flask import Flask
from flask_restful import Api
from product import Product, ProductList

app = Flask(__name__)
api = Api(app)

random.seed(6969)
products = {f"product:{random.getrandbits(32)}": i for i in (
    {
        "type": "Book",
        "price": 19.99
    },
    {
        "type": "Desk",
        "price": 99.99
    },
    {
        "type": "Lamp",
        "price": 39.99
    }
)}

r = redis.Redis(host='localhost', port=6379, decode_responses=True, db=0)
with r.pipeline() as pipe:
    for pid, product in products.items():
        pipe.hset(pid, mapping=product)
    pipe.execute()

print(r.keys())

api.add_resource(Product, '/product', '/product/<int:product_id>')
api.add_resource(ProductList, '/products')

if __name__ == '__main__':
    app.run(debug=True)
