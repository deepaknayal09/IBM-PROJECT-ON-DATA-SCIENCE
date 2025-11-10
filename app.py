from flask import Flask, render_template, request
import pickle
from symptoms import all_symptoms

app = Flask(__name__)

# Load model and label encoder
model = pickle.load(open('model.pkl', 'rb'))
label_encoder = pickle.load(open('label_encoder.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html', symptoms=all_symptoms)

@app.route('/predict', methods=['POST'])
def predict():
    selected = request.form.getlist('symptoms')
    input_vector = [1 if symptom in selected else 0 for symptom in all_symptoms]
    prediction_encoded = model.predict([input_vector])[0]
    prediction = label_encoder.inverse_transform([prediction_encoded])[0]
    return render_template('index.html', symptoms=all_symptoms, result=f"Predicted Disease: {prediction}")

if __name__ == '__main__':
    app.run(debug=True)
