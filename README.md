# 🚦 Traffic Volume Prediction WebApp

This is a **Flask-based machine learning web application** that predicts traffic volume based on user inputs such as weather conditions, date-time, temperature, etc.  

The prediction engine is built using **MLPRegressor** from scikit-learn, with input and output scaling handled by **MinMaxScaler**. The model was trained on real-world data obtained from **Kaggle**.

---

## 📁 Dataset Source

The dataset used for model training was obtained from Kaggle:  
🔗 [Traffic Volume Dataset on Kaggle](https://www.kaggle.com/datasets)

- **Format:** CSV  
- **Content:** Hourly traffic volume data 
- **Features:** Date-time, temperature, weather, holiday, humidity etc  
- **Target:** Traffic volume

---

## 🧠 Machine Learning Model

- **Model Used:** `MLPRegressor` (Multi-Layer Perceptron Regressor)  
- **Scaler:** `MinMaxScaler` used for both inputs and outputs  
- **Training Steps:**
  - Feature engineering (e.g., extracting hour, day from datetime)
  - Normalization using MinMaxScaler
  - Model trained and saved using `pickle`

### 🔐 Saved Model Files

- `trained_model1.sav` → MinMaxScaler for input features  
- `trained_model2.sav` → MinMaxScaler for output target  
- `trained_model3.sav` → Trained MLPRegressor model

---

## 🌐 Web Application Features

- Input form to accept traffic conditions and time  
- Flask backend serves model predictions  
- Real-time prediction shown on the same page  
- Simple and responsive web UI using HTML/CSS

---

## ⚙️ How to Run This Project Locally

> 💡 Make sure Python 3.7 or higher is installed.

# Clone the repository
**git clone https://github.com/Vasu1203/Traffic-Volume-Prediction-Flask-WebApp.git**

# Create virtual environment
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Install the dependencies
pip install -r requirements.txt

# Run the Flask app
python app.py




