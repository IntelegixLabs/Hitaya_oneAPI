##########To add PYTHON PATH to make sure All Module Loads ########## 
import os
import sys

path = os.path.abspath(os.path.join(os.getcwd(), "../"))
sys.path.append(path)

####### Importing Library for Works ###########
import logging

############ Import Constants Module ##############
import APP_Constants as AC

############ Import Supporting Module ##############
from modules.helper.support import get_classifier
from app import db


def get_response(diseaseparameter):
    classifier_diabetic = get_classifier(disease="diabetic")
    pregnancies = diseaseparameter["Pregnancies"]
    glucose = diseaseparameter["Glucose"]
    bloodpressure = diseaseparameter["BloodPressure"]
    skinthickness = diseaseparameter["SkinThickness"]
    insulin = diseaseparameter["Insulin"]
    bmi = diseaseparameter["BMI"]
    diabetespedigreefunction = diseaseparameter["DiabetesPedigreeFunction"]
    age = diseaseparameter["Age"]

    prediction = classifier_diabetic.predict(
        [[pregnancies, glucose, bloodpressure, skinthickness, insulin, bmi, diabetespedigreefunction, age]])
    payload = {"Pregnancies": pregnancies,
               "Glucose": glucose,
               "BloodPressure": bloodpressure,
               "SkinThickness": skinthickness,
               "Insulin": insulin, "BMI": bmi,
               "DiabetesPedigreeFunction": diabetespedigreefunction,
               "Age": age}
    if prediction[0] == 1:
        return_msg = "Diabetic"
    else:
        return_msg = "Not Diabetic"
    payload["result"] = return_msg
    db.diabetics.insert_one(payload)
    return return_msg
