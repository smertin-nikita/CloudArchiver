from pprint import pprint

import requests

from VkRequester import VkUser, VkPhoto
from YaUploader import YaUploader
from config import CONFIG


def get_url_for_token():
    return requests.get(
        url='https://oauth.vk.com/authorize',
        params={
            'client_id': CONFIG['app_id'],
            'display': 'page',
            'redirect_uri': 'https://oauth.vk.com/blank.html',
            'scope': CONFIG['scope'],
            'response_type': 'token',
            'v': CONFIG['v']
        }
    ).url


user = VkUser(token=CONFIG['vk']['token'])
photos = user.get_photos()
photos = map(VkPhoto.get_by_size, photos)
uploader = YaUploader(token=CONFIG['yandex']['token'])
for photo in photos:
    uploader.upload(photo['url'])
