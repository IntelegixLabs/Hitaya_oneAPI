##########To add PYTHON PATH to make sure All Module Loads ########## 
import os
import sys

from app import db
from modules.dbconnect.models.liver import LiverModel

path = os.path.abspath(os.path.join(os.getcwd(), "../"))
sys.path.append(path)

####### Importing Library for Works ###########

############ Import Constants Module ##############
############ Import Supporting Module ##############
from modules.helper.support import get_classifier


def get_response(diseaseparameter):
    classifier_liver_disease = get_classifier(disease="liver_disease")
    age = diseaseparameter["Age"]
    gender_female = diseaseparameter["Gender_Female"]
    gender_male = diseaseparameter["Gender_Male"]
    total_bilirubin = diseaseparameter["Total_Bilirubin"]
    direct_bilirubin = diseaseparameter["Direct_Bilirubin"]
    alkaline_phosphotase = diseaseparameter["Alkaline_Phosphotase"]
    alamine_aminotransferase = diseaseparameter["Alamine_Aminotransferase"]
    aspartate_aminotransferase = diseaseparameter["Aspartate_Aminotransferase"]
    total_protiens = diseaseparameter["Total_Protiens"]
    albumin = diseaseparameter["Albumin"]
    albumin_and_globulin_ratio = diseaseparameter["Albumin_and_Globulin_Ratio"]

    prediction = classifier_liver_disease.predict(
        [[age, gender_female, gender_male, total_bilirubin, direct_bilirubin, alkaline_phosphotase,
          alamine_aminotransferase, aspartate_aminotransferase, total_protiens, albumin,
          albumin_and_globulin_ratio]])

    if prediction[0] == 1:
        return_msg = "Liver Disease"
    else:
        return_msg = "No Liver Disease"

    diseaseparameter["result"] = return_msg

    liver_data = LiverModel(**diseaseparameter)
    db.liver.insert_one(liver_data.dict())
    return return_msg
