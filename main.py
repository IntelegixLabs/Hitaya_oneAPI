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

pickle_breast_cancer = open("models/breast_cancer.pkl", "rb")
classifier_breast_cancer = pickle.load(pickle_breast_cancer)


@app.route('/api/v1/breast_cancer', methods=['POST'])
def breast_cancer():
    if request.method == 'POST':

        data = request.get_json(force=True)

        radius_mean = data["radius_mean"]
        texture_mean = data["texture_mean"]
        perimeter_mean = data["perimeter_mean"]
        area_mean = data["area_mean"]
        smoothness_mean = data["smoothness_mean"]
        compactness_mean = data["compactness_mean"]
        concavity_mean = data["concavity_mean"]
        concave_points_mean = data["concave_points_mean"]
        symmetry_mean = data["symmetry_mean"]
        fractal_dimension_mean = data["fractal_dimension_mean"]
        radius_se = data["radius_se"]
        texture_se = data["texture_se"]
        perimeter_se = data["perimeter_se"]
        area_se = data["area_se"]
        smoothness_se = data["smoothness_se"]
        compactness_se = data["compactness_se"]
        concavity_se = data["concavity_se"]
        concave_points_se = data["concave_points_se"]
        symmetry_se = data["symmetry_se"]
        fractal_dimension_se = data["fractal_dimension_se"]
        radius_worst = data["radius_worst"]
        texture_worst = data["texture_worst"]
        perimeter_worst = data["perimeter_worst"]
        area_worst = data["area_worst"]
        smoothness_worst = data["smoothness_worst"]
        compactness_worst = data["compactness_worst"]
        concavity_worst = data["concavity_worst"]
        concave_points_worst = data["concave_points_worst"]
        symmetry_worst = data["symmetry_worst"]
        fractal_dimension_worst = data["fractal_dimension_worst"]

        prediction = classifier_breast_cancer.predict([[radius_mean, texture_mean, perimeter_mean, area_mean,
                                                        smoothness_mean, compactness_mean, concavity_mean,
                                                        concave_points_mean, symmetry_mean, fractal_dimension_mean,
                                                        radius_se, texture_se, perimeter_se, area_se, smoothness_se,
                                                        compactness_se, concavity_se, concave_points_se, symmetry_se,
                                                        fractal_dimension_se, radius_worst, texture_worst,
                                                        perimeter_worst, area_worst, smoothness_worst,
                                                        compactness_worst,
                                                        concavity_worst, concave_points_worst, symmetry_worst,
                                                        fractal_dimension_worst]])

        if prediction[0] == "M":
            return jsonify("Malignant")
        else:
            return jsonify("Benign")


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

        prediction = classifier_diabetic.predict(
            [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

        if prediction[0] == 1:
            return jsonify("Diabetic")
        else:
            return jsonify("Not Diabetic")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
