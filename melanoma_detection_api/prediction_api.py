# Dependencies
from flask import Flask, request, render_template_string, jsonify
import traceback
from PIL import Image
from werkzeug.utils import secure_filename
import tensorflow as tf

from preprocessing.image_preprocessing import preprocessing
from model.model_loader import model_loader

app = Flask(__name__)

@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        if model:
            try:
                if request.files:
                    data = request.files['image']
                    image = Image.open(data)
                    img = preprocessing(image=image)

                #return str(np.argmax(model.predict(x=img/255),axis=1))
                return str(model.predict(x=img))

            except:
                return jsonify({'trace': traceback.format_exc()})
        else:
            print ('Train the model first')
            return ('No model here to use')

if __name__ == '__main__':
    try:
        port = int(sys.argv[1]) # This is for a command-line input
    except:
        port = 12345 # If you don't provide any port the port will be set to 12345

    model_path = 'model/model_melanoma_classification.h5'
    model = model_loader(model_name=model_path)

    app.run(port=port, debug=True)