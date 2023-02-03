import tkinter as tk
import pymongo

from os.path import exists
from tkinter import *

window = tk.Tk()
window.geometry('600x500')
window.title("Database handler")
window.config(padx=10, pady=10, bg='#FFD700')

f = Frame(window)

xscrollbar = Scrollbar(f, orient=HORIZONTAL)
xscrollbar.grid(row=1, column=0, sticky=N+S+E+W)

yscrollbar = Scrollbar(f)
yscrollbar.grid(row=0, column=1, sticky=N+S+E+W)

text = Text(f, wrap=NONE,
            xscrollcommand=xscrollbar.set,
            yscrollcommand=yscrollbar.set)
text.grid(row=0, column=0)

xscrollbar.config(command=text.xview)
yscrollbar.config(command=text.yview)

title_label = tk.Label(window, text="Database handler", bg='#FFD700')
title_label.config(font=("Lobster", 34))
title_label.pack(padx=10, pady=10)

def create_collection():
    name = inputtxt.get(1.0, "end-1c")
    try:
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["mydatabase"]
        mycollection = mydb[f"{name}"]
        if exists("collections names.txt"):
            with open('collections names.txt', 'w') as f:
                f.write(f'{name}')
        else:
            f = open("collections names.txt", "w+")
            f.write(f"{name}")

    except Exception as error:
        old_label_names.config(text="A error has happened.")

def find_all():
    try:
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["mydatabase"]
        f = open("collections names.txt", "r")
        mycollection = mydb[f"{f.read()}"]
        for x in mycollection.find().sort("name"):
            old_label_names.config(text=f"{x}")

    except Exception as error:
        old_label_names.config(text="A error has happened.")

def deltee():
    delete = deltetxt.get(1.0, "end-1c")
    try:
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["mydatabase"]
        f = open("collections names.txt", "r")
        mycollection = mydb[f"{f.read()}"]
        myquery = {"address": f"{delete}"}
        mycollection.delete_one(myquery)
    except Exception as error:
        old_label_names.config(text="A error has happened.")

inputtxt = tk.Text(window,
                   height = 2,
                   width = 20,
                   fg='red')
inputtxt.pack()

deltetxt = tk.Text(window,
                   height = 2,
                   width = 20,
                   fg='red')
deltetxt.pack()

old_label_names = tk.Label(window, text='', wraplength=1200, justify="left", bg='#FFD700')
old_label_names.pack(padx=10, pady=10)

# Button Creation
printButton = tk.Button(window,
                        text = "Create",
                        command = create_collection,
                        bg='#4a7abc',
                        fg='black',
                        activebackground='green',
                        activeforeground='white',)
printButton.pack()

findbutton = tk.Button(window,
    text="Find",
    command=find_all,
    bg='#4a7abc',
    fg='black',
    activebackground='green',
    activeforeground='white',)
findbutton.pack()

deltebutton = tk.Button(window,
    text="Delete",
    command=deltee,
    bg='#4a7abc',
    fg='black',
    activebackground='green',
    activeforeground='white',)
deltebutton.pack()

checks_names = tk.Label(window, text='First box is to create and second is to delete', wraplength=1200, justify="left", bg='#FFD700')
checks_names.pack(padx=10, pady=10)

window.mainloop()
