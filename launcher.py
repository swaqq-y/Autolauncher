import tkinter as tk
from tkinter import ttk
import subprocess
safe_globals = {"__builtins__": None}
safe_locals = {}
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


buttonslist = ['Repair BetterDiscord', 'Update ZapretDiscordYoutube']
#buttonslist = ['Repair BetterDiscord', 'Update ZapretDiscordYoutube', 'Download BetterDiscord Plugins', 'Download BetterDiscord Themes']
buttonsway = {'Repair BetterDiscord':'./scripts/repair_betterdiscord.py', 'Update ZapretDiscordYoutube':'./scripts/updatezapret.py'}
listbutton = []

for button in buttonslist:
    bttn = betterbutton(name=button, script=buttonsway[button])
    bttn.btn.pack()





root.mainloop()







