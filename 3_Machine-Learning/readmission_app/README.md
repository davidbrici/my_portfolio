
# Patient Readmission Prediction API

## Overview
This project develops a Flask-based API to predict the likelihood of patient readmission within 30 days. The prediction is based on features derived from a healthcare dataset. The API hosts a machine learning model trained using logistic regression.

## Features
- **/predict**: Accepts patient data as input and returns the likelihood of readmission.
- **/health**: Confirms the API's status.
- Swagger documentation is integrated for interactive testing.

## Requirements
- Python 3.9+
- Conda for environment management
- Libraries:
  - Flask
  - Flask-RESTful
  - Flasgger
  - Pandas
  - NumPy
  - Scikit-learn
  - Joblib

## Setup Instructions
1. Clone the repository and navigate to the project directory:
   ```bash
   git clone <repository_url>
   cd flask_app
   ```

2. Create and activate a Conda environment:
   ```bash
   conda create --name readmission_env python=3.9
   conda activate readmission_env
   ```

3. Install required libraries:
   ```bash
   pip install flask flask-restful flasgger pandas numpy scikit-learn joblib
   ```

4. Run the Flask app:
   ```bash
   python app.py
   ```

5. Test the API using Swagger or Postman.

## API Endpoints
### /predict
- **Method**: POST
- **Input**: JSON object containing patient data
  - Example:
    ```json
    {
      "age": 65,
      "time_in_hospital": 5,
      "num_lab_procedures": 43,
      "num_procedures": 2,
      "num_medications": 15
    }
    ```
- **Output**: JSON response
  - Example:
    ```json
    {
      "readmission": 1
    }
    ```

### /health
- **Method**: GET
- **Output**: JSON object confirming the API status
  - Example:
    ```json
    {
      "status": "API is running"
    }
    ```

## Dataset Preprocessing
- Columns with excessive missing values (`weight`, `payer_code`, `medical_specialty`) were dropped.
- Categorical variables were encoded using one-hot encoding or label encoding.
- The target variable `readmitted` was binarized (`<30` mapped to 1, others to 0).

## Model Details
- **Algorithm**: Logistic Regression
- **Features**:
  - Age
  - Time in hospital
  - Number of lab procedures
  - Number of medications
  - And others...
- **Accuracy**: ~88% on the test dataset.

## Documentation
Swagger UI is available at `http://127.0.0.1:5000/apidocs` once the API is running.

## Future Improvements
- Add token-based authentication.
- Expand feature set for predictions.
- Deploy the API using a cloud service.


