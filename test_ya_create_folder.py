import requests
from unittest import TestCase


class YandexDisk:
    BASE_URL = 'https://cloud-api.yandex.net/'

    def __init__(self, token):
        self.token = token

    def _get_common_headers(self):
        return {
            'Authorization': self.token
        }

    def create_folder(self, name):
        headers = self._get_common_headers()
        params = {
            'path': name
        }
        response = requests.put(f'{self.BASE_URL}v1/disk/resources',
                                headers=headers, params=params)
        return response.status_code


TOKEN = 'sectet'


class CreateFolder(TestCase):

    def test_folder(self):
        yandex = YandexDisk(TOKEN)
        first_status_code = 201
        result = yandex.create_folder('folder')
        self.assertEqual(result, first_status_code)

    def test_token(self):
        status_code = 401
        fake_token = TOKEN + 'asdf'
        yandex = YandexDisk(fake_token)
        result = yandex.create_folder('new_folder')
        self.assertEqual(result, status_code)

    def test_repeat_create_folder(self):
        yandex = YandexDisk(TOKEN)
        first_status_code = 409
        result = yandex.create_folder('folder')
        self.assertEqual(result, first_status_code)

    

