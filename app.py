from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('churn_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    tenure = float(request.form['tenure'])
    monthly = float(request.form['monthly'])
    total = float(request.form['total'])

    features = [[tenure, monthly, total]]

    prediction = model.predict(features)[0]

    result = "Will Churn" if prediction == 1 else "Will Stay"

    return render_template('index.html', prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)
