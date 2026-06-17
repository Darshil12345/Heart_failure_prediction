# ❤️ Heart Failure Prediction System

A Django-based Machine Learning web application that predicts the likelihood of heart disease using patient health parameters. The system uses a trained Random Forest Classifier and provides secure user authentication, prediction history management, search, and pagination features.

🔗 Live Demo: https://heart-failure-prediction-2-bqaq.onrender.com

## Features
- User Registration & Login
- Heart Disease Prediction using Machine Learning
- Prediction History Tracking
- Search & Pagination
- Responsive Bootstrap UI
- Secure Authentication

## Tech Stack
- Python
- Django
- Scikit-Learn
- Pandas & NumPy
- Bootstrap 5
- SQLite
- Render

## Dataset
Heart Failure Prediction Dataset from Kaggle containing 11 clinical features such as Age, Chest Pain Type, Blood Pressure, Cholesterol, ECG Results, and Maximum Heart Rate to predict heart disease risk. :contentReference[oaicite:0]{index=0}

## Installation

```bash
git clone https://github.com/Darshil12345/Heart_failure_prediction.git
cd Heart_failure_prediction

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
