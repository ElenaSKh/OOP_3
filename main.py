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

import requests
import os

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        # Тут ваша логика
        # Функция может ничего не возвращать
        url = 'https://cloud-api.yandex.net:443/v1/disk/resources/upload'
        headers = {'Authorization': 'OAuth ' +self.token}
        params = {'path': '/superheroes.jpg'}
        data = requests.get(url, headers=headers, params=params).json()
        url = data['href']
        with open(file_path, 'rb') as f:
            response = requests.put(url, files={'file': f}, headers=headers, params=params)
        return response.status_code

if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = "C:\\Education\\PycharmProjects\\OOP3\\superheroes-0.jpg"
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)