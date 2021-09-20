import tensorflow as tf
import traceback
import sys

def model_loader(model_name:str):
    try:
        model = tf.keras.models.load_model(model_name)
        print("Model successfully loaded")
    except:
        print("Could not find the required model")
        traceback.print_exc(file=sys.stdout)


    return model