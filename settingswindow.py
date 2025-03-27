from tkinter import ttk
import tkinter as tk
import json
from tkinter.messagebox import showinfo

root = tk.Tk()
root.title('Settings')
root.iconbitmap("./icon.ico")
root.geometry('300x200')
settingsfile = open('settings.json')
settings_json = settingsfile.read()
config = json.loads(settings_json)

zaprettext = ttk.Label(text="Enter ZapretDiscordYoutube path")
zaprettext.pack()
pathtozapret = ttk.Entry()
pathtozapret.pack()
pathtobd = ttk.Label(text="Enter BetterDiscord path")
pathtobd.pack()
pathtobetterdiscord = ttk.Entry()
pathtobetterdiscord.pack()
def info():
    showinfo(title="With love from Swaqq-y", message="Version: {}\n Thanks for downloading.\n (* ^ ω ^)".format(config["version"]))
def sucsess():
    showinfo(title="Успешно завершено", message="Успешно задано")
def setjsonzapret():
    config["pathtozapret"] = pathtozapret.get()
    with open("./settings.json", 'w', encoding='utf-8') as file:
        json.dump(config, file, ensure_ascii=False, indent=4)
    sucsess()
def setjsonbd():
    config["betterdiscordpath"] = pathtobetterdiscord.get()
    with open("./settings.json", 'w', encoding='utf-8') as file:
        json.dump(config, file, ensure_ascii=False, indent=4)
    sucsess()
zapretbtn = ttk.Button(text="Set ZapretDiscordYoutube path", command=setjsonzapret)
zapretbtn.pack()

betterdiscordbtn = ttk.Button(text="Set BetterDiscord path", command=setjsonbd)
betterdiscordbtn.pack()
labeeel = ttk.Label(text="\n")
labeeel.pack()
appinfo = ttk.Button(text="App info", command=info)
appinfo.pack()

root.mainloop()