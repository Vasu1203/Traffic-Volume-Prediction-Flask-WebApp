from flask import Flask, render_template, request
import joblib

# Load model and scalers
model = joblib.load("trained_model3.sav")
x_scaler = joblib.load("trained_model1.sav")
y_scaler = joblib.load("trained_model2.sav")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [float(request.form[key]) for key in [
            'is_holiday', 'temperature', 'weekday', 'hour',
            'month_day', 'year', 'month', 'weather_type', 'weather_description'
        ]]
        
        scaled_input = x_scaler.transform([features])
        prediction = model.predict(scaled_input)
        predicted_traffic = y_scaler.inverse_transform([prediction])[0][0]

        if predicted_traffic <= 1000:
            traffic_status = "No Traffic"
        elif predicted_traffic <= 3000:
            traffic_status = "Busy or Normal Traffic"
        elif predicted_traffic <= 5500:
            traffic_status = "Heavy Traffic"
        else:
            traffic_status = "Worst Case"

        return render_template('result.html', traffic=round(predicted_traffic, 2), status=traffic_status)
    
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
