##########To add PYTHON PATH to make sure All Module Loads ########## 
import os
import sys

from modules.dbconnect.models.diabetics import DiabeticModel

path = os.path.abspath(os.path.join(os.getcwd(), "../"))
sys.path.append(path)

####### Importing Library for Works ###########

############ Import Constants Module ##############

from app import db
############ Import Supporting Module ##############
from modules.helper.support import get_classifier


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
    if prediction[0] == 1:
        return_msg = "Diabetic"
    else:
        return_msg = "Not Diabetic"
    diseaseparameter["result"] = return_msg
    diabetic_data = DiabeticModel(**diseaseparameter)
    db.diabetics.insert_one(diabetic_data.dict())
    return return_msg
