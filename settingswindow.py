from tkinter import ttk
import json

settingsfile = open('settings.json')
settings_json = settingsfile.read()
settings = json.loads(settings_json)
waytozapret = ttk.Entry()
waytozapret.pack()
