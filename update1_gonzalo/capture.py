import cv2

def capture_image():
    """
    Captura imágenes desde la cámara web en tiempo real.
    Retorna el fotograma capturado.
    """
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error al abrir la cámara")
        return None

    ret, frame = cap.read()
    if not ret:
        print("Error al capturar el fotograma")
        cap.release()
        return None
    
    # Mensaje que indica que la captura fue exitosa
    print("Captura realizada correctamente")
    
    cap.release()
    return frame
