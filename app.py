from flask import Flask, request
import base64



app = Flask(__name__)


@app.route('/')
def check():
    return "App is Working !!"

if __name__ == '__main__':
    app.run(debug=True)
