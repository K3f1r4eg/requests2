from pprint import pprint

import requests

from ya_disk import YaUploader

TOKEN = ""


if __name__ == '__main__':
    ya = YaUploader(token=TOKEN)
    ya.upload_file('RF/Russia_file.txt','Russia.txt')