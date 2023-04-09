from flask_cors import CORS
from flask import Flask, request, jsonify

# from lightgbm import LGBMClassifier

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

pickle_chronic_kidney = open("models/chronic_kidney.pkl", "rb")
classifier_chronic_kidney = pickle.load(pickle_chronic_kidney)

pickle_heart_disease = open("models/heart_disease.pkl", "rb")
classifier_heart_disease = pickle.load(pickle_heart_disease)

pickle_liver_disease = open("models/liver.pkl", "rb")
classifier_liver_disease = pickle.load(pickle_liver_disease)


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


@app.route('/api/v1/kidney_chronic', methods=['POST'])
def kidney_chronic():
    if request.method == 'POST':

        data = request.get_json(force=True)

        age = data["age"]
        bp = data["bp"]
        sg = data["sg"]
        al = data["al"]
        su = data["su"]
        rbc = data["rbc"]
        pc = data["pc"]
        pcc = data["pcc"]
        ba = data["ba"]
        bgr = data["bgr"]
        bu = data["bu"]
        sc = data["sc"]
        sod = data["sod"]
        pot = data["pot"]
        hemo = data["hemo"]
        pcv = data["pcv"]
        wc = data["wc"]
        rc = data["rc"]
        htn = data["htn"]
        dm = data["dm"]
        cad = data["cad"]
        appet = data["appet"]
        pe = data["pe"]
        ane = data["ane"]

        prediction = classifier_chronic_kidney.predict(
            [[age, bp, sg, al, su, rbc, pc, pcc, ba, bgr, bu, sc, sod, pot, hemo, pcv, wc, rc, htn, dm, cad, appet, pe,
              ane]])

        if prediction[0] == 1:
            return jsonify("Chronic Kidney Disease")
        else:
            return jsonify("Not Chronic Kidney Disease")


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


@app.route('/api/v1/heart_disease', methods=['POST'])
def heart_disease():
    if request.method == 'POST':

        data = request.get_json(force=True)

        age = data["age"]
        sex = data["sex"]
        cp = data["cp"]
        trestbps = data["trestbps"]
        chol = data["chol"]
        fbs = data["fbs"]
        restecg = data["restecg"]
        thalach = data["thalach"]
        exang = data["exang"]
        oldpeak = data["oldpeak"]
        slope = data["slope"]
        ca = data["ca"]
        thal = data["thal"]

        prediction = classifier_heart_disease.predict(
            [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

        if prediction[0] == 1:
            return jsonify("Heart Disease")
        else:
            return jsonify("No Heart Disease")


@app.route('/api/v1/liver_disease', methods=['POST'])
def liver_disease():
    if request.method == 'POST':

        data = request.get_json(force=True)

        Age = data["Age"]
        Gender_Female = data["Gender_Female"]
        Gender_Male = data["Gender_Male"]
        Total_Bilirubin = data["Total_Bilirubin"]
        Direct_Bilirubin = data["Direct_Bilirubin"]
        Alkaline_Phosphotase = data["Alkaline_Phosphotase"]
        Alamine_Aminotransferase = data["Alamine_Aminotransferase"]
        Aspartate_Aminotransferase = data["Aspartate_Aminotransferase"]
        Total_Protiens = data["Total_Protiens"]
        Albumin = data["Albumin"]
        Albumin_and_Globulin_Ratio = data["Albumin_and_Globulin_Ratio"]

        prediction = classifier_liver_disease.predict(
            [[Age, Gender_Female, Gender_Male, Total_Bilirubin, Direct_Bilirubin, Alkaline_Phosphotase,
              Alamine_Aminotransferase, Aspartate_Aminotransferase, Total_Protiens, Albumin,
              Albumin_and_Globulin_Ratio]])

        if prediction[0] == 1:
            return jsonify("Liver Disease")
        else:
            return jsonify("No Liver Disease")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
