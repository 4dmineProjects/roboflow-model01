from flask import Flask, request, render_template_string
import base64
from io import BytesIO
from inference_sdk import InferenceHTTPClient


app = Flask(__name__)


@app.route('/', methods=['GET'])
def check():
    return 'App is Working x1'



if __name__ == '__main__':
    app.run(debug=True)
