"""
Test the Storage class

"""
from unittest import TestCase
from api.resources.storage import Storage


class TestStorage(TestCase):
    """
    Test the Storage class

    """

    def setUp(self):
        """
        Create the storage instance

        """
        self.storage = Storage()

    def test_upload(self):
        """
        Test if the upload function raise not implemented yet

        """
        self.assertRaises(NotImplementedError, self.storage.upload, None)

    def test_get(self):
        """
        Test if the get function raise not implemented yet

        """
        self.assertRaises(NotImplementedError, self.storage.get, None)

    def test_delete(self):
        """
        Test if the delete function raise not implemented yet

        """
        self.assertRaises(NotImplementedError, self.storage.delete, None)
