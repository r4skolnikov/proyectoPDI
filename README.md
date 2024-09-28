
# Proyecto de Reconocimiento de Escritura a Mano y Conversión a Voz

Este proyecto tiene como objetivo capturar texto escrito a mano en tiempo real, reconocerlo utilizando redes neuronales (Tesseract OCR) y convertir el texto reconocido en voz. El sistema captura la escritura a mano a través de una cámara web, procesa las imágenes para reconocer el texto y lo convierte en palabras habladas utilizando pyttsx3.

## Características
- Captura de imágenes en tiempo real desde una cámara web.
- Preprocesamiento de las imágenes capturadas para mejorar el reconocimiento de texto.
- Reconocimiento de escritura a mano utilizando Tesseract OCR.
- Conversión de texto a voz utilizando pyttsx3.

## Requisitos

### Requisitos de Hardware
- Un computador con cámara web para la captura de imágenes en tiempo real.
- Opcional: Micrófono y altavoces para la interacción por voz.

### Requisitos de Software

- Python 3.8 o superior
- Dependencias listadas en `requirements.txt`

### Dependencias de Python
- `opencv-python` (para capturar imágenes desde la cámara web)
- `pytesseract` (para el reconocimiento de texto utilizando Tesseract OCR)
- `pyttsx3` (para convertir el texto reconocido en voz)

### Instrucciones de Instalación

Sigue estas instrucciones para configurar el proyecto en tu máquina local.

#### 1. Clonar el repositorio
Primero, clona el repositorio desde GitHub a tu máquina local:
```bash
git clone https://github.com/tuusuario/handwriting_recognition_project.git
cd handwriting_recognition_project
```

#### 2. Configurar un entorno virtual
Se recomienda utilizar un entorno virtual para gestionar las dependencias y evitar conflictos con otros proyectos de Python.

##### En Linux/macOS:
1. Crea un entorno virtual:
   ```bash
   python3 -m venv venv
   ```

2. Activa el entorno virtual:
   ```bash
   source venv/bin/activate
   ```

##### En Windows:
1. Crea un entorno virtual:
   ```bash
   python -m venv venv
   ```

2. Activa el entorno virtual:
   ```bash
   venv\Scripts\activate
   ```

#### 3. Instalar las dependencias del proyecto
Una vez que el entorno virtual esté activado, instala las dependencias listadas en `requirements.txt`:

```bash
pip install -r requirements.txt
```

#### 4. Instalar Tesseract OCR
Es necesario tener instalado Tesseract OCR en tu sistema.

- **Linux (distribuciones basadas en Arch)**:
  ```bash
  sudo pacman -S tesseract tesseract-data-eng
  ```

- **Ubuntu/Debian**:
  ```bash
  sudo apt install tesseract-ocr
  ```

- **Windows**:
  Descarga e instala Tesseract OCR desde [aquí](https://github.com/UB-Mannheim/tesseract/wiki).
  Después de la instalación, asegúrate de agregar la ruta de `tesseract.exe` a las variables de entorno.

#### 5. Ejecutar el proyecto
Una vez que todo esté configurado, puedes ejecutar el proyecto utilizando el script principal:

```bash
python src/main.py
```

El sistema comenzará a capturar video desde la cámara web, reconocer el texto escrito a mano y convertirlo en voz.

### Estructura del Proyecto

```
handwriting_recognition_project/
│
├── data/                    # Directorio para almacenar imágenes/videos
│   ├── raw/                 # Imágenes/videos sin procesar
│   └── processed/           # Imágenes/videos procesados
│
├── src/                     # Código fuente del proyecto
│   ├── capture.py           # Código para captura de imágenes desde la cámara web
│   ├── preprocess.py        # Funciones de preprocesamiento de imágenes
│   ├── recognition.py       # Código de reconocimiento de escritura a mano (Tesseract)
│   ├── text_to_speech.py    # Conversión de texto a voz
│   └── main.py              # Script principal para ejecutar el proyecto
│
├── tests/                   # Pruebas unitarias para todos los módulos
│   ├── test_capture.py      # Pruebas para el módulo de captura
│   ├── test_preprocess.py   # Pruebas para el módulo de preprocesamiento
│   ├── test_recognition.py  # Pruebas para el módulo de reconocimiento
│   └── test_text_to_speech.py # Pruebas para el módulo de conversión de texto a voz
│
├── .gitignore               # Archivo gitignore
├── README.md                # Documentación (este archivo)
└── requirements.txt         # Dependencias del proyecto
```

## Ejecutar Pruebas

Las pruebas unitarias para los módulos están ubicadas en el directorio `tests/`. Puedes ejecutar las pruebas utilizando `pytest`:

```bash
pytest
```

### Cómo ejecutar las pruebas
1. Asegúrate de tener pytest instalado en tu entorno virtual:
   ```bash
   pip install pytest
   ```

2. Ejecuta todas las pruebas:
   ```bash
   pytest
   ```

Esto ejecutará todas las pruebas unitarias para verificar que los módulos de captura, preprocesamiento, reconocimiento y conversión de texto a voz funcionen correctamente.

## Problemas Conocidos

- El sistema puede tener dificultades en entornos con poca luz o con escritura de baja calidad.
- Se recomienda la aceleración por GPU para un reconocimiento de texto más rápido, aunque no es obligatoria.
- En grandes cantidades de texto, puede haber un retraso en la conversión de texto a voz.

## Mejoras Futuras

- Mejorar la precisión del modelo entrenando con un conjunto de datos más grande de muestras de escritura a mano.
- Mejorar la conversión de texto a voz con opciones más avanzadas.
- Implementar un manejo de errores más avanzado para casos donde no se puede reconocer el texto.

## Licencia

Este proyecto está bajo la licencia MIT - consulta el archivo [LICENSE](LICENSE) para más detalles.
