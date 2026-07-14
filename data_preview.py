import tkinter as tk
from tkinter import ttk
import pandas as pd

def data_preview_left(frame: tk.Widget, data: pd.DataFrame):
    for widget in frame.winfo_children():
        widget.destroy()

    if data is None or data.empty:
        return

    columns = list(data.columns)
    tree = ttk.Treeview(frame, columns=columns, show="headings", height=15)

    #Define the column headings and properties
    for col in columns:
        tree.heading(col, text=str(col))
        tree.column(col, width=80, anchor=tk.CENTER)

    #Insert the rows from data.head(5)
    for index, row in data.head(5).iterrows():
        tree.insert("", tk.END, values=[str(val) for val in row])

    # Insert a visual separator row to indicate skipped data
    if len(data) > 10:
        tree.insert("", tk.END, values=["..." for _ in columns])   
        for index, row in data.tail(5).iterrows():      # Insert the rows from data.tail(5)
            tree.insert("", tk.END, values=[str(val) for val in row])
    #If dataset has between 6 and 10 rows, just show the remaining rows       
    elif len(data) > 5:
        for index, row in data.iloc[5:].iterrows():
            tree.insert("", tk.END, values=[str(val) for val in row])

    #Add horizontal and vertical scrollbars
    v_scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tree.yview)
    h_scrollbar = ttk.Scrollbar(frame, orient=tk.HORIZONTAL, command=tree.xview)
    tree.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)

    #Pack the table and scrollbars into the partition
    v_scrollbar.pack(fill=tk.Y, side=tk.RIGHT)
    h_scrollbar.pack(fill=tk.X, side=tk.BOTTOM)
    tree.pack(fill=tk.BOTH, expand=True, padx=5, pady=5, side=tk.LEFT)