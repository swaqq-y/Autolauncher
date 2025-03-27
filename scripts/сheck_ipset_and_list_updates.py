import requests
import subprocess
import json
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

parent_dir = os.path.dirname(os.path.dirname(current_dir))

config_path = os.path.join(parent_dir, "config.json")

cfgfile = open(config_path, 'r')
config = json.loads(cfgfile)
pathtozapret = config['pathtozapret']

files = ['list-general.txt', 'list-discord.txt', 'ipset-discord.txt']
examplegithub = 'https://raw.githubusercontent.com/Flowseal/zapret-discord-youtube/main/'
url_listdiscord = '{}{}'.format(examplegithub, files[1])
url_listgeneral = '{}{}'.format(examplegithub, files[0])
url_ipsetdiscord = '{}{}'.format(examplegithub, files[2])
response = requests.get(url_listdiscord)
if response.status_code == 200:
    content = response.text
    listdiscord = open('list-discord.txt', 'w+')
    listdiscord.write(content)
else:
    print("Ошибка при загрузке файла")

response = requests.get(url_ipsetdiscord)
if response.status_code == 200:
    content = response.text
    listdiscord = open('ipset-discord.txt', 'w+')
    listdiscord.write(content)
else:
    print("Ошибка при загрузке файла")

response = requests.get(url_listgeneral)
if response.status_code == 200:
    content = response.text
    listdiscord = open('list-general.txt', 'w+')
    listdiscord.write(content)
else:
    print("Ошибка при загрузке файла")

bat_file_path = 'general.bat'

try:
    subprocess.run(bat_file_path, shell=True, check=True)
    print(".bat файл успешно запущен!")
except subprocess.CalledProcessError as e:
    print(f"Ошибка при запуске .bat файла: {e}")

