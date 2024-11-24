import argparse
import re
import time
from capture import capture_image
from preprocess import preprocess_image
from recognition import recognize_text
from text_to_speech import speak_text
from metrics_collector import MetricsCollector
from pdf_generator import generate_pdf

# Inicializa el recolector de métricas
metrics_collector = MetricsCollector()

def handle_blind_mode():
    """
    Modo interactivo para personas ciegas.
    Utiliza TTS para guiar y las teclas 'f' y 'j' para interacciones básicas.
    Proporciona instrucciones claras y requiere presionar 'jjj' para salir del programa.
    """
    explain_blind_mode()  

    quit_sequence = ""
    while True:
        command = input("Presiona 'f' para capturar o 'j' para salir: ").strip().lower()

        if command == 'f':
            speak_text("Por favor, acerque el texto a la cámara.")
            time.sleep(2)  

            speak_text("Capturando imagen en 3... 2... 1...")
            image_path = capture_image()  
            if not image_path:
                speak_text("No se pudo capturar la imagen. Intenta de nuevo.")
                continue

            speak_text("Puede retirar el texto de la cámara.")
            time.sleep(1)  

            speak_text("Procesando la imagen...")
            processed_image = preprocess_image(image_path)  

            speak_text("Reconociendo texto...")
            text = recognize_text(processed_image)  
            if text:
                speak_text(f"El texto reconocido es: {text}")
            else:
                speak_text("No se detectó texto en la imagen.")

        elif command == 'j':
            quit_sequence += 'j'
            if quit_sequence == 'jjj':
                speak_text("Saliendo del programa. Hasta luego.")
                break
        else:
            quit_sequence = "" 
            speak_text("Comando no reconocido. Intenta de nuevo.")


def handle_normal_mode(args):
    """
    Modo para usuarios normales.
    Permite digitalizar texto, generar PDFs, escuchar texto y generar métricas.
    """
    if args.image:
        if not re.match(r"^[\w,\s-]+\.[A-Za-z]{3,4}$", args.image):
            raise ValueError("La ruta de la imagen no es válida.")

        print("Preprocesando la imagen...")
        processed_image = preprocess_image(args.image)

        print("Reconociendo texto...")
        text = recognize_text(processed_image)
        print("Texto reconocido:")
        print(text)

        if args.tts:
            speak_text(text)

        if args.generate_pdf:
            print("Generando PDF...")
            generate_pdf("texto_digitalizado.pdf", text)
            print("PDF generado: texto_digitalizado.pdf")

    if args.metrics:
        metrics_collector.save_metrics_to_csv()
        metrics_collector.plot_metrics()


def explain_blind_mode():
    """
    Explica el funcionamiento del modo ciego al usuario mediante TTS.
    """
    speak_text("Bienvenido al modo para personas ciegas.")
    speak_text("Este programa te permitirá capturar texto manuscrito y escuchar el resultado.")
    speak_text("Presiona la tecla 'f' para capturar una imagen. A continuación, te indicaremos cuándo acercar el texto a la cámara y cuándo retirarlo.")
    speak_text("Para salir del programa, presiona tres veces consecutivas la tecla 'j'.")
    speak_text("¡Comencemos!")


def main():
    """
    Punto de entrada principal del programa.
    Permite elegir entre el modo para personas ciegas y el modo para usuarios normales.
    """
    parser = argparse.ArgumentParser(
        description="""
Proyecto OCR para digitalizar texto manuscrito.

Este programa tiene dos modos principales:

1. Modo para personas ciegas (--blind): 
   Permite interactuar con el programa mediante TTS y teclas específicas 
   ('f' para capturar imágenes y 'j' para salir).

2. Modo CLI para usuarios normales:
   Permite digitalizar imágenes, generar PDFs, escuchar el texto digitalizado 
   y generar métricas de rendimiento.
        """,
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        "--blind",
        action="store_true",
        help="Activa el modo para personas ciegas, manejado mediante TTS y teclas específicas."
    )
    parser.add_argument(
        "--image",
        type=str,
        help="Ruta de la imagen para procesar mediante OCR. (Solo para modo CLI)."
    )
    parser.add_argument(
        "--tts",
        action="store_true",
        help="Lee el texto digitalizado usando TTS. (Solo para modo CLI)."
    )
    parser.add_argument(
        "--generate-pdf",
        action="store_true",
        help="Genera un PDF con el texto digitalizado. (Solo para modo CLI)."
    )
    parser.add_argument(
        "--metrics",
        action="store_true",
        help="Genera métricas y gráficos de rendimiento del OCR. (Solo para modo CLI)."
    )
    parser.add_argument(
        "--help",
        action="help",
        help="Muestra esta ayuda y termina el programa."
    )

    args = parser.parse_args()

    if args.blind:
        handle_blind_mode()
    else:
        handle_normal_mode(args)


if __name__ == "__main__":
    main()
