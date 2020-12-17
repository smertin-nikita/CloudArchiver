import os

import requests
import os.path as op
import os


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def create_folder(self, name):
        try:
            response = requests.put(
                url='https://cloud-api.yandex.net/v1/disk/resources',
                params={
                    'path': name,
                    'overwrite': 'true'
                },
                headers={'Authorization': 'OAuth ' + self.token}
            )
            response.raise_for_status()
        except requests.RequestException as e:
            if e.response.status_code == 409:
                self.create_folder('VkPhotos')
            print(e.response.status_code)
            return False

        return True

    def upload_by_url(self, file_url, path='download'):

        if not self.create_folder('VkPhotos'):
            return False

        try:
            response = requests.post(
                url='https://cloud-api.yandex.net/v1/disk/resources/upload',
                params={
                    'path': path,
                    'url': file_url,
                    'overwrite': 'true'
                },
                headers={'Authorization': 'OAuth ' + self.token}
            )
            response.raise_for_status()
        except requests.RequestException as e:
            print(e.response.status_code)
            return False

        return True

    def upload_from_path(self, file_path):
        """Метод загруджает файл file_path на яндекс диск"""

        try:
            response = requests.get(
                url='https://cloud-api.yandex.net/v1/disk/resources/upload',
                params={'path': op.basename(file_path), 'overwrite': 'true'},
                headers={'Authorization': 'OAuth ' + self.token}
            )
            response.raise_for_status()
        except requests.RequestException as e:
            print(e.response.status_code)
            return False

        data = response.json()
        href = data['href']

        try:
            with open(file_path, 'rb') as f:
                response = requests.put(href, files={'file': f})
                response.raise_for_status()
        except FileNotFoundError:
            print('Файл не найден')
            return False
        except requests.RequestException as e:
            print(e.response.status_code)
            return False

        return True
