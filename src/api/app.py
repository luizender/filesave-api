"""
This module has the App and Routes of API

"""
import json
import logging.config
from flask import Flask
from flask_restful import Api
from api.resources import File
from api.resources.storage import GCloudStorage
from api.settings import LOGGING_FILE

APP = Flask(__name__)
API = Api(APP)

API.add_resource(File, '/file', '/file/<string:filename>',
                 resource_class_kwargs={'storage': GCloudStorage()})

if __name__ == '__main__':
    # set up proper logging.
    with open(LOGGING_FILE, "r", encoding="utf-8") as config:
        logging.config.dictConfig(json.load(config))
    APP.run(host='0.0.0.0', use_reloader=True)
