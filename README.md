# Introduction

Two small applications: one is a website with fully functioning HTML, CSS and JS running on [Flask](https://flask.palletsprojects.com/en/3.0.x/#), the Python web micro-framework and the other one is an app using [flask-restful](https://flask-restful.readthedocs.io/en/latest/), an extension for Flask that adds support for building REST APIs using Redis for key-value in-memory data storage.

## Install

Using the provided requirements.txt file inside config folder:

    pip install -r requirements.txt
    
it is also required to have a Redis server running on your machine, if you want a simple way to start one up you can use [Docker](https://www.docker.com/) to run the following command:

    docker run -d --name redis-stack-server -p 6379:6379 redis/redis-stack-server:latest

## Run the Flask website

    flask --app server run

## Run the REST API

    python3 rest_api.py

# REST API

The REST API endpoints are described below.

For convenience an in-memory database solution was used, here is the default data that was used to populate it for testing:

<p align="center">
    <img width="640" src="https://raw.githubusercontent.com/dumiii/web-dev-flask/master/images/data.png" alt="Download Instructions">
</p>

## Get product

### Request

`GET /product/id`

    curl -i -H 'Accept: application/json' http://127.0.0.1:5000/product/4111591970

### Response

    HTTP/1.1 200 OK
    Server: Werkzeug/3.0.2 Python/3.12.3
    Date: Wed, 08 May 2024 16:46:36 GMT
    Content-Type: application/json
    Content-Length: 45
    Connection: close

    {
        "type": "Lamp",
        "price": "39.99"
    }

## Create a new product

### Request

`POST /product`

    curl -i -H 'Content-Type: application/json' -d '{"type":"Laptop", "price":299.99}' http://127.0.0.1:5000/product

### Response

    HTTP/1.1 201 CREATED
    Server: Werkzeug/3.0.2 Python/3.12.3
    Date: Wed, 08 May 2024 18:46:34 GMT
    Content-Type: application/json
    Content-Length: 90
    Connection: close

    {
        "product:3414359210": {
            "type": "Laptop",
            "price": "299.99"
        }
    }

## Get a non-existent product

### Request

`GET /product/id`

    curl -i -H 'Accept: application/json' http://127.0.0.1:5000/product/9999

### Response

    HTTP/1.1 404 NOT FOUND
    Server: Werkzeug/3.0.2 Python/3.12.3
    Date: Wed, 08 May 2024 18:52:57 GMT
    Content-Type: application/json
    Content-Length: 48
    Connection: close

    {
        "message": "product:9999 doesn't exist"
    }

## Get list of products

### Request

`GET /products`

    curl -i -H 'Accept: application/json' http://127.0.0.1:5000/products

### Response

    HTTP/1.1 200 OK
    Server: Werkzeug/3.0.2 Python/3.12.3
    Date: Wed, 08 May 2024 18:53:46 GMT
    Content-Type: application/json
    Content-Length: 341
    Connection: close

    {
        "product:3414359210": {
            "type": "Laptop",
            "price": "299.99"
        },
        "product:3835099362": {
            "type": "Desk",
            "price": "99.99"
        },
        "product:299840531": {
            "type": "Book",
            "price": "19.99"
        },
        "product:4111591970": {
            "type": "Lamp",
            "price": "39.99"
        }
    }

## Change a product

### Request

`PUT /product/id`

    curl -i -H 'Content-Type: application/json' -d '{"type":"Book2", "price":30.99}' -X PUT http://127.0.0.1:5000/product/299840531

### Response

    HTTP/1.1 200 OK
    Server: Werkzeug/3.0.2 Python/3.12.3
    Date: Wed, 08 May 2024 18:59:09 GMT
    Content-Type: application/json
    Content-Length: 46
    Connection: close

    {
        "type": "Book2",
        "price": "30.99"
    }

## Change field of product

### Request

`PUT /product/id`

    curl -i -H 'Content-Type: application/json' -d '{"price":40.99}' -X PUT http://127.0.0.1:5000/product/299840531

### Response

    HTTP/1.1 200 OK
    Server: Werkzeug/3.0.2 Python/3.12.3
    Date: Wed, 08 May 2024 19:00:34 GMT
    Content-Type: application/json
    Content-Length: 46
    Connection: close

    {
        "type": "Book2",
        "price": "40.99"
    }

## Delete a product

### Request

`DELETE /product/id`

    curl -i -H 'Accept: application/json' -X DELETE http://127.0.0.1:5000/product/3414359210 

### Response

    HTTP/1.1 204 NO CONTENT
    Server: Werkzeug/3.0.2 Python/3.12.3
    Date: Wed, 08 May 2024 17:04:26 GMT
    Content-Type: application/json
    Connection: close


## Try to delete same product again

### Request

`DELETE /product/id`

    curl -i -H 'Accept: application/json' -X DELETE http://127.0.0.1:5000/product/3414359210    

### Response

    HTTP/1.1 404 NOT FOUND
    Server: Werkzeug/3.0.2 Python/3.12.3
    Date: Wed, 08 May 2024 17:06:07 GMT
    Content-Type: application/json
    Content-Length: 54
    Connection: close

    {
        "message": "product:3414359210 doesn't exist"
    }

# Credits

- [The Complete Python Developer](https://www.udemy.com/course/complete-python-developer-zero-to-mastery/?couponCode=ST20MT50724)
- [Flask](https://flask.palletsprojects.com/en/3.0.x/)
- [flask-restful](https://flask-restful.readthedocs.io/en/latest/)
- [Docker](https://www.docker.com/)
- [Redis](https://redis-py.readthedocs.io/en/stable/)
- [Carbon](https://carbon.now.sh/)
