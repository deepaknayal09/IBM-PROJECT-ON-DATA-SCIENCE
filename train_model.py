import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score


# Load the dataset
df = pd.read_csv('disease_dataset.csv')

# Separate features and target
X = df.drop('Disease', axis=1)
y = df['Disease']

# Save symptom list for the frontend
with open('symptoms.py', 'w') as f:
    f.write(f"all_symptoms = {list(X.columns)}")

# Encode target labels
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# Save label encoder for decoding predictions later (optional)
with open('label_encoder.pkl', 'wb') as f:
    pickle.dump(le, f)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))


# Save the model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as model.pkl")
