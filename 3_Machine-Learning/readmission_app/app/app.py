from flask import Flask, request, jsonify
from flasgger import Swagger
import joblib
import numpy as np

app = Flask(__name__)
Swagger(app)  # Initialize Swagger

# Load the trained model
try:
    model = joblib.load("../models/readmission_model.pkl")
except FileNotFoundError:
    raise FileNotFoundError("Model file not found. Ensure 'readmission_model.pkl' exists in the 'models' directory.")
except Exception as e:
    raise RuntimeError(f"Error loading model: {e}")

# Root route
@app.route('/')
def home():
    """
    Home Page
    ---
    responses:
      200:
        description: Welcome message for the API
    """
    return jsonify({"message": "Welcome to the Readmission Prediction API!"})


# Predict route
@app.route('/predict', methods=['POST'])
def predict():
    """
    Predict Readmission
    ---
    parameters:
      - name: input
        in: body
        required: true
        schema:
          type: object
          properties:
            age:
              type: number
            time_in_hospital:
              type: number
            num_lab_procedures:
              type: number
            num_procedures:
              type: number
            num_medications:
              type: number
    responses:
      200:
        description: Predicted readmission likelihood
      400:
        description: Error in input or prediction
    """
    try:
        # Parse input data
        data = request.json

        # Ensure all required keys are present
        required_keys = ['age', 'time_in_hospital', 'num_lab_procedures', 'num_procedures', 'num_medications']
        if not all(key in data for key in required_keys):
            return jsonify({'error': f"Missing required fields. Required fields are: {required_keys}"}), 400

        # Create feature array
        features = np.array([
            data['age'],
            data['time_in_hospital'],
            data['num_lab_procedures'],
            data['num_procedures'],
            data['num_medications']
        ]).reshape(1, -1)

        # Make prediction
        prediction = model.predict(features)
        return jsonify({'readmission': int(prediction[0])})

    except Exception as e:
        return jsonify({'error': str(e)}), 400


# Health check route
@app.route('/health', methods=['GET'])
def health():
    """
    Health Check
    ---
    responses:
      200:
        description: API is running successfully
    """
    return jsonify({'status': 'API is running'})


if __name__ == '__main__':
    app.run(debug=True)
