from flask import Flask, jsonify, request
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
    if (len(products_found) > 0): 
        return jsonify({'product':products_found[0]})
    else:
        return jsonify({'message':'Product not found'})

@app.route('/products', methods=['POST'])
def post_products():
    new_product = {
        'name': request.json['names'],
        'price': request.json['prices'],
        'quantity': request.json['quantities']
    }
    Products.append(new_product)
    return ({'message':'Products add amazing', "products": Products})

@app.route('/products/<string:product_name>', methods=['PUT'])
def edit_product(product_name): 
    products_found = [product for product in Products if product['name'] == product_name]
    if len(products_found) > 0 : 
        products_found[0]['name'] = request.json['name']
        products_found[0]['price'] = request.json['price']
        products_found[0]['quantity'] = request.json['quantity']
        return jsonify({
            'message':'Product updated',
            'product':products_found[0]
        }) 
    return jsonify({'message':'Not found boy'})

@app.route('/products/<string:product_name>', methods=['DELETE'])
def delete_product(product_name):
    products_found = [product for product in Products if product['name'] == product_name]
    if len(products_found) > 0 :
        Products.remove(products_found[0])
        return jsonify({
            'message':'Product updated',
            'products':Products
        }) 
    else:
        return jsonify({'No se pudo eliminar, trate de nuevo'})


app.run(host='127.0.0.1', port=4000, debug=True)