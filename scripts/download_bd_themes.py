import requests
import json
from pathlib import Path
import os
from tkinter.messagebox import showwarning
current_file = Path(__file__).resolve()
config_path = current_file.parent / "settings.json"
filepath = current_file.parent / "themes.txt"

with open(config_path, 'r', encoding='utf-8') as cfgfile:
    config = json.load(cfgfile)

betterdiscord_path = Path(config['betterdiscordpath'])
themespath = betterdiscord_path / "themes"
plugins = []
tmp = ''
count =0
count += int(config['lasttheme'])
if betterdiscord_path != '':
    if betterdiscord_path.exists() and os.path.getsize(filepath) > 0:
        with open(filepath, 'r') as pluginsfile:
            for letter in pluginsfile.read():
                if letter != ';':
                    tmp += letter
                else:
                    plugins.append(tmp.strip())
                    tmp = ''

        os.makedirs(themespath, exist_ok=True)

        for i in plugins:
            response = requests.get(i)
            theme_name = i.split('/')[-1].split('?')[0] + '{}.theme.css'.format(count)
            pathfortheme = themespath / theme_name
            count += 1
            if response.status_code == 200:
                with open(pathfortheme, 'wb') as f:
                    f.write(response.content)
                    print(f'Тема {theme_name} скачана!')
        config["lasttheme"] = str(count)
        with open(config_path, 'w', encoding='utf-8') as file:
            json.dump(config, file, ensure_ascii=False, indent=4)
    else:
        showwarning(title='Warning', message='Path to BetterDiscord is empty!')