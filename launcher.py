import tkinter as tk
from tkinter import ttk
import subprocess
safe_globals = {"__builtins__": None}
safe_locals = {}
class betterbutton:

    name = ''
    script = ''
    file = ''
    btn = None
    def __init__(self):
        global name
        global btn
        btn = ttk.Button(text=name, command=self.runscript)
    def runscript(self):
        global file
        code = open(file, 'r')
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







