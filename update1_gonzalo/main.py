import cv2
from capture import capture_image
from preprocess import preprocess_image
from recognition import recognize_text
from text_to_speech import text_to_speech

def capture_and_process():
    cap = cv2.VideoCapture(0)  # Abre la cámara
    frame_counter = 0  # Contador para procesar cada cierto número de fotogramas

    if not cap.isOpened():
        print("Error al abrir la cámara")
        return

    while True:
        ret, frame = cap.read()  # Captura el fotograma de la cámara en tiempo real
        if not ret:
            print("Error al capturar el fotograma")
            break

        frame_counter += 1

        # Procesar cada 20 fotogramas para mejorar el rendimiento
        if frame_counter % 20 == 0:
            # Preprocesar la imagen (blanco y negro, binarización)
            processed_image = preprocess_image(frame)

            # Usar Tesseract para reconocer el texto y obtener las coordenadas
            text, boxes = recognize_text(processed_image)
            
            # Imprimir el texto reconocido en la consola
            print(f'Texto reconocido (longitud {len(text)}): "{text}"')

            # Convertir el texto reconocido a voz
            if text.strip():  # Solo si se reconoce texto
                text_to_speech(text)

        # Mostrar el video en tiempo real
        cv2.imshow('Captura en tiempo real', frame)

        # Salir del ciclo al presionar 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()  # Liberar la cámara cuando termina el ciclo
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_and_process()

