"""
The file resource object

"""
import logging
import werkzeug
from flask_restful import Resource, reqparse, abort

LOGGER = logging.getLogger(__name__)


class File(Resource):
    """
    The File resource is responsible for list, create and update file
    to Google Cloud Storage
    """

    def __init__(self, **kwargs):
        """
        Create a new File instance

        :param \\**kwargs: See below

        :Keyword Arguments:
            * *storage* (``Storage``) -- The storage instance

        """
        self.storage = kwargs['storage']

        self.post_parser = reqparse.RequestParser()
        self.post_parser.add_argument('file', type=werkzeug.datastructures.FileStorage,
                                      location='files', required=True)

    def get(self, filename=None):
        """
        List all files or get the specific file

        :param filename: The filename to get or None (to get the list)
        :type filename: str
        """
        try:
            return self.storage.get(filename)
        except FileNotFoundError:
            abort(404, message='File %s does not exist' % filename)
        except BaseException:
            message = 'Failed to list the files of storage'
            if filename:
                message = 'Failed to get the file ' + filename

            abort(500, message=message)

            LOGGER.error('A generic exception has occurred.', exc_info=True)

    def post(self):
        """
        Upload the file to Google Cloud Storage

        """
        data = self.post_parser.parse_args()

        try:
            LOGGER.debug('Trying to upload file  to storage')
            self.storage.upload(data.file)
            LOGGER.debug('The file was uploaded with success')
            return {
                'filename': data.file.filename,
                'message': 'The file was uploaded with success'
            }
        except BaseException:
            abort(500, message='The file was not uploaded')
            LOGGER.error('A generic exception has occurred.', exc_info=True)

    def delete(self, filename):
        """
        Delete the file from Google Cloud Storage

        :param filename: The name of file to delete
        :type filename: str
        """
        try:
            self.storage.delete(filename)
            return {
                'filename': filename,
                'message': 'The file was deleted with success'
            }
        except FileNotFoundError:
            abort(404, message='File %s does not exist' % filename)
        except BaseException:
            abort(500, message='Failed to delete the file ' + filename)
            LOGGER.error('A generic exception has occurred.', exc_info=True)
