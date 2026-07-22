import os
import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd

def load_dataset_from_system():
    #Open the file picker dialog with format filters
    file_path = filedialog.askopenfilename(
        title="Select a Dataset to Visualize",
        filetypes=[
            ("All Supported Files", "*.csv *.xlsx *.xls *.json *.tsv *.txt"),
            ("CSV Files", "*.csv"),
            ("Excel Spreadsheets", "*.xlsx *.xls"),
            ("JSON Files", "*.json"),
            ("Tab-Separated Files", "*.tsv *.txt"),
            ("All Files", "*.*")
        ]
    )
    
    if not file_path:
        messagebox.showwarning("Cancelled:\t","File selection cancelled by user.")
        return
        
    try:
        #Extract the file extension to pick the correct pandas reader
        file_ext = os.path.splitext(file_path)[1].lower()
        
        if file_ext == '.csv':
            df = pd.read_csv(file_path)
        elif file_ext in ['.xlsx', '.xls']:
            df = pd.read_excel(file_path)
        elif file_ext == '.json':
            df = pd.read_json(file_path)
        elif file_ext in ['.tsv', '.txt']:
            df = pd.read_csv(file_path, sep='\t')
        else:
            messagebox.showerror("Unsupported Format", f"Cannot read file type: {file_ext}")
            return None 
        #Success feedback
        messagebox.showinfo("Success", f"Loaded '{os.path.basename(file_path)}'\nRows: {df.shape[0]} | Columns: {df.shape[1]}")
        return df
        
    except Exception as e:
        #Catch corrupted files, permission errors, or missing Excel engines
        messagebox.showerror("File Load Error", f"An error occurred while reading the file:\n\n{str(e)}")
        return None
    
if __name__ == '__main__':
    df = load_dataset_from_system()
    print(df.head(5))