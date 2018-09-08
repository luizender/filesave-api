"""
This module has the App and Routes of API

"""

from flask import Flask
from flask_restful import Api
from api.resources import File

APP = Flask(__name__)
API = Api(APP)

API.add_resource(File, '/file', '/file/<string:filename>')

if __name__ == '__main__':
    APP.run(host='0.0.0.0', debug=True)
