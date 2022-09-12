#!/usr/bin/env python
# encoding: utf-8

"""
Script: gitconfig_script.py
Auteur: PF
Date: 12/09/2022 13:18
"""

# Imports
from tkinter import *
import tkinter as tk
from re import search

# Global
file_path = 'C:\\Users\\A38579\\.gitconfig'


# Functions
def Simpletoggle():
    change_file_state()
    if toggle_button.config('text')[-1] == 'Proxy ON':
        toggle_button.config(text='Proxy OFF')
    else:
        toggle_button.config(text='Proxy ON')


def check_file_state():
    path = getTextInput()
    with open(path) as f:
        lines = f.readlines()
        for line in lines:
            if 'http' in line:
                if line.startswith('#'):
                    return False
                else:
                    return True


def change_file_state():
    path = getTextInput()
    with open(path) as f:
        lines = f.readlines()
        indexes = []
        for i, line in enumerate(lines):
            if search(r"http", line):
                indexes.append(i)

    for index in indexes:
        if lines[index].startswith('#'):
            lines[index] = lines[index].replace("#", "")
        else:
            lines[index] = "#" + lines[index]

    with open(path, 'w') as f:
        f.writelines(lines)


def getTextInput():
    return inputtxt.get()


# Main
root = tk.Tk()
root.title('Proxies for gitconfig')
root.resizable(False, False)

canvas1 = tk.Canvas(root, width=300, height=20)
canvas1.pack()

inputtxt = tk.Entry(root, width=30)

inputtxt.pack(side=tk.LEFT, padx=20, pady=10)
inputtxt.insert('end', file_path)
print(getTextInput())

if check_file_state():
    state = "Proxy ON"
else:
    state = "Proxy OFF"

toggle_button = Button(text=state, width=10, command=Simpletoggle)
toggle_button.pack(side=tk.RIGHT, padx=20, pady=10)

#canvas1.create_window(150, 150, window=toggle_button)

root.mainloop()


def main():
    pass


if __name__ == '__main__':
    main()
