import joblib
import pandas as pd

from ml_feature_extractor import extract_ml_features


# Load model
model = joblib.load("backend/phishing_url_model.pkl")


# Features used by model
feature_names = [
    "URLLength",
    "DomainLength",
    "IsDomainIP",
    "NoOfSubDomain",
    "HasObfuscation",
    "NoOfObfuscatedChar",
    "NoOfLettersInURL",
    "NoOfDegitsInURL",
    "NoOfEqualsInURL",
    "NoOfQMarkInURL",
    "NoOfAmpersandInURL",
    "IsHTTPS"
]


# URLs to test
urls = [
    "https://google.com",
    "http://example-123456.com",
    "http://secure-login-account-123456789.com/@verify"
]


# Test each URL
for url in urls:

    features = extract_ml_features(url)

    X = pd.DataFrame(
        [[features[name] for name in feature_names]],
        columns=feature_names
    )

    prediction = model.predict(X)[0]
    probability = model.predict_proba(X)[0]

legitimate_probability = probability[0] * 100
phishing_probability = probability[1] * 100

print("Legitimate Probability:", round(legitimate_probability, 2), "%")
print("Phishing Probability:", round(phishing_probability, 2), "%")
print("\n--------------------------------")
print("URL:", url)
print("ML Prediction:", prediction)

if prediction == 0:
        print("Result: LEGITIMATE")
else:
        print("Result: PHISHING")