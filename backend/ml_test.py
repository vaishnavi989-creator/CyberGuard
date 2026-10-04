import joblib
import pandas as pd

from ml_feature_extractor import extract_ml_features


# Load trained ML model
model = joblib.load("backend/phishing_model.pkl")


# Test URL
url = "https://google.com"


# Extract features
features = extract_ml_features(url)


# Convert features into DataFrame
X = pd.DataFrame([features])


# Make prediction
prediction = model.predict(X)[0]

print("URL:", url)
print("ML Prediction:", prediction)

if prediction == 1:
    print("Result: LEGITIMATE")
else:
    print("Result: PHISHING")