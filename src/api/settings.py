"""
This module has the settings of project

"""
import os

# General configuration of API
API_MODE = os.environ.get('API_MODE', 'prod')
LOGGING_FILE = os.path.join(os.path.dirname(__file__), 'logging.json')

# Google Cloud Storage configuration
GCLOUD_PROJECT = os.environ.get('GCLOUD_PROJECT', 'filesave')
GCLOUD_STORAGE_BUCKET = os.environ.get(
    'GCLOUD_STORAGE_BUCKET', 'filesave-storage')
GCLOUD_STORAGE_ROOT_PATH = '/' + API_MODE
GCLOUD_STORAGE_CHUNK_SIZE = os.environ.get('GCLOUD_STORAGE_CHUNK_SIZE', 524288)
