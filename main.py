from flask_cors import CORS
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_swagger_ui import get_swaggerui_blueprint

from data_models.diabetic import diabetic

import json
import pickle

# webserver gateway interphase (WSGI)
app = Flask(__name__)
api = Api(app)

# Configure Swagger UI
SWAGGER_URL = '/swagger1'
API_URL = '/swagger1.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Sample API"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)


@app.route('/swagger1.json')
def swagger():
    with open('swagger1.json', 'r') as f:
        return jsonify(json.load(f))

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
