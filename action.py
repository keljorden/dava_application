import tkinter as tk
from tkinter import ttk
import pandas as pd
from data_loader import load_dataset_from_system
from data_preview import data_preview_left
from wrapper import *
from data_desc import *
from clean_data import clean
from ploter import PlotBuilder

data_load_btn_state = {'df': None}
def on_click_add_data(preview_frame: tk.Widget, data_desc_frame: tk.Widget):
    df = load_dataset_from_system()
    if df is not None:
        data_load_btn_state['df'] = df
        data_preview_left(preview_frame, data=df)
        describe_dataset(data_desc_frame, data=df)

def on_click_select(bottom_left_frame, selected_plot, df):
    df = df
    for widget in bottom_left_frame.winfo_children():
        widget.destroy()
        
    chosen_plot = selected_plot.get()
    plt = PlotBuilder(frame = bottom_left_frame, kind = chosen_plot, data = df)
    
def on_click_clean_btn(plot_instance, clean_strategie: str, xcol: pd.Series = None, ycol: pd.Series = None):

    if xcol is not None and ycol is not None:
        plot_instance.clean_x = clean(clean_strategie, xcol)
        plot_instance.clean_y = clean(clean_strategie, ycol)

    elif ycol is None and xcol is not None:
        plot_instance.clean_x = clean(clean_strategie, xcol)
        plot_instance.clean_y = None 

    elif xcol is None and ycol is not None:
        plot_instance.clean_x = None # Reset X
        plot_instance.clean_y = clean(clean_strategie, ycol)
        
    plot_instance.update_column_info()

def on_click_download(frame: tk.Widget):
    pass

if __name__ == '__main__':
    print("this file contains code for button actions")