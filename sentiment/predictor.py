# sentiment/predictor.py

import os
import joblib

# Get the path to the ml folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ML_PATH = os.path.join(BASE_DIR, "ml")

# Load model and vectorizer
model = joblib.load(os.path.join(ML_PATH, "model.pkl"))
vectorizer = joblib.load(os.path.join(ML_PATH, "vectorizer.pkl"))

def predict_sentiment(text):
    # Transform the input
    X = vectorizer.transform([text])
    # Predict
    prediction = model.predict(X)
    return prediction[0]
