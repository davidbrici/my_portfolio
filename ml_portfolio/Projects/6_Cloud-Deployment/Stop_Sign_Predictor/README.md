# Stop Sign Predictor

This project trains and deploys a model to classify images of stop signs. The goal is to create a simple image classifier that predicts whether an image contains a stop sign.

## Project Overview

The project includes:

- **Dataset**: Contains training and testing images.
- **Notebooks**: Jupyter notebooks for model training and testing the prediction app.
- **Saved Model**: Where the trained model is stored.
- **App**: A web application for users to upload images and receive classification results.

## File Structure

- `dataset/`
  - `train/`: Training images.
  - `test/`: Testing images.
- `notebooks/`
  - `model-training.ipynb`: Loads the dataset, trains the classifier, and saves the model.
  - `prediction-app.ipynb`: Tests the prediction function with an image.
- `saved_model/`: Contains the trained model.
- `app/`
  - `app.py`: Web app allowing image uploads for classification.
- `requirements.txt`: List of required packages.
- `README.md`: Overview and instructions.

## Steps to Run the Project

1. **Prepare the Environment**:
   - Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```

2. **Train the Model**:
   - Open `notebooks/model-training.ipynb`, load the dataset, train the model, and save it in the `saved_model/` folder.

3. **Deploy the App**:
   - Run the web app using:
     ```bash
     python app/app.py
     ```

## Live Application

Access the live application here: [My Classification App](https://my-classification-app-66c7a4fafca55d73f850957c.1l13rak5ihuh.eu-gb.codeengine.appdomain.cloud)

## Source Code

The application's source code is in the `app` folder. The `app.py` file provides a basic structure for the Flask application.

## Dependencies

Ensure the following packages are installed:
- Python 3.x
- TensorFlow
- OpenCV
- Flask (or Streamlit)
- Additional dependencies listed in `requirements.txt`
