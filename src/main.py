## aqui se junta todo

from capture import capture_image
from preprocess import preprocess_image
from recognition import recognize_text
from text_to_speech import text_to_speech
import cv2

def capture_and_process():
    frame_counter = 0  # Contador para procesar cada cierto número de fotogramas

    while True:
        # Capturar la imagen desde la cámara
        frame = capture_image()
        if frame is None:
            break

        # Procesar cada 20 fotogramas para mejorar el rendimiento
        frame_counter += 1
        if frame_counter % 20 == 0:
            # Preprocesar la imagen (blanco y negro, binarización)
            processed_image = preprocess_image(frame)

            # Usar Tesseract para reconocer el texto
            text = recognize_text(processed_image)
            print(f'Texto reconocido: {text}')

            # Convertir el texto reconocido a voz
            if text.strip():
                text_to_speech(text)

        # Mostrar el video en tiempo real
        cv2.imshow('Captura en tiempo real', frame)

        # Salir del ciclo al presionar 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_and_process()
