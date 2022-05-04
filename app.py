from flask import Flask, jsonify
from products import products

app = Flask(__name__)

@app.route('/ping')
def ping():
    return jsonify({'message': 'pong!'})

@app.route('/products')
def getProducts():
    #return jsonify(products)
    return jsonify({"products": products, "message": "Product's list"})

# if the name of this file is the main one. Run the server in debug mode
if __name__ == '__main__':
    app.run(debug=True, port=4000)


