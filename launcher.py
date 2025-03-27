import tkinter as tk
from tkinter import ttk
import subprocess
import sys
import os

root = tk.Tk()
root.title("AutoLauncher")
root.geometry('600x400')
root.title('AutoLauncher')
class betterbutton:
    def __init__(self, name="", script=""):
        self.name = name
        self.script = script
        self.btn = ttk.Button(text=self.name, command=self.runscript)
    def runscript(self):
        file = open(self.script, 'r')
        code = file.read()
        exec(code)


def opensettings():
    subprocess.run([sys.executable, "settingswindow.py"])

buttonslist = ['Repair BetterDiscord', 'Update ZapretDiscordYoutube', 'Download BetterDiscord Plugins', 'Download BetterDiscord Themes']
buttonsway = {'Repair BetterDiscord':'./scripts/repair_betterdiscord.py', 'Update ZapretDiscordYoutube':'./scripts/updatezapret.py', 'Download BetterDiscord Plugins':'./scripts/download_bd_plugins.py', 'Download BetterDiscord Themes':'./scripts/download_bd_themes.py'}
listbutton = []

for button in buttonslist:
    bttn = betterbutton(name=button, script=buttonsway[button])
    bttn.btn.pack()


settings = ttk.Button(text="Settings", command=opensettings)
settings.pack(anchor="s")



root.mainloop()







