import unittest
import cv2

class TestCaptureImage(unittest.TestCase):

    #Verificar si hay una camara disponible
    def test_camera_detected(self):
        camera = cv2.VideoCapture(0)
        camera_avaible = camera.isOpened()
        self.assertTrue(camera_avaible)

    #Verificar si hay captura
    def test_capture(self):
        camera = cv2.VideoCapture(0)
        self.assertIsNotNone(camera.read)
    

if __name__ == '__main__':
    unittest.main()