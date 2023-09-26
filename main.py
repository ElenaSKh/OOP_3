# Задача 1
print('Задача 1, супергерои')

import json
from pprint import pprint
import requests
url = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"
respons = requests.get(url)
data = respons.json()
name = ['Hulk', 'Captain America', 'Thanos']#, 'A-Bomb', 'Agent Zero', 'Agent Bob']
heros = []
for ii in name:
    for item in data:
        if item['name'] == ii:
            heros.append({'name': ii, 'intelligence': item['powerstats']['intelligence']})
super_heros = sorted(heros, key=lambda name: name['intelligence'])
super_hero = super_heros[-1]
pprint(super_heros)
print('**************')
print(f"Самый умный {super_hero['name']}, интеллект: {super_hero['intelligence']}")


# Задача 2
print('Задача 2, Яндекс.Диск')

import os

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        # Тут ваша логика
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        params = {"path": file_path}
        headers = {"Authorization": token}
        response = requests.put(url, headers=headers, params=params)
        url = url + '/upload'
        print(url)
        file_in_dir = os.listdir(file_path)
        for file_i in file_in_dir:
            # собираем ссылку в полный путь к файлам
            file_full_path = file_path + '/' + file_i
            params = {"path": file_full_path}
            resp = requests.get(url, headers=headers, params=params)
            url_for_upload = resp.json().get('href', '')
            print(file_full_path)
            with open(file_full_path, 'rb') as file:
                response2 = requests.put(url_for_upload, files={"file": file})
            print(f'файл {url_for_upload} \n загружен!')
        # Функция может ничего не возвращать

if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    token = ''
    path_to_file = 'for_test'
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)