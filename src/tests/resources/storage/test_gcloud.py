"""
Test the Storage class

"""
from unittest import TestCase
from werkzeug.datastructures import FileStorage
from api.resources.storage import GCloudStorage


class TestGCloudStorage(TestCase):
    """
    Test the GCloudStorage class

    """

    def setUp(self):
        """
        Set up test

        """
        self.file = FileStorage(filename='/dummy', name='/dummy')
        self.storage = GCloudStorage()

    def test_upload_invalid_file(self):
        """
        Test the if the upload function raise an error to a invalid file

        """
        self.assertRaises(AttributeError, self.storage.upload, None)

    def test_upload_file(self):
        """
        Test the upload file to Google Cloud Storage

        """
        self.assertEqual(self.storage.upload(self.file), True)
        self.assertEqual(self.storage.delete(self.file.filename), True)

    def test_get_list(self):
        """
        Test the get list of files from Google Cloud Storage

        """
        self.assertEqual(self.storage.upload(self.file), True)

        data = self.storage.get()
        self.assertIsInstance(data, list)

        first_file_data = data[0]
        self.assertIsInstance(first_file_data, dict)
        self.assertEqual(first_file_data['filename'], '/' + self.file.filename)

        self.assertEqual(self.storage.delete(self.file.filename), True)

    def test_get_invalid_file(self):
        """
        Test if the function get raise an error to a invalid filename

        """
        self.assertRaises(FileNotFoundError, self.storage.get, 'invalid')

    def test_get_file(self):
        """
        Test the get file data from Google Cloud Storage

        """
        self.assertEqual(self.storage.upload(self.file), True)

        data = self.storage.get(self.file.filename)
        self.assertIsInstance(data, dict)
        self.assertEqual('/' + self.file.filename, data['filename'])

        self.assertEqual(self.storage.delete(self.file.filename), True)

    def test_delete_invalid_file(self):
        """
        Test if the function delete raise an error to a invalid filename

        """
        self.assertRaises(FileNotFoundError, self.storage.delete, 'invalid')

    def test_delete_file(self):
        """
        Test if the file was deleted from Google Cloud Storage

        """
        self.assertEqual(self.storage.upload(self.file), True)
        self.assertEqual(self.storage.delete(self.file.filename), True)
        self.assertRaises(FileNotFoundError,
                          self.storage.get, self.file.filename)
