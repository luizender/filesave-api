"""
This module has the settings of project

"""
import os

# General configuration of API
API_MODE = os.environ.get('API_MODE', 'prod')
API_DEVEL_MODE = API_MODE == 'devel'
LOGGING_FILE = os.path.join(os.path.dirname(__file__), 'logging.json')

# Google Cloud Storage configuration
GCLOUD_PROJECT = os.environ.get('GCLOUD_PROJECT', 'filesave')
GCLOUD_STORAGE_BUCKET = os.environ.get(
    'GCLOUD_STORAGE_BUCKET', 'filesave-storage')
GCLOUD_STORAGE_ROOT_PATH = '/dev' if API_DEVEL_MODE else '/prod'
GCLOUD_STORAGE_CHUNK_SIZE = os.environ.get('GCLOUD_STORAGE_CHUNK_SIZE', 524288)
