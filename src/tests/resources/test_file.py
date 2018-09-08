"""
Test the File Recourse

"""
import io
import json
from unittest import TestCase
from api.app import APP


class TestFileAPI(TestCase):
    """
    Test the File Recourse

    """

    def setUp(self):
        """
        Set up test

        """
        self.client = APP.test_client()

    def test_upload(self):
        """
        Test the upload file

        """
        data = {'file': (io.BytesIO(b"dummy"), 'dummy')}
        resp = self.client.post('/file', data=data)
        self.assertEqual(resp.status_code, 200)

        data = json.loads(resp.data)
        self.assertEqual(data['filename'], 'dummy')
        self.assertEqual(data['message'], 'The file was uploaded with success')

        resp = self.client.delete('/file/dummy')
        self.assertEqual(resp.status_code, 200)

    def test_get_empty_list(self):
        """
        Test to get the empty list

        """
        resp = self.client.get('/file')
        self.assertEqual(resp.status_code, 200)

        data = json.loads(resp.data)
        self.assertEqual(len(data), 0)

    def test_get_list(self):
        """
        Test to get the list of files

        """
        data = {'file': (io.BytesIO(b"dummy"), 'dummy')}
        resp = self.client.post('/file', data=data)
        self.assertEqual(resp.status_code, 200)

        resp = self.client.get('/file')
        data = json.loads(resp.data)
        self.assertEqual(len(data), 1)

        first_file_data = data[0]
        self.assertEqual(first_file_data['filename'], '/dummy')

        resp = self.client.delete('/file/dummy')
        self.assertEqual(resp.status_code, 200)

    def test_get_invalid_file(self):
        """
        Test to get a invalid file

        """
        resp = self.client.get('/file/dummy')
        self.assertEqual(resp.status_code, 404)

    def test_get_file(self):
        """
        Test  to get a specific file

        """
        data = {'file': (io.BytesIO(b"dummy"), 'dummy')}
        resp = self.client.post('/file', data=data)
        self.assertEqual(resp.status_code, 200)

        resp = self.client.get('/file/dummy')
        self.assertEqual(resp.status_code, 200)

        data = json.loads(resp.data)
        self.assertEqual(data['filename'], '/dummy')

        resp = self.client.delete('/file/dummy')
        self.assertEqual(resp.status_code, 200)

    def test_delete_invalid_file(self):
        """
        Test to delete a invalid file

        """
        resp = self.client.delete('/file/dummy')
        self.assertEqual(resp.status_code, 404)

    def test_delete_file(self):
        """
        Test to delete a file

        """
        data = {'file': (io.BytesIO(b"dummy"), 'dummy')}
        resp = self.client.post('/file', data=data)
        self.assertEqual(resp.status_code, 200)

        resp = self.client.delete('/file/dummy')
        self.assertEqual(resp.status_code, 200)

        data = json.loads(resp.data)
        self.assertEqual(data['filename'], 'dummy')
        self.assertEqual(data['message'], 'The file was deleted with success')
