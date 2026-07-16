import tkinter as tk
from tkinter import ttk
import pandas as pd
from data_loader import load_dataset_from_system
from data_preview import data_preview_left
from wrapper import *
from data_desc import *

def on_click_add_data(preview_frame: tk.Widget, data_desc_frame: tk.Widget):
    df = load_dataset_from_system()
    if df is not None:
        data_preview_left(preview_frame, data=df)
        describe_dataset(data_desc_frame, data=df)

def on_click_select(bottom_left_frame, selected_plot):
    for widget in bottom_left_frame.winfo_children():
        widget.destroy()
        
    chosen_plot = selected_plot.get()
    
    result_label = add_lable( bottom_left_frame, text=f"Selected Plot Type: {chosen_plot}")
    
    result_label.pack(padx=10, pady=10, anchor="w")

if __name__ == '__main__':
    print("this file contains code for button actions")