from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

# Load the trained model
model_path = 'model.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])

def predict():
    try:
        # Fetching form data
        age = int(request.form['age'])
        sex = int(request.form['sex'])
        cp = int(request.form['cp'])
        trestbps = int(request.form['trestbps'])
        chol = int(request.form['chol'])
        fbs = int(request.form['fbs'])
        restecg = int(request.form['restecg'])
        thalach = int(request.form['thalach'])
        exang = int(request.form['exang'])
        oldpeak = float(request.form['oldpeak'])
        slope = int(request.form['slope'])
        ca = int(request.form['ca'])
        thal = int(request.form['thal'])

        # Example prediction logic
        # Replace this with your model prediction
        if age > 50 and chol > 200:
            result = "High Risk of Heart Attack"
        else:
            result = "Low Risk of Heart Attack"

        # Render the same page with the result
        return render_template('index.html', result=result)

    except Exception as e:
        return render_template('index.html', result="An error occurred: " + str(e))


if __name__ == "__main__":
    app.run(debug=True)

