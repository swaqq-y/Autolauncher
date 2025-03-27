import requests
import os
import subprocess


betterdiscord_url = "https://github.com/BetterDiscord/Installer/releases/latest/download/BetterDiscord-Windows.exe"
installer_path = os.path.join(os.getenv("TEMP"), "BetterDiscord-Windows.exe")


response = requests.get(betterdiscord_url)
if response.status_code == 200:
    with open(installer_path, "wb") as f:
        f.write(response.content)
        print("BetterDiscord скачан!")

try:
    subprocess.run(installer_path, shell=True, check=True)
    print(".bat файл успешно запущен!")
except subprocess.CalledProcessError as e:
    print(f"Ошибка при запуске .bat файла: {e}")