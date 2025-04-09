from tkinter import ttk
import tkinter as tk
from tkinter import filedialog
from tkinter.messagebox import showinfo, showwarning, showerror
from pathlib import Path
import json

root = tk.Tk()
# def addmod():
#     current_file = Path(__file__).resolve()
#     pathtoscripts = Path(current_file.parent) / 'scripts.json'
#     f = open(pathtoscripts)
#     configraw = f.read()
#     config = json.load(configraw)
#     config['']

def addmodfinal():
    if Path(scriptentry.get()).exists() and Path(scriptentry.get()).is_file() and modname.get() != '':
        showinfo(title="Later =3", message="In version 2.0 =3")
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
root.geometry("400x400")
entername = ttk.Label(root, text="Enter mod name")
modname = ttk.Entry()
enterscript = ttk.Label(root, text="Enter mod script")
scriptentry = ttk.Entry()
openbutton = ttk.Button(root, text="Open file", command=es)
finaladd = ttk.Button(root, text="Add mod!", command=addmodfinal)
entername.pack()
modname.pack()
enterscript.pack()
scriptentry.pack()
openbutton.pack()
finaladd.pack()
root.mainloop()