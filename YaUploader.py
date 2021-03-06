import os

import requests
import os.path as op
import os


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path=None, file_url=None):
        """Метод загруджает файл file_path на яндекс диск"""

        if file_path:
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
        elif file_url:
            try:
                response = requests.post(
                    url='https://cloud-api.yandex.net/v1/disk/resources/upload',
                    params={
                        'path': op.join(os.getcwd(), 'photos/'),
                        'url': file_url,
                        'overwrite': 'true'},
                    headers={'Authorization': 'OAuth ' + self.token}
                )
                response.raise_for_status()
            except requests.RequestException as e:
                print(e.response.status_code)
                return False
        else:
            return False

        data = response.json()
        href = data['href']

        try:
            with open(file_path, 'rb') as f:
                response = requests.put(href, files={'file': f})
                response.raise_for_status()
                return True
        except FileNotFoundError:
            print('Файл не найден')
            return False
        except requests.RequestException as e:
            print(e.response.status_code)
            return False
