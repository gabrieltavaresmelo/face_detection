# 😎 Face Detection with OpenCV

This project demonstrates how to detect faces in an image using OpenCV's Haar Cascade Classifier. The program loads an image, detects faces, draws rectangles around them, and saves the result.

## 📋 Table of Contents
1. [Prerequisites](#prerequisites)
2. [Setup Instructions](#setup-instructions)
3. [Running the Code](#running-the-code)
4. [Environment Management](#environment-management)
5. [How It Works](#how-it-works)
6. [License](#license)
7. [Contributing](#contributing)

---

## ✅ Prerequisites

- 🐍 **Python 3.10+**
- 🖼️ **OpenCV 4.x**
- 🐾 **Conda** (optional, but recommended for managing environments)

Make sure you have [Anaconda](https://www.anaconda.com/products/distribution) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html) installed to easily manage the Python environment.

---

## 🚀 Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/gabrieltavaresmelo/face_detection
cd face_detection
```

### 2️⃣ Create and Activate Virtual Environment (Optional)
To isolate the project dependencies, it's a good practice to use a virtual environment:
```bash
conda create --name facedetection pip python=3.10
conda activate facedetection
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

Alternatively, if you don't have a `requirements.txt` yet:
```bash
pip install opencv-python
pip install opencv-python-headless
```

---

## ▶️ Running the Code

1. Place an image named `sample.jpg` in the project directory or modify the image path in the code.

2. Download the pre-trained Haar Cascade XML file:
   - You can download the `haarcascade_frontalface_default.xml` from [OpenCV's GitHub repository](https://github.com/opencv/opencv/tree/master/data/haarcascades).

3. Run the Python script:
```bash
python camera.py
python image.py
```

Once the code is executed, the original image and the result with detected faces will be displayed in separate windows. The result image will also be saved as `sample-result.jpg`.

---

## 🛠️ Environment Management

Here are some useful `conda` commands to manage the virtual environment for this project:

- **List all environments**:
    ```bash
    conda info --envs
    ```

- **Remove an environment**:
    ```bash
    conda env remove --name facedetection
    ```

- **Activate the environment**:
    ```bash
    conda activate facedetection
    ```

- **Deactivate the environment**:
    ```bash
    conda deactivate
    ```

- **Save installed dependencies**:
    ```bash
    pip freeze > requirements-lock.txt
    ```

---

## 🔍 How It Works

The following steps are executed in the Python script:

1. **Load the Haar Cascade Classifier**:
    The `haarcascade_frontalface_default.xml` is used to detect faces in the image.

2. **Read the Input Image**:
    The script loads an image (`sample.jpg`) using `cv2.imread()`.

3. **Convert to Grayscale**:
    The image is converted to grayscale using `cv2.cvtColor()` for better performance in face detection.

4. **Detect Faces**:
    Faces are detected using the `detectMultiScale()` method of the cascade classifier.

5. **Draw Rectangles**:
    For each detected face, a rectangle is drawn around the face using `cv2.rectangle()`.

6. **Display and Save Results**:
    The original and the resulting images are displayed using `cv2.imshow()`, and the result is saved as `sample-result.jpg`.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 🤝 Contributing

Contributions are welcome! If you'd like to contribute, feel free to fork this repository and submit a pull request.
