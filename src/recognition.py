# aqui se hace la magia

# src/recognition.py

import pytesseract

def recognize_text(image):
    """
    Reconoce el texto en una imagen preprocesada utilizando Tesseract OCR.
    Retorna el texto reconocido.
    """
    text = pytesseract.image_to_string(image)
    return text
