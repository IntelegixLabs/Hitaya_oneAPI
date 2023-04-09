##########To add PYTHON PATH to make sure All Module Loads ########## 
import os
import sys
path = os.path.abspath(os.path.join(os.getcwd(),"../"))
sys.path.append(path)

####### Importing Library for Works ###########
import logging

############ Import Constants Module ##############
import APP_Constants as AC

from modules.helper.support import get_classifier



def get_response(diseaseparameter):

    classifier_chronic_kidney = get_classifier(disease="chronic_kidney")
    age = diseaseparameter["age"]
    bp = diseaseparameter["bp"]
    sg = diseaseparameter["sg"]
    al = diseaseparameter["al"]
    su = diseaseparameter["su"]
    rbc = diseaseparameter["rbc"]
    pc = diseaseparameter["pc"]
    pcc = diseaseparameter["pcc"]
    ba = diseaseparameter["ba"]
    bgr = diseaseparameter["bgr"]
    bu = diseaseparameter["bu"]
    sc = diseaseparameter["sc"]
    sod = diseaseparameter["sod"]
    pot = diseaseparameter["pot"]
    hemo = diseaseparameter["hemo"]
    pcv = diseaseparameter["pcv"]
    wc = diseaseparameter["wc"]
    rc = diseaseparameter["rc"]
    htn = diseaseparameter["htn"]
    dm = diseaseparameter["dm"]
    cad = diseaseparameter["cad"]
    appet = diseaseparameter["appet"]
    pe = diseaseparameter["pe"]
    ane = diseaseparameter["ane"]

    prediction = classifier_chronic_kidney.predict(
        [[age, bp, sg, al, su, rbc, pc, pcc, ba, bgr, bu, sc, sod, pot, hemo, pcv, wc, rc, htn, dm, cad, appet, pe,
            ane]])

    if prediction[0] == 1:
        return_msg="Chronic Kidney Disease"
    else:
        return_msg="Not Chronic Kidney Disease"
    return return_msg
