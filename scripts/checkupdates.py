import requests
import json
from pathlib import Path
import tkinter as tk
from tkinter.messagebox import showinfo
def get_github_repo_files():
    url = f"https://api.github.com/repos/swaqq-y/Autolauncher/contents/"
    headers = {
        'Accept': 'application/vnd.github.v3+json'
    }
response = requests.get('https://raw.githubusercontent.com/swaqq-y/Autolauncher/main/settings.json')

config_path = Path(__file__).parent / 'settings.json'
icon_path = Path(__file__).parent / 'icon.ico'

githubconfig = json.loads(response.text)

config = json.load(open(config_path))

if githubconfig['version'] != config['version']:
    config["version"] = githubconfig['version']
    with open(config_path, 'w', encoding='utf-8') as file:
        json.dump(config, file, ensure_ascii=False, indent=4)

    showinfo('AutoLaucher Updates', 'AutoLaucher Updates are installed.')
else:
    showinfo('AutoLaucher Updates', 'Everything is up to date.')
