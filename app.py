from flask import Flask
from app import create_app

# app = Flask(__name__)

app = create_app()

# @app.route("/")
# def hello():
#     return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=True, port=5000)
