from flask import Flask

app = Flask(__name__)

# if the name of this file is the main one. Run the server in debug mode
if __name__ == '__main__':
    app.run(debug=True, port=4000)