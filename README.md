
# Handwriting Recognition and Text-to-Speech Project

This project aims to recognize handwritten text using neural networks and convert the recognized text into speech. The system captures handwriting in real-time using a webcam, processes the images, recognizes the text, and then converts the text to speech.

## Features
- Real-time handwriting capture via webcam.
- Preprocessing of captured images to improve recognition accuracy.
- Handwriting recognition using a deep neural network (DNN).
- Conversion of recognized text to speech using text-to-speech (TTS) technology.

## Requirements

### Hardware
- A computer with a webcam for real-time handwriting capture.

### Software
- Python 3.8 or higher
- Virtual environment for dependency management

## Installation

Follow these steps to set up the project on your local machine.

### 1. Clone the repository
First, clone the repository from GitHub to your local machine:
```bash
git clone https://github.com/r4skolnikov/proyectoPDI.git
cd proyectoPDI
```

### 2. Set up a virtual environment
It's important to use a virtual environment to manage the project dependencies and avoid conflicts with other Python projects.

#### Linux (Arch Linux or similar)
1. Install `python-virtualenv` if you don't have it:
   ```bash
   sudo pacman -S python-virtualenv
   ```

2. Create a virtual environment in the project directory:
   ```bash
   virtualenv venv
   ```

3. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```

#### Other OS (Optional)
- On Windows:
   ```bash
   venv\Scripts\activate
   ```
- On macOS:
   ```bash
   source venv/bin/activate
   ```

### 3. Install dependencies
Once the virtual environment is activated, install the project dependencies using `pip`:

```bash
pip install -r requirements.txt
```

This will install all necessary libraries, such as:
- `opencv-python`
- `numpy`
- `tensorflow` or `torch` (depending on the model implementation)
- `gTTS` for text-to-speech conversion

### 4. Set up your webcam
Make sure that your computer’s webcam is working. You can test it by running a small OpenCV script.

If the webcam is working correctly, you should see a live video feed from your camera.

## Project Structure

```
handwriting_recognition_project/
│
├── data/                    # Directory for storing images/videos
│   ├── raw/                 # Unprocessed images/videos
│   └── processed/           # Preprocessed images/videos
│
├── models/                  # Neural network models
│   └── handwriting_model.py # Handwriting recognition model
│
├── src/                     # Source code for the project
│   ├── capture.py           # Webcam capture code
│   ├── preprocess.py        # Image preprocessing functions
│   ├── recognition.py       # Handwriting recognition code
│   ├── text_to_speech.py    # Text-to-speech conversion code
│   └── main.py              # Main script to run the project
│
├── tests/                   # Unit tests
├── notebooks/               # Jupyter notebooks for experimentation
├── .gitignore               # Git ignore file to avoid unnecessary files
├── README.md                # Project documentation (this file)
└── requirements.txt         # Project dependencies
```

## Running the Project

### 1. Running the project
Once everything is set up, you can run the project using the `main.py` script. This script will orchestrate the entire workflow: capturing the image, processing it, recognizing the text, and converting it to speech.

Make sure the virtual environment is activated, and run the following command:

```bash
python src/main.py
```

### 2. Expected Behavior
- The webcam will open, and the system will capture a frame of handwritten text.
- The image will be preprocessed (converted to grayscale, binarized, etc.).
- The text in the image will be recognized using the neural network.
- The recognized text will be converted to speech, and you should hear the output through your speakers.

## Customization

- **Modify the model:** You can modify the neural network model in the `models/handwriting_model.py` file if you want to experiment with different architectures.
- **Tuning preprocessing steps:** If you need to adjust the image preprocessing steps (e.g., noise reduction, binarization), you can edit `src/preprocess.py`.

## Running Tests

Unit tests are located in the `tests/` directory. To run the tests, use:

```bash
python -m unittest discover tests
```

This will run all unit tests to ensure that the preprocessing, recognition, and text-to-speech functionalities are working as expected.

## Known Issues

- The system might struggle with poor-quality handwriting or images with low resolution.
- GPU support is recommended for faster neural network inference.

## Future Enhancements

- Improve model accuracy by training with a larger dataset of handwriting samples.
- Add more advanced text-to-speech options.
- Implement more robust error handling for cases where the text cannot be recognized.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
