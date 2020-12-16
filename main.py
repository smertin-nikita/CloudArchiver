from VkRequester import VkUser
from YaUploader import YaUploader
from config import CONFIG

user = VkUser(token=CONFIG['vk']['token'])
uploader = YaUploader(token=CONFIG['yandex']['token'])
