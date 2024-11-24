
# Proyecto OCR para Digitalización de Texto Manuscrito

Este proyecto es una herramienta diseñada para facilitar el acceso a texto manuscrito tanto a personas ciegas como a usuarios regulares. Utilizando tecnologías de reconocimiento óptico de caracteres (OCR) y síntesis de texto a voz (TTS), el programa permite digitalizar texto manuscrito de manera eficiente y accesible.

## Motivación

El proyecto tiene dos objetivos principales:
1. **Accesibilidad para personas ciegas**: Brindar una herramienta que permita a las personas ciegas interpretar texto manuscrito mediante una interacción sencilla, basada en TTS y teclas con relieve (`f` y `j`).
2. **Digitalización para estudiantes y oficinistas**: Permitir a los usuarios normales digitalizar texto manuscrito de forma rápida y generar documentos PDF o métricas de rendimiento.

## Instalación de Requerimientos

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/r4skolnikov/proyectoPDI.git
   cd proyectoPDI
   ```

2. **Instalar dependencias**:
   Asegúrate de tener Python 3.8 o superior instalado. Luego, ejecuta:
   ```bash
   pip install -r requirements.txt
   ```

   Si planeas usar una GPU con PyTorch, instala la versión específica de `torch` para tu versión de CUDA:
   ```bash
   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
   ```

3. **Verificar instalación**:
   Una vez instaladas las dependencias, puedes ejecutar el programa:
   ```bash
   python main.py --help
   ```

## Uso

El programa tiene dos modos principales:

### 1. Modo para Personas Ciegas
Este modo utiliza TTS para guiar al usuario. Las interacciones se realizan mediante las teclas:
- **`f`**: Captura de imagen desde la cámara para procesar texto manuscrito.
- **`j`**: Se presiona tres veces consecutivas (`jjj`) para salir del programa.

Para iniciar este modo, ejecuta:
```bash
python main.py --blind
```

### 2. Modo CLI para Usuarios Normales
En este modo, puedes usar diversas flags para realizar tareas específicas:
- **Procesar una imagen**: 
  ```bash
  python main.py --image ruta/a/imagen.jpg
  ```
- **Leer el texto reconocido con TTS**:
  ```bash
  python main.py --image ruta/a/imagen.jpg --tts
  ```
- **Generar un PDF**:
  ```bash
  python main.py --image ruta/a/imagen.jpg --generate-pdf
  ```
- **Generar métricas y gráficos**:
  ```bash
  python main.py --metrics
  ```

Para ver todas las opciones disponibles:
```bash
python main.py --help
```

## Características

- **Reconocimiento de Texto**: Basado en EasyOCR, optimizado para texto manuscrito.
- **Compatibilidad con GPU**: Acelera el procesamiento utilizando PyTorch.
- **Digitalización a PDF**: Convierte el texto digitalizado en documentos PDF.
- **Análisis de Rendimiento**: Genera métricas y gráficos del tiempo de procesamiento y confianza del OCR.
- **Accesibilidad mediante TTS**: Permite a personas ciegas interpretar texto manuscrito fácilmente.

---

