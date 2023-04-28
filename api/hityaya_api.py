######### Import Path into System Path ###########
import os
import os.path
import sys

path = os.path.abspath(os.path.join(os.getcwd(), "./."))
sys.path.append(path)

####### Importing  Flask Component and required python lib ##################

from flask import request, jsonify, Blueprint, Response
from flask_api import status
import logging
from modules.diseases import chest_xray
import cv2
import json

######## Importing Supporting Lib #################

import APP_Constants as AC

####### Importing responses from Disease Modules #########
from modules.helper.support import get_disease_response

######## Creating Blueprint for all APIs #########

disease_Blueprint = Blueprint('disease_Blueprint', __name__)


######### Function for return disease assesment #######

UPLOAD_FOLDER = 'static/upload'

@disease_Blueprint.route('/disease/predictImage', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']
        filename = f.filename

        # save our image in upload folder
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        f.save(file_path)  # save image into upload folder
        # get predictions

        # import pdb
        # pdb.set_trace()
        host = request.headers.get('HOST')

        # Make prediction
        pred_image, predictions = chest_xray.chest_xray(source=file_path)
        pred_filename = 'prediction_image.jpg'
        cv2.imwrite(f'./static/predict/{pred_filename}', pred_image)

        print(predictions)

        report = []
        for i, obj in enumerate(predictions):
            imagex = obj['roi']  # grayscale image (array)
            x = obj['x']  # name
            y = obj['y']  # name
            w = obj['w']  # name
            h = obj['h']  # name
            class_name = obj['prediction_class']  # name
            prediction_score = obj['prediction_score']  # probability score

            # save grayscale and eigne in predict folder
            image = f'roi_{i}.jpg'
            cv2.imwrite(f'./static/predict/{image}', imagex)

            # save report
            report.append(["http://"+host+"/static/predict/"+image,
                           x,
                           y,
                           w,
                           h,
                           class_name,
                           prediction_score,
                           "http://" + host + "/static/predict/" + pred_filename])

        # Do some processing, get output_imgs
        return Response(json.dumps(report), mimetype='application/json')

    return None

@disease_Blueprint.route('/disease', methods=['POST'])
def disease():
    """disease API 

    Returns:
        [JSON]: [disease Model result JSON]
    """
    try:
        inputpayload = request.get_json(cache=False)
        logging.info("Request came for Disease - %s", inputpayload['disease'])
        result = get_disease_response(disease=inputpayload['disease'], diseaseparameter=inputpayload['parameters'])
        logging.info("Prediction for Disease - %s", result)
        return jsonify(result), status.HTTP_200_OK
    except Exception as err:
        return jsonify(f"Module - Error - {err}"), status.HTTP_400_BAD_REQUEST
