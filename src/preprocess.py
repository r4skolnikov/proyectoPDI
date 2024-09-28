## aqui se aplican filtros a las imagenes para que tesseract funcione mejor

import cv2

def preprocess_image(image):
    """
    Preprocesa la imagen capturada (convertir a escala de grises y binarización).
    Retorna la imagen binarizada.
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)
    return binary
