"""
This module is responsible for create an Abstract class to

"""


class Storage:
    """
    This module is responsible for create an Abstract class to Storage

    """

    def upload(self, file):
        """
        Upload a file to the Storage

        :param file: The file to upload
        :type file: file
        :raises NotImplementedError: This method is not implemented for the Storage class
        """
        raise NotImplementedError('Upload method not implemented yet.')

    def get(self, filename=None):
        """
        Get a file or list all files (with filename is None) from the Storage

        :param filename: The name of file to get
        :type filename: str
        :raises NotImplementedError: This method is not implemented for the Storage class
        """
        raise NotImplementedError('Get method not implemented yet.')

    def delete(self, filename):
        """
        Delete a file from the Storage

        :param filename: The name of file to delete
        :type filename: str
        :raises NotImplementedError: This method is not implemented for the Storage class
        """
        raise NotImplementedError('Delete method not implemented yet.')
