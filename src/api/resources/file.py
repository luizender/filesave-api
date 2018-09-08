"""
The file resource object

"""
import werkzeug
from flask_restful import Resource, reqparse


class File(Resource):
    """
    The File resource is responsible for list, create and update file
    to Google Cloud Storage
    """

    def __init__(self):
        super().__init__()

        self.post_parser = reqparse.RequestParser()
        self.post_parser.add_argument('file', type=werkzeug.datastructures.FileStorage,
                                      location='files', required=True)

    def get(self, filaname=None):
        """
        List all files or get the specific file

        :param filaname: The filename to get or None (to get the list)
        :type filaname: str
        """
        pass

    def post(self, filename):
        """
        Upload the file to Google Cloud Storage

        :param filename: The name of file to upload
        :type filename: str
        """
        pass

    def delete(self, filename):
        """
        Delete the file from Google Cloud Storage

        :param filename: The name of file to delete
        :type filename: str
        """
        pass
