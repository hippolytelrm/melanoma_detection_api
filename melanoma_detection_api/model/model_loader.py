import tensorflow as tf
import traceback
import sys
import os

ALLOWED_EXTENSIONS = set(['h5', 'hdf5'])

def model_loader(model_path:str):

    EXTENSION = model_path.split('.')[-1]

    if model_path.split('/')[-1] in os.listdir('model'):
        if EXTENSION not in ALLOWED_EXTENSIONS:
            raise ImportError('Wrong format')

        try:
            model = tf.keras.models.load_model(model_path)
            print("Model successfully loaded")
            return model
        except:
            pass

    else:
        raise ModuleNotFoundError('Model not found')




