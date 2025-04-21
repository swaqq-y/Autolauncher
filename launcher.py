import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
import subprocess
import sys
from pathlib import Path
import json

root = tk.Tk()
root.iconbitmap("./icon.ico")
root.title("AutoLauncher")
root.geometry('600x400')
root.title('AutoLauncher')
pathtoconfig = Path('./settings.json')
with open(pathtoconfig) as f:
    config = json.load(f)
class betterbutton:
    def __init__(self, name="", script=""):
        self.name = name
        self.script = script
        self.btn = ttk.Button(text=self.name, command=self.runscript)
    def runscript(self):
        if self.script != '':
            file = open(self.script, 'r')
            code = file.read()
            exec(code)
        else:
            tkinter.messagebox.showerror(title='Critical Error', message='Script file does not exist...')


def opensettings():
    subprocess.run([sys.executable, "settingswindow.py"])
def openaddmod():
    subprocess.run([sys.executable, "addscript.py"])
buttonslist = ['Repair BetterDiscord', 'Update ZapretDiscordYoutube', 'Download BetterDiscord Plugins', 'Download BetterDiscord Themes', "Check AutoLaucher Updates"]
buttonsway = {'Repair BetterDiscord':'./scripts/repair_betterdiscord.py', 'Update ZapretDiscordYoutube':'./scripts/updatezapret.py', 'Download BetterDiscord Plugins':'./scripts/download_bd_plugins.py', 'Download BetterDiscord Themes':'./scripts/download_bd_themes.py', 'Check AutoLaucher Updates' : './checkupdates.py'}
listbutton = []

pathtoscripts = Path('./scripts.json')
try:
    if pathtoscripts.is_file() and pathtoscripts.exists():
        with open(pathtoscripts) as f:
            scripts = json.load(f)
        if scripts != {}:
            lasti = 0
            lastscript = int(config['lastscript'])
            lastscript += 1
            for i in range(lastscript):
                if i == 0:
                    i += 1
                if lasti == i:
                    i += 1
                    continue
                buttonslist.append(scripts["script" + str(i)]['name'])
                buttonsway[scripts["script" + str(i)]['name']] = scripts["script" + str(i)]['scriptname']
                lasti = i

        for button in buttonslist:
            bttn = betterbutton(name=button, script=buttonsway[button])
            bttn.btn.pack()

except KeyError:
    lastscript = int(config['lastscript'])
    config['lastscript'] = str(lastscript - 1)
    with open("./settings.json", 'w', encoding='utf-8') as file:
        json.dump(config, file, ensure_ascii=False, indent=4)
    tkinter.messagebox.showerror(title='Critical Error!', message='Critical Error (101):\n In the settings.json file,\n the lastscript value is greater than\n the number of scripts in scripts.json. \n We are trying to fix this, please try to restart this app.')

settings = ttk.Button(text="Settings", command=opensettings)
settings.pack(anchor="s")
addascript = ttk.Button(text="Add a script", command=openaddmod)
addascript.pack(anchor=tk.S)


root.mainloop()







