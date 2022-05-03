from flask import Flask
from products import products

app = Flask(__name__)

@app.route('/ping')
def ping():
    return 'Pong'

# if the name of this file is the main one. Run the server in debug mode
if __name__ == '__main__':
    app.run(debug=True, port=4000)


