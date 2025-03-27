import requests
import json
from pathlib import Path
import os

current_file = Path(__file__).resolve()
config_path = current_file.parent / "settings.json"
filepath = current_file.parent / "plugins.txt"

with open(config_path, 'r', encoding='utf-8') as cfgfile:
    config = json.load(cfgfile)

betterdiscord_path = Path(config['betterdiscordpath'])
pluginspath = betterdiscord_path / "plugins"
plugins = []
tmp = ''
count =0
count += int(config["lastplugin"])
if betterdiscord_path.exists() and os.path.getsize(filepath) > 0:
    with open(filepath, 'r') as pluginsfile:
        for letter in pluginsfile.read():
            if letter != ';':
                tmp += letter
            else:
                plugins.append(tmp.strip())
                tmp = ''

    os.makedirs(pluginspath, exist_ok=True)

    for i in plugins:
        response = requests.get(i)
        plugin_name = i.split('/')[-1].split('?')[0] + '{}.plugin.js'.format(count)
        pathforplugin = pluginspath / plugin_name
        count+=1
        if response.status_code == 200:
            with open(pathforplugin, 'wb') as f:
                f.write(response.content)
                print(f'Плагин {plugin_name} скачан!')
    config["lastplugin"] = str(count)
    with open(config_path, 'w', encoding='utf-8') as file:
        json.dump(config, file, ensure_ascii=False, indent=4)
else:
    print("Файл плагинов или путь к betterdiscord пусты...")