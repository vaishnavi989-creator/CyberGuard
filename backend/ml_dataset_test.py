import joblib
import pandas as pd

from ml_feature_extractor import extract_ml_features


# Load model
model = joblib.load("backend/phishing_url_model.pkl")


# Features used during training
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


# Known URLs from dataset
test_urls = [
    ("http://www.teramill.com", 0),
    ("http://www.f0519141.xsph.ru", 0),
    ("https://www.southbankmosaics.com", 1),
    ("https://www.uni-mainz.de", 1)
]


for url, actual_label in test_urls:

    features = extract_ml_features(url)

    X = pd.DataFrame(
        [[features[name] for name in feature_names]],
        columns=feature_names
    )

    prediction = model.predict(X)[0]

    print("\n--------------------------------")
    print("URL:", url)
    print("Actual Label:", actual_label)
    print("Predicted Label:", prediction)

    if prediction == 0:
        print("Prediction: LEGITIMATE")
    else:
        print("Prediction: PHISHING")

    if prediction == actual_label:
        print("Correct: YES")
    else:
        print("Correct: NO")