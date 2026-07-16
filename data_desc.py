import tkinter as tk
from tkinter import ttk
import pandas as pd
from wrapper import *

def describe_dataset(dataset_desc_frame: tk.Widget, data: pd.DataFrame):
    # 1. Clear previous widgets
    for widget in dataset_desc_frame.winfo_children():
        widget.destroy()

    if data is None or data.empty:
        return

    columns = list(data.columns)
    col_var = tk.StringVar(value=columns[0])

    for i in range(4):
        dataset_desc_frame.grid_columnconfigure(i, weight=1)

    col_label = add_lable(dataset_desc_frame, text='Column count:')
    col_count = add_lable(dataset_desc_frame, text=str(data.shape[1]))  

    row_label = add_lable(dataset_desc_frame, text='Row count:')
    row_count = add_lable(dataset_desc_frame, text=str(data.shape[0]))  

    col_label.grid(row=0, column=0, sticky="ew", padx=10, pady=5)
    col_count.grid(row=0, column=1, sticky="ew", padx=10, pady=5)
    row_label.grid(row=0, column=2, sticky="ew", padx=10, pady=5)
    row_count.grid(row=0, column=3, sticky="ew", padx=10, pady=5)

    filter_label = add_lable(dataset_desc_frame, text='Select Column:')
    filter_cb = add_combobox(dataset_desc_frame, values=columns, textvariable=col_var)

    filter_label.grid(row=1, column=0, sticky="ew", padx=(10, 2), pady=5)
    filter_cb.grid(row=1, column=1, columnspan=3, sticky="ew", padx=(2, 10), pady=5)

    dtype_label = add_lable(dataset_desc_frame, text='Data type:')
    initial_dtype = str(data[columns[0]].dtype) 
    dtype_entry = add_entry(dataset_desc_frame, text=initial_dtype)

    dtype_label.grid(row=2, column=0, sticky="ew", padx=(10, 2), pady=5)
    dtype_entry.grid(row=2, column=1, columnspan=3, sticky="ew", padx=(2, 10), pady=5)

    na_count_label_text = add_lable(dataset_desc_frame, text='N/A Count:')
    na_count_label = add_lable(dataset_desc_frame, text="0")

    na_percent_label_text = add_lable(dataset_desc_frame, text='N/A Percent:')
    na_percent_label = add_lable(dataset_desc_frame, text="0%")

    na_count_label_text.grid(row=3, column=0, sticky="ew", padx=10, pady=5)
    na_count_label.grid(row=3, column=1, sticky="ew", padx=10, pady=5)
    na_percent_label_text.grid(row=3, column=2, sticky="ew", padx=10, pady=5)
    na_percent_label.grid(row=3, column=3, sticky="ew", padx=10, pady=5)

    def update_column_info(*args):
        selected_col = col_var.get()
        if not selected_col or selected_col not in data.columns:
            return

        new_dtype = str(data[selected_col].dtype)
        dtype_entry.config(state='normal')
        dtype_entry.delete(0, tk.END)
        dtype_entry.insert(0, new_dtype)
        dtype_entry.config(state='readonly') 

        na_count = data[selected_col].isna().sum()
        na_percentage = (na_count / len(data)) * 100
        
        na_count_label.config(text=na_count)
        na_percent_label.config(text=f"{na_percentage:.2f}%")

    filter_cb.bind("<<ComboboxSelected>>", update_column_info)
    
    update_column_info()