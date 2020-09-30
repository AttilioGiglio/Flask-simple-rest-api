from flask import Flask, jsonify
from src.products import Products

app = Flask(__name__)

# Method GET is the default method, not need to add
@app.route('/')
def start():
    return jsonify({"mesage": "ping-pong"}) 

@app.route('/products', methods=['GET'])
def get_products():
    # return jsonify(Products)
    return jsonify({'products':Products, 'message': 'Products List'})

@app.route('/products/<string:product_name>')
def get_product(product_name):
    products_found = [product for product in Products if product['name'] == product_name]
    return jsonify({'product':products_found[0]})

app.run(host='127.0.0.1', port=4000, debug=True)