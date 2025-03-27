import tkinter as tk
from tkinter import ttk
import threading
from corescripts.scripts import repair_betterdiscord
import subprocess
safe_globals = {"__builtins__": None}  # Запрещаем встроенные функции (open, eval и т. д.)
safe_locals = {}
class betterbutton:
    name = ''
    script = ''
    code = open('./corescripts/scripts/repair_betterdiscord.py', 'r')
    def runscript(self):
        global code
        exec(code, safe_globals, safe_locals)


buttonslist = ['Repair BetterDiscord', 'Update ZapretDiscordYoutube', 'Download BetterDiscord Plugins', 'Download BetterDiscord Themes']
listbutton = []


# Создание интерфейса
root = tk.Tk()
root.title("AutoLauncher")
root.geometry('600x400')
root.title('AutoLauncher')

for i in buttonslist:
    if i == buttonslist[1]:
        commanda = subprocess.run()
    listbutton.append(ttk.Button(text=i, ))



root.mainloop()







