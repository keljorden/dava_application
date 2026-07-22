import tkinter as tk
from tkinter import ttk

# split windows vertically or horizontally 
def split_window(root, dir: str = 'HORIZONTAL'):
    if dir == 'HORIZONTAL':
        split = ttk.PanedWindow(root, orient= tk.HORIZONTAL)
    elif dir == 'VERTICAL':
        split = ttk.PanedWindow(root, orient= tk.VERTICAL)
    else: return 'Unsupported split attempted'
    return split

# create frame to add to the window
def create_frame(window, **kwargs):
    new_frame = ttk.Frame(window, **kwargs)
    return new_frame

# add frame to the parent window/frame
def add_frame(parent_frame, child_frame, w: int = 1, **kwargs):
    parent_frame.add(child_frame, weight= w, **kwargs)


def add_lable(frame, text: str, font =("Arial", 10, "bold"), **kwargs):
    lbl = ttk.Label(frame, text = text, font = font, **kwargs)
    return lbl

def add_button(frame, text: str, command = None, padx = 10, pady = 10, **kwargs):
    kwargs.setdefault("cursor", "hand2")
    btn = ttk.Button(frame, text = text, command = command, **kwargs)
    return btn

def add_combobox(frame, values: list, textvariable: str, **kwargs):
    kwargs.setdefault("state", "readonly")
    cb = ttk.Combobox(frame, values=values, textvariable = textvariable, **kwargs)
    return cb

def add_entry(frame, text: str):
    var = tk.StringVar(value=text)
    entry = ttk.Entry(frame, textvariable=var, state='readonly')
    return entry