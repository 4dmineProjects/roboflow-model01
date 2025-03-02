from flask import Flask, request, render_template_string
import base64
from inference_sdk import InferenceHTTPClient


#Cpnstaants
API_URL = "https://detect.roboflow.com"
API_KEY = 'uaILUnyqtod9HiftUywN'


def get_preds(base64_image=""):

    client = InferenceHTTPClient(
        api_url= API_URL,
        api_key=API_KEY
    )
    
    predictions = client.run_workflow(
        workspace_name="sliit-u2znu",
        workflow_id="custom-workflow-3",
        images={
            # "image": "https://agritech.tnau.ac.in/crop_protection/chilli-disease-bact.jpg"
            "image" : base64_image
        },
        use_cache=True # cache workflow definition for 15 minutes
    )
    
    return predictions



def extract_results(data):

    predictions = data[0]['predictions']['predictions']
    max_confidence_class = max(predictions, key=lambda x: x['confidence'])
    
    return max_confidence_class['class'], max_confidence_class['confidence']




app = Flask(__name__)


@app.route('/', methods=['GET'])
def check():
    return 'App is Working'



@app.route('/predict', methods=['GET', 'POST'])
def upload_image():
    image_base64 = None
    
    
    print('--------')
    
    if request.method == 'POST' and 'image' in request.files:
        image_file = request.files['image']
        
        # Read image and encode it to base64
        img_data = image_file.read()
        image_base64 = base64.b64encode(img_data).decode('utf-8')  
        print('Converted to bs64')
        
        preds =  get_preds(image_base64)
        res = extract_results(preds)
        
        print('------' , res)
        

    return res

if __name__ == '__main__':
    app.run(debug=True)
