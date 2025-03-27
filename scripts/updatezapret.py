import requests
import subprocess
from pathlib import Path
import json
import os

current_file = Path(__file__).resolve()
config_path = current_file.parent / "settings.json"
fixed_config_path = str(config_path).replace(r'\\', '/')
with open(fixed_config_path, 'r', encoding='utf-8') as cfgfile:
    config = json.load(cfgfile)
pathtozapret = config['pathtozapret']

if pathtozapret != "":
    files = ['list-general.txt', 'list-discord.txt', 'ipset-discord.txt']
    examplegithub = 'https://raw.githubusercontent.com/Flowseal/zapret-discord-youtube/main/'
    url_listdiscord = '{}{}'.format(examplegithub, files[1])
    url_listgeneral = '{}{}'.format(examplegithub, files[0])
    url_ipsetdiscord = '{}{}'.format(examplegithub, files[2])
    response = requests.get(url_listdiscord)
    if response.status_code == 200:
        content = response.text
        listdiscord = open(os.path.join(pathtozapret, 'list-discord.txt'), 'w+')
        listdiscord.write(content)
    else:
        print("Ошибка при загрузке файла")

    response = requests.get(url_ipsetdiscord)
    if response.status_code == 200:
        content = response.text
        listdiscord = open(os.path.join(pathtozapret, 'ipset-discord.txt'), 'w+')
        listdiscord.write(content)
    else:
        print("Ошибка при загрузке файла")

    response = requests.get(url_listgeneral)
    if response.status_code == 200:
        content = response.text
        listdiscord = open(os.path.join(pathtozapret, 'list-general.txt'), 'w+')
        listdiscord.write(content)
    else:
        print("Ошибка при загрузке файла")

    bat_file_path = os.path.join(pathtozapret, 'general.bat')

    try:
        subprocess.run(bat_file_path, shell=True, check=True)
        print(".bat файл успешно запущен!")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при запуске .bat файла: {e}")
else:
    print("Путь к ZapretDiscordYoutube пуст...")

