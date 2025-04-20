import requests
import json
from pathlib import Path
from tkinter.messagebox import showinfo
import zipfile
import os

config_path = Path(__file__).parent / 'settings.json'
icon_path = Path(__file__).parent / 'icon.ico'

config = json.load(open(config_path))
updatename = config['updatename']
response = requests.get('https://raw.githubusercontent.com/swaqq-y/Autolauncher/{}/settings.json'.format(updatename))



githubconfig = json.loads(response.text)
currentfile = Path(__file__).resolve()


#if githubconfig['version'] != config['version']:
scriptsfiles = os.listdir('./')
with zipfile.ZipFile("backup.zip", "w") as zf:
    zf.write(currentfile.parent / "themes.txt")
    zf.write(currentfile.parent / 'plugins.txt')
    zf.write(currentfile.parent / 'settings.json')
    zf.write(currentfile.parent / 'scripts.json')
    zf.write(currentfile.parent / 'scripts/')
    for i in scriptsfiles:
        zf.write(currentfile.parent / 'scripts' / i)



    # config["version"] = githubconfig['version']
    # with open(config_path, 'w', encoding='utf-8') as file:
    #     json.dump(config, file, ensure_ascii=False, indent=4)


#     showinfo('AutoLauncher Updates', 'AutoLaucher Updates are installed.')
# else:
#     showinfo('AutoLauncher Updates', 'Everything is up to date.')
