from flask import Flask, request
import base64


try:
    from inference_sdk import InferenceHTTPClient
    print("InferenceHTTPClient imported successfully!")
except ImportError as e:
    print(f"Error importing InferenceHTTPClient: {e}")


app = Flask(__name__)


@app.route('/')
def check():
    return "App is Working !!"

if __name__ == '__main__':
    app.run(debug=True)
