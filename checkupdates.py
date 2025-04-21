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


if githubconfig['version'] != config['version']:
    scriptsfiles = os.listdir('./scripts/')
    with zipfile.ZipFile("backup.zip", "w") as zf:
        zf.write("./themes.txt")
        zf.write('./plugins.txt')
        zf.write('./settings.json')
        zf.write('./scripts.json')
        zf.write('./scripts/')
        for i in scriptsfiles:
            zf.write('./scripts/' + i)





    showinfo('AutoLauncher Updates', 'AutoLaucher Updates are installed.')
else:
   showinfo('AutoLauncher Updates', 'Everything is up to date.')
