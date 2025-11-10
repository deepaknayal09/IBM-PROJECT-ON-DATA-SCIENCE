# IBM-PROJECT-ON-DATA-SCIENCE
# 🩺 Human Disease Prediction System

A web-based application that predicts potential diseases based on user-selected symptoms.  
This project integrates *Machine Learning (Random Forest Classifier), a **Flask backend, and a **simple HTML/CSS frontend* to provide a functional proof-of-concept for applying Data Science in healthcare.

---

## 📖 Table of Contents
1. Executive Summary  
2. Problem Statement  
3. Project Objectives  
4. System Architecture  
5. Technology Stack  
6. Data Collection & Preparation  
7. Model Training  
8. Backend Development (Flask)  
9. Frontend Development (HTML/CSS)  
10. Deployment & Usage  
11. Future Scope  
12. Conclusion  
13. References  

---

## 🚀 Executive Summary
The *Disease Prediction System* helps users identify possible diseases based on symptoms they select.  
It uses a *Random Forest Classifier* trained on a custom dataset, served via Flask, and displayed through a clean web interface.  
This project demonstrates the synergy between *data science, backend development, and frontend design* to solve real-world problems.

---

## ❓ Problem Statement
Medical information online is often:
- *Overwhelming*: Too much unstructured data.  
- *Lacking Context*: A single symptom can have many causes.  
- *Anxiety-Inducing*: Misleading results can causeiagnosis.  

This system provides structured, contextual predictions to reduce misinformation and encourage timely medical consultation.

---

## 🎯 Project Objectives
1. *Data Processing*: Preprocess CSV dataset with one-hot encoding for symptoms and label encoding for diseases.  
2. *Model Training*: Train a Random Forest Classifier and save it as model.pkl.  
3. *Backend Development*: Build Flask server (app.py) to handle requests and predictions.  
4. *Frontend Development*: Create a simple HTML/CSS interface for symptom selection and result display.  
5. *Integration*: Ensure seamless communication between frontend, backend, and ML model.

---

## 🛠 System Architecture
1. *Dataset Creator* (dataset_creator.py) → Generates disease_dataset.csv.  
2. *Model Trainer* (train_model.py) → Encodes data, trains Random Forest, saves model.pkl.  
3. *Flask App* (app.py) → Loads model, serves homepage, handles predictions.  
4. *Frontend* (index.html, style.css) → User interface for symptom selection and prediction display.

---

## 💻 Technology Stack
- *Python* (core language)  
- *Scikit-learn* (Random Forest Classifier)  
- *Pandas & NumPy* (data manipulation)  
- *Flask* (backend framework)  
- *HTML, CSS* (frontend design)  
- *Jinja2* (templating engine)  
- *Pickle* (model serialization)

---

## 📊 Data Collection & Preparation
- *Dataset*: disease_dataset.csv with symptoms as columns and disease labels.  
- *Preprocessing*:
  - One-Hot Encoding for symptoms.  
  - Label Encoding for diseases.  

---

## 🤖 Model Training
- Algorithm: *Random Forest Classifier (100 trees)*  
- Train/Test Split: 80/20  
- Output: Serialized model (model.pkl)  

---

## ⚙ Backend Development (Flask)
- **Home Route (/): Renders symptom selection page.  
- **Prediction Route (/predict): Accepts symptoms, transforms input, predicts disease, returns result.  

---

## 🎨 Frontend Development
- **HTML (index.html): Checkbox form for symptoms, result display.  
- **CSS (style.css): Clean, minimal styling with focus on usability.  

---

## 📦 Deployment & Usage
1. Create virtual environment:  
   ```bash
   python -m venv venv
2. Activate environment:  
   - Windows: venv\Scripts\activate  
   - Linux/Mac: source venv/bin/activate  
3. Install dependencies:  
   `bash
   pip install flask pandas scikit-learn python-docx reportlab
   `
4. Generate dataset:  
   `bash
   python dataset_creator.py
   `
5. Train model:  
   `bash
   python train_model.py
   `
6. Run Flask app:  
   `bash
   python app.py
   `
7. Open browser at:  
   `
   http://127.0.0.1:5000/
   `

---

🔮 Future Scope
- Use advanced models (e.g., deep learning).  
- Add database integration for dynamic data.  
- Implement user accounts & history tracking.  
- Enhance UI/UX with search, detailed results.  
- Add medical disclaimer prominently.  

---

✅ Conclusion
This project successfully integrates machine learning, backend, and frontend into a functional application.  
It serves as a proof-of-concept for healthcare-related AI tools and provides a strong foundation for future improvements.

---

📚 References
1. Breiman, L. (2001). Random Forests. Machine Learning, 45(1), 5-32.  
2. Pedregosa, F., et al. (2011). Scikit-learn: Machine Learning in Python. JMLR, 12, 2825-2830.  
3. McKinney, W. (2010). Data Structures for Statistical Computing in Python. SciPy Conference.  
4. Ronacher, A. Flask Web Development Documentation. Pallets Project.  
