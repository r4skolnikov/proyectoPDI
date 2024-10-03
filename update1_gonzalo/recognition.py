import pytesseract

def recognize_text(image):
    """
    Reconoce el texto en una imagen preprocesada utilizando Tesseract OCR.
    Retorna el texto reconocido y las coordenadas del cuadro del texto.
    """
    # Obtener el texto reconocido
    text = pytesseract.image_to_string(image, lang='eng')  # Cambia 'eng' si es necesario
    
    # Obtener las cajas delimitadoras del texto
    boxes = pytesseract.image_to_boxes(image)  # Obtiene las coordenadas de los caracteres
    
    return text, boxes
