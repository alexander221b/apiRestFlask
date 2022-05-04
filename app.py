from flask import Flask, jsonify, request
from products import products

app = Flask(__name__)

@app.route('/ping')
def ping():
    return jsonify({'message': 'pong!'})

@app.route('/products')
def getProducts():
    #return jsonify(products)
    return jsonify({"products": products, "message": "Product's list"})

@app.route('/products/<string:product_name>')
def getProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name ]
    if(len(productsFound) > 0):
        return jsonify(productsFound)
    return jsonify({"message": "Product not found"})

@app.route('/products', methods=['POST'])
def addProduct():
    data = request.json
    newProduct = {}
    error = {"message": ""}
    if("name" in data):
        newProduct['name'] = data['name']
    else:
        error['message'] = "field name doesn't exist"
        return jsonify(error)
    if("price" in data):
        newProduct['price'] = data['price']
    else:
        error['message'] = "field price doesn't exist"
        return jsonify(error)
    if("quantity" in data):
        newProduct['quantity'] = data['quantity']
    else:
        error['message'] = "field quantity doesn't exist"
        return jsonify(error)
    products.append(newProduct)
    return jsonify({"message": "new product added", "products": products})
    
        
    



# if the name of this file is the main one. Run the server in debug mode
if __name__ == '__main__':
    app.run(debug=True, port=4000)


