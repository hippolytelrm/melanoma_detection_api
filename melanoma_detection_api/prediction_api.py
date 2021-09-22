# Dependencies
from flask import Flask, request, render_template_string, jsonify
import traceback
from PIL import Image
from werkzeug.utils import secure_filename
import tensorflow as tf
import numpy as np

from preprocessing.image_preprocessing import preprocessing
from model.model_loader import model_loader

app = Flask(__name__)

MODEL_ALLOWED_EXTENSIONS = set(['h5', 'hdf5'])
IMAGE_ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

prediction_dict={
    0:'benign',
    1:'malignant'
}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in IMAGE_ALLOWED_EXTENSIONS

@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        if model:
            try:
                if request.files and allowed_file(request.files['image'].filename):
                    data = request.files['image']
                    image = Image.open(data)
                    img = preprocessing(image=image)

                    prediction_index = np.argmax(model.predict(x=img),axis=1)[0]
                    prediction = np.squeeze(model.predict(x=img),0)

                    if prediction_index == 1:
                         return "You must consult a dermatologist!\nThe model predicted that your skin lesion is {0} with a probability of {1} % !".format(
                            prediction_dict[int(prediction_index)], str(prediction[int(prediction_index)] * 100))

                    else:
                        return "No worry!\nThe model predicted that your skin lesion is {0} with a probability of {1} % !".format(
                            prediction_dict[int(prediction_index)], str(prediction[int(prediction_index)] * 100))

                else:
                    raise ImportError('Wrong format')


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

    model_path = 'model/model_melanoma_detection.h5'
    #model_path = 'blabla'

    model = model_loader(model_path=model_path)
    #print(type(model))

    app.run(port=port, debug=True)

