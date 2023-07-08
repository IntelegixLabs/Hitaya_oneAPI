##########To add PYTHON PATH to make sure All Module Loads ########## 
import os
import sys

from app import db
from modules.dbconnect.models.breast_cancer import BreastCancerModel

path = os.path.abspath(os.path.join(os.getcwd(), "../"))
sys.path.append(path)

####### Importing Library for Works ###########

############ Import Constants Module ##############
from modules.helper.support import get_classifier


def get_response(diseaseparameter):
    classifier_breast_cancer = get_classifier(disease="breast_cancer")
    radius_mean = diseaseparameter["radius_mean"]
    texture_mean = diseaseparameter["texture_mean"]
    perimeter_mean = diseaseparameter["perimeter_mean"]
    area_mean = diseaseparameter["area_mean"]
    smoothness_mean = diseaseparameter["smoothness_mean"]
    compactness_mean = diseaseparameter["compactness_mean"]
    concavity_mean = diseaseparameter["concavity_mean"]
    concave_points_mean = diseaseparameter["concave_points_mean"]
    symmetry_mean = diseaseparameter["symmetry_mean"]
    fractal_dimension_mean = diseaseparameter["fractal_dimension_mean"]
    radius_se = diseaseparameter["radius_se"]
    texture_se = diseaseparameter["texture_se"]
    perimeter_se = diseaseparameter["perimeter_se"]
    area_se = diseaseparameter["area_se"]
    smoothness_se = diseaseparameter["smoothness_se"]
    compactness_se = diseaseparameter["compactness_se"]
    concavity_se = diseaseparameter["concavity_se"]
    concave_points_se = diseaseparameter["concave_points_se"]
    symmetry_se = diseaseparameter["symmetry_se"]
    fractal_dimension_se = diseaseparameter["fractal_dimension_se"]
    radius_worst = diseaseparameter["radius_worst"]
    texture_worst = diseaseparameter["texture_worst"]
    perimeter_worst = diseaseparameter["perimeter_worst"]
    area_worst = diseaseparameter["area_worst"]
    smoothness_worst = diseaseparameter["smoothness_worst"]
    compactness_worst = diseaseparameter["compactness_worst"]
    concavity_worst = diseaseparameter["concavity_worst"]
    concave_points_worst = diseaseparameter["concave_points_worst"]
    symmetry_worst = diseaseparameter["symmetry_worst"]
    fractal_dimension_worst = diseaseparameter["fractal_dimension_worst"]

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
        return_msg = "Malignant"
    else:
        return_msg = "Benign"
    diseaseparameter["result"] = return_msg
    breast_cancer_data = BreastCancerModel(**diseaseparameter)

    db.breast_cancer.insert_one(breast_cancer_data.dict())
    return return_msg
