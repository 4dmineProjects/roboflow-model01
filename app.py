from flask import Flask, request, render_template_string
import base64
from io import BytesIO

try:
    from inference_sdk import InferenceHTTPClient
    print("----------------------->>>>>>>>>InferenceHTTPClient imported successfully!")
except ImportError as e:
    print(f"----------------------->>>>>>>>>Error importing InferenceHTTPClient: {e}")


app = Flask(__name__)


@app.route('/', methods=['GET'])
def check():
    return 'App is Working 1'



if __name__ == '__main__':
    app.run(debug=True)
