# test_app.py
import unittest
from app import area_triangulo

class TestAreaTriangulo(unittest.TestCase):

    def test_area_triangulo(self):
        self.assertEqual(area_triangulo(3, 4), 6) 
