import tkinter.messagebox
from tkinter import ttk
import tkinter as tk
from tkinter import filedialog
from tkinter.messagebox import showinfo, showwarning, showerror
from pathlib import Path
import json



root = tk.Tk()
def addmod(name, scriptname):
    pathtoconfig = Path('./settings.json')
    pathtoscripts = Path('./scripts.json')
    if pathtoscripts.exists() and pathtoconfig.exists():
        with open("./settings.json") as f:
            config = json.load(f)
        with open("./scripts.json") as f:
            scripts = json.load(f)
        lastscript = int(config['lastscript']) + 1
        config['lastscript'] = str(lastscript)
        scripts['script' + str(lastscript)] = {'name': name, 'scriptname': scriptname}

        with open("./settings.json", 'w', encoding='utf-8') as file:
            json.dump(config, file, ensure_ascii=False, indent=4)
        with open("./scripts.json", 'w', encoding='utf-8') as file:
            json.dump(scripts, file, ensure_ascii=False, indent=4)
        showinfo(title='Success!', message='Done!')
    else:
        showerror(title='Critical Error', message='settings.json or scripts.json files does not exist...')



def addmodfinal():
    if Path(scriptentry.get()).exists() and Path(scriptentry.get()).is_file() and modname.get() != '':
        addmod(modname.get(), scriptentry.get())
        showinfo(title="Success", message="Done!")
    elif Path(scriptentry.get()).exists() and Path(scriptentry.get()).is_file() and modname.get() == '':
        showwarning(title='Warning', message='Name entry is empty.')
    elif not Path(scriptentry.get()).exists() and not Path(scriptentry.get()).is_file() and modname.get() != '':
        showerror(title="Error", message='Path to script is not a file or does not exist.')
    else:
        showerror(title="Error", message='Path to script is not a file or does not exist,\n and name entry is empty.')
def openfile(entry):
    filename = filedialog.askopenfilename(title="Select File", initialdir='./scripts/')
    entry.insert('end', filename)
def es():
    openfile(scriptentry)
root.iconbitmap("./icon.ico")
root.title("Add a mod")
root.geometry("400x450")
entername = ttk.Label(root, text="Enter script name")
modname = ttk.Entry()
enterscript = ttk.Label(root, text="Enter script path")
scriptentry = ttk.Entry()
openbutton = ttk.Button(root, text="Open file", command=es)
finaladd = ttk.Button(root, text="Add script!", command=addmodfinal)
entername.pack()
modname.pack()
enterscript.pack()
scriptentry.pack()
openbutton.pack()
finaladd.pack()
root.mainloop()