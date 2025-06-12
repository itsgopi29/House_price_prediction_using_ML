from flask import Flask, render_template, request
import pickle
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get values from the form
    features = [float(x) for x in request.form.values()]
    final_input = np.array([features])
    prediction = model.predict(final_input)
    price_lakhs = prediction[0]

    # Convert lakhs to crore and lakh
    total_lakhs = int(price_lakhs)
    crore = total_lakhs // 100
    lakhs = total_lakhs % 100

    result = "Estimated House Price: ₹ "

    if crore > 0:
        result += f"{crore} crore "
    if lakhs > 0:
        result += f"{lakhs} lakh"

    return render_template('index.html', prediction_text=result.strip())

if __name__ == '__main__':
    app.run(debug=True)
