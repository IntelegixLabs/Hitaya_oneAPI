from importlib import import_module
import os.path
import pickle
import time


def get_disease_response(disease,diseaseparameter):
    diseasefilepath = 'modules/diseases/'+disease+'.py'
    diseasemodulename = 'modules.diseases.' + disease
    if os.path.isfile(diseasefilepath):
        diseasemodule = import_module(diseasemodulename)
        if callable(getattr(diseasemodule, 'get_response')):
            diseasereturnmethod = getattr(diseasemodule, "get_response")
            diseaseresponse = diseasereturnmethod(diseaseparameter)
        else:
            raise ModuleNotFoundError("get_response method is not present in the disease file")
    else:
        raise FileNotFoundError("Disease file is not present")
    return diseaseresponse


def get_classifier(disease):
    pickle_source = 'resources/models/'+disease+'.pkl'
    pickle_disease = open(pickle_source, "rb")
    classifier_disease = pickle.load(pickle_disease)
    return classifier_disease


