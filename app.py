######## Importing Lib for Python works and Flasks #################
from flask import Flask
from flask_cors import CORS
import logging
from logging.handlers import RotatingFileHandler

######## Importing Supporting Lib #################
import APP_Constants as AC

###### importing the API blueprints #######
from api.hityaya_api import disease_Blueprint

app = Flask(__name__)
CORS(app)

app.register_blueprint(blueprint=disease_Blueprint, url_prefix=AC.APP_ENDPOINT)

rth = logging.handlers.RotatingFileHandler(
    filename='./logs/HitayaLog.log',
    maxBytes=25000,
    backupCount=10
)

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s  : %(message)s', handlers=[rth])

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
