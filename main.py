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