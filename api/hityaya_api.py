######### Import Path into System Path ###########
import os
import os.path
import sys
path = os.path.abspath(os.path.join(os.getcwd(),"./."))
sys.path.append(path)

####### Importing  Flask Component and required python lib ##################

from flask import request,jsonify,Blueprint
from flask_api import status
import logging

######## Importing Supporting Lib #################

import APP_Constants as AC


####### Importing responses from Disease Modules #########
from modules.helper.support import get_disease_response


######## Creating Blueprint for all APIs #########

disease_Blueprint = Blueprint('disease_Blueprint',__name__)




######### Function for return disease assesment #######

@disease_Blueprint.route('/disease',methods = ['POST'])
def disease():
    """disease API 

    Returns:
        [JSON]: [disease Model result JSON]
    """
    try:
        inputpayload =  request.get_json(cache= False)
        logging.info("Request came for Disease - %s",inputpayload['disease'])
        result = get_disease_response(disease=inputpayload['disease'],diseaseparameter=inputpayload['parameters'])
        logging.info("Prediction for Disease - %s",result)
        return jsonify(result), status.HTTP_200_OK
    except Exception as err:
        return jsonify(f"Module - Error - {err}"), status.HTTP_400_BAD_REQUEST