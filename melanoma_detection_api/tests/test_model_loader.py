import unittest
import sys
sys.path.append('../')
from model.model_loader import model_loader
#import model_loader
import os


class TestModelLoading(unittest.TestCase):

    def test_module_not_found(self):
        model_path = ' '
        self.assertRaises(ModuleNotFoundError, model_loader, model_path)

    def test_wrong_format(self):
        model_path = '../model/ISIC_6388940.jpg'
        self.assertRaises(ImportError, model_loader, model_path)

