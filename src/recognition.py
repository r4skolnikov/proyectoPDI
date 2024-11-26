# aqui se hace la magia

# src/recognition.py

import easyocr
from gpu_manager import check_gpu

def ocr_with_easyocr(image_path, use_gpu=None):
    """
    Reconocimiento de texto usando EasyOCR con soporte GPU.
    """
    if use_gpu is None:
        use_gpu = check_gpu()

    reader = easyocr.Reader(['en','es'], gpu=use_gpu)
    results = reader.readtext(image_path)
    print(results)
    return results



def recognize_text(image_path):
    text = ocr_with_easyocr(image_path)
    return text


