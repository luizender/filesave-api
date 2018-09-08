"""
This module has the class of Google Cloud Storage

"""
from google.cloud import storage, exceptions
from api.settings import (GCLOUD_PROJECT, GCLOUD_STORAGE_BUCKET,
                          GCLOUD_STORAGE_ROOT_PATH, GCLOUD_STORAGE_CHUNK_SIZE)
from .storage import Storage


class GCloudStorage(Storage):
    """
    This class is responsible to upload, get and delete files from Google Cloud Storage

    """

    def __init__(self):
        """
        Create a new Google Cloud Storage instance

        """
        self.client = storage.Client(project=GCLOUD_PROJECT)
        self.bucket = self.client.get_bucket(GCLOUD_STORAGE_BUCKET)

    def upload(self, file):
        """
        Upload a file to the Google Cloud Storage

        :param file: The file to upload
        :type file: file
        """
        filename = '%s/%s' % (GCLOUD_STORAGE_ROOT_PATH, file.filename)
        blob = self.bucket.blob(filename, chunk_size=GCLOUD_STORAGE_CHUNK_SIZE)
        blob.upload_from_string(file.read(), content_type=file.content_type)

    def get(self, filename=None):
        """
        Get a file or list all files (with filename is None)
        from the Google Cloud Storage

        :param filename: The name of file to get
        :type filename: str
        :return: The list of files or the specific file
        """
        if not filename:
            list_files = []
            blobs = self.bucket.list_blobs(prefix=GCLOUD_STORAGE_ROOT_PATH)
            for blob in blobs:
                list_files.append({
                    'filename': blob.name[len(GCLOUD_STORAGE_ROOT_PATH):],
                    'content_type': blob.content_type,
                    'size': blob.size
                })
            return list_files

        filename = '%s/%s' % (GCLOUD_STORAGE_ROOT_PATH, filename)
        blob = self.bucket.get_blob(filename)
        if not blob:
            raise FileNotFoundError()

        return {
            'filename': blob.name,
            'content_type': blob.content_type,
            'size': blob.size,
        }

    def delete(self, filename):
        """
        Delete a file from the Google Cloud Storage

        :param filename: The name of file to delete
        :type filename: str
        """
        filename = '%s/%s' % (GCLOUD_STORAGE_ROOT_PATH, filename)
        try:
            self.bucket.delete_blob(filename)
        except exceptions.NotFound:
            raise FileNotFoundError()
