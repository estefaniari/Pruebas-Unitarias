# test_app.py
import unittest
from app import area_triangulo

class TestAreaTriangulo(unittest.TestCase):

    def test_area_triangulo(self):
        self.assertEqual(area_triangulo(3, 4), 6) 
    
    def test_area_triangulo_base_negativa(self):
        with self.assertRaises(ValueError):
            area_triangulo(-3, 4)

    def test_area_triangulo_altura_cero(self):
        with self.assertRaises(ValueError):
            area_triangulo(3, 0)  
