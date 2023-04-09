##########To add PYTHON PATH to make sure All Module Loads ########## 
import os
import sys
path = os.path.abspath(os.path.join(os.getcwd(),"../"))
sys.path.append(path)


####### Importing Library for Works ###########
import logging

############ Import Constants Module ##############
import APP_Constants as AC

############ Import Supporting Module ##############
from modules.helper.support import get_classifier



def get_response(diseaseparameter):
    classifier_heart_disease = get_classifier(disease="heart_disease")
    age = diseaseparameter["age"]
    sex = diseaseparameter["sex"]
    cp = diseaseparameter["cp"]
    trestbps = diseaseparameter["trestbps"]
    chol = diseaseparameter["chol"]
    fbs = diseaseparameter["fbs"]
    restecg = diseaseparameter["restecg"]
    thalach = diseaseparameter["thalach"]
    exang = diseaseparameter["exang"]
    oldpeak = diseaseparameter["oldpeak"]
    slope = diseaseparameter["slope"]
    ca = diseaseparameter["ca"]
    thal = diseaseparameter["thal"]

    prediction = classifier_heart_disease.predict(
        [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

    if prediction[0] == 1:
        return_msg = "Heart Disease"
    else:
        return_msg = "No Heart Disease"
    return return_msg