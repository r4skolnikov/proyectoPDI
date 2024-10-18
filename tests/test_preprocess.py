import unittest
import cv2
import numpy as np
from preprocess import preprocess_image

class TestPreprocessImage(unittest.TestCase):
    
    def test_small_preprocess_image(self):
        # Crear una imagen de prueba en color (BGR)
        image = np.array([[[255, 0, 0], [0, 255, 0]], [[0, 0, 255], [255, 255, 255]]], dtype=np.uint8)  
        
        # Ejecutar la funcion preprocess_image
        processed_image = preprocess_image(image)
        
        # Verificar que la imagen procesada sea en escala de grises y binarizada correctamente
        expected_output = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, expected_output = cv2.threshold(expected_output, 150, 255, cv2.THRESH_BINARY)
        
        # Verificar si las imagenes son iguales
        np.testing.assert_array_equal(processed_image, expected_output, err_msg="Error en test_small_preprocess_image: Las imágenes procesadas no coinciden.")

    def test_preprocess_big__image(self):
        # Crear una imagen de prueba en color (BGR)
        big_image = np.ones((480, 640, 3), dtype=np.uint8) * 255 
        
        # Ejecutar la funcion preprocess_image
        processed_image = preprocess_image(big_image)
        
        # Verificar que la imagen procesada sea en escala de grises y binarizada correctamente
        expected_output = cv2.cvtColor(big_image, cv2.COLOR_BGR2GRAY)
        _, expected_output = cv2.threshold(expected_output, 150, 255, cv2.THRESH_BINARY)
        
        # Verificar si las imagenes son iguales
        np.testing.assert_array_equal(processed_image, expected_output, err_msg="Error en test_small_preprocess_image: Las imágenes procesadas no coinciden.")

if __name__ == '__main__':
    unittest.main()
