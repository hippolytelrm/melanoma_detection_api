import os
import unittest
import sys
sys.path.append('../')
from preprocessing.image_preprocessing import preprocessing
from PIL import Image
import numpy as np

class TestPreprocessing(unittest.TestCase):

    def test_preprocessing_shape(self):

        sys.path.append('../tests')
        image_path = 'tests/ISIC_6388940.jpg'
        image = Image.open(image_path)
        preprocessed_img = preprocessing(image)
        self.assertEqual(preprocessed_img.shape,(1,224,224,3))

    def test_preprocessing_values(self):
        sys.path.append('../tests')
        image_path = 'tests/ISIC_6388940.jpg'
        image = Image.open(image_path)
        preprocessed_img = preprocessing(image)

        pixels_bool = True
        test_pixel_values = preprocessed_img.all() <= 1. and  preprocessed_img.all() >= 0
        self.assertEqual(test_pixel_values,True)



