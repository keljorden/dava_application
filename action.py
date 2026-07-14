import tkinter as tk
from tkinter import ttk
import pandas as pd
from data_loader import load_dataset_from_system
from data_preview import data_preview_left
from layout import *

def on_click_add_data(preview_frame):
    df = load_dataset_from_system()
    if df is not None:
        data_preview_left(preview_frame, data=df)

if __name__ == '__main__':
    print("this file contains code for button actions")