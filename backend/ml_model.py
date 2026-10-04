import pandas as pd

# Load dataset
df = pd.read_csv(
    "./dataset/phiusil_dataset/PhiUSIIL_Phishing_URL_Dataset.csv"
)

# Features we will use
features = [
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
    "IsHTTPS",
    "NoOfURLRedirect",
    "HasPasswordField",
    "Bank",
    "Pay",
    "Crypto"
]

print("Selected Features:")
print(features)

print("\nNumber of Features:", len(features))

print("\nDataset Shape:", df.shape)
# Input features
X = df[features]

# Target
y = df["label"]

print("\nX Shape:", X.shape)
print("y Shape:", y.shape)
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTraining Data:", X_train.shape)
print("Testing Data:", X_test.shape)

# Create ML model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Train model
model.fit(X_train, y_train)

print("\nML Model Training Completed!")
from sklearn.metrics import accuracy_score, classification_report

# Make predictions
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", accuracy)
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
import joblib

# Save trained model
joblib.dump(model, "backend/phishing_model.pkl")

print("\nModel saved successfully!")