import os
import unittest
import sys
sys.path.append('../')
from prediction_api import predict
from model.model_loader import model_loader
from PIL import Image
import numpy as np

class TestModelPrediction(unittest.TestCase):

    def test_prediction_benign(self):

        #image_path = 'data/benign/ISIC_5907599.jpg'
        #image = Image.open(image_path)

        model_path = 'model/model_melanoma_classification.h5'
        model = model_loader(model_path=model_path)

        result = predict()
        self.assertEqual(result,0)

    """
    def test_prediction_melanoma(self):
        sys.path.append('../tests')
        image_path = 'tests/ISIC_6388940.jpg'
        image = Image.open(image_path)
        preprocessed_img = preprocessing(image)

        pixels_bool = True
        test_pixel_values = preprocessed_img.all() <= 1. and  preprocessed_img.all() >= 0
        self.assertEqual(test_pixel_values,True)
    """


