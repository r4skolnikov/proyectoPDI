import cv2

def preprocess_image(image):
    """
    Preprocesa la imagen capturada (convertir a escala de grises y binarización).
    Retorna la imagen binarizada.
    """
    # Convertir a escala de grises
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Ajustar el valor del umbral para la binarización
    _, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)  # Prueba con un umbral de 150
    
    return binary

