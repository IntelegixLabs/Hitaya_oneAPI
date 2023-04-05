from flask_cors import CORS
from flask import Flask, request, jsonify

from data_models.diabetic import diabetic

import pickle

# webserver gateway interphase (WSGI)
app = Flask(__name__)

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

# Loading Models

pickle_diabetic = open("models/diabetic.pkl", "rb")
classifier_diabetic = pickle.load(pickle_diabetic)


@app.route('/api/v1/diabetic', methods=['POST'])
def diabetic():
    if request.method == 'POST':

        data = request.get_json(force=True)

        Pregnancies = data["Pregnancies"]
        Glucose = data["Glucose"]
        BloodPressure = data["BloodPressure"]
        SkinThickness = data["SkinThickness"]
        Insulin = data["Insulin"]
        BMI = data["BMI"]
        DiabetesPedigreeFunction = data["DiabetesPedigreeFunction"]
        Age = data["Age"]

        prediction = classifier_diabetic.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

        if prediction[0] == 1:
            return jsonify("Diabetic")
        else:
            return jsonify("Not Diabetic")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
