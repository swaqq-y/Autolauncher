from tkinter import ttk
import json

settingsfile = open('settings.json')
settings_json = settingsfile.read()
settings = json.loads(settings_json)
pathtozapret = ttk.Entry()
pathtozapret.pack()
