import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from tkinter import messagebox
import seaborn as sns
from wrapper import *

class PlotBuilder:
    _plot_map = {
        'scatter': '_ploter_relplot', 'line': '_ploter_relplot',
        'hist': '_ploter_displot',    'kde': '_ploter_displot',    'ecdf': '_ploter_displot',
        'strip': '_ploter_catplot',   'swarm': '_ploter_catplot',  'boxen': '_ploter_catplot',
        'violin': '_ploter_catplot',  'bar': '_ploter_catplot',    'point': '_ploter_catplot'
    }

    _na_strategies = [
        "1. Leave as-is (None)",      
        "2. Drop Missing (dropna)",
        "3. Fill with Zero (fillna(0))",
        "4. Forward Fill (ffill)",
        "5. Linear Interpolate"
    ]

    
    def __init__(self, frame: tk.Widget, kind: str, data=None, **kwargs):
        self.frame = frame
        self.data = data
        self.kind = kind
        self.data_cleaner_approach = tk.StringVar(value=self._na_strategies[0])

        self.clean_x = None
        self.clean_y = None
        self.clean_hue = None
        self.plt = None
        self.err = None

        self.build_ui()

        if kind not in self._plot_map:
            raise ValueError(f"Kind '{self.kind}' must be one of {list(self._plot_map.keys())}")
        
        method_name = self._plot_map[self.kind]
        plot_method = getattr(self, method_name)
        
        self.plt, self.err = plot_method(**kwargs)
        

    def update_column_info(self, event=None):
        if self.data is None:
            return
            
        x_col = self.x_var.get()
        y_col = self.y_var.get()
        hue_col = self.hue_var.get()

        if event is not None:
            self.clean_x = None
            self.clean_y = None
            self.clean_hue = None

        if x_col in self.data.columns:
            if self.clean_x is not None and self.clean_x.name == x_col:
                x_nas = self.clean_x.isna().sum()
            else:
                x_nas = self.data[x_col].isna().sum()
                
            self.x_na_entry.config(state='normal')
            self.x_na_entry.delete(0, tk.END)
            self.x_na_entry.insert(0, str(x_nas))
            self.x_na_entry.config(state='readonly')

        if y_col in self.data.columns:
            if self.clean_y is not None and self.clean_y.name == y_col:
                y_nas = self.clean_y.isna().sum()
            else:
                y_nas = self.data[y_col].isna().sum()
                
            self.y_na_entry.config(state='normal')
            self.y_na_entry.delete(0, tk.END)
            self.y_na_entry.insert(0, str(y_nas))
            self.y_na_entry.config(state='readonly')

        if hue_col and hue_col != 'None' and hue_col in self.data.columns:
            if self.clean_hue is not None and self.clean_hue.name == hue_col:
                hue_nas = self.clean_hue.isna().sum()
            else:
                hue_nas = self.data[hue_col].isna().sum()
            
            hue_val = str(hue_nas)
        else:
            hue_val = "-"  

        self.hue_na_entry.config(state='normal')
        self.hue_na_entry.delete(0, tk.END)
        self.hue_na_entry.insert(0, hue_val)
        self.hue_na_entry.config(state='readonly')


    def _ploter_relplot(self, **kwargs):
        
        try:
            x_name = self.x_var.get()
            y_name = self.y_var.get()
            hue_name = self.hue_var.get()

            if not x_name or not y_name:
                messagebox.showerror("Missing value error: ", " X or Y is not selected or mising")
                return None

            plot_x = self.clean_x if (self.clean_x is not None and self.clean_x.name == x_name) else self.data[x_name]
            plot_y = self.clean_y if (self.clean_y is not None and self.clean_y.name == y_name) else self.data[y_name]
            
            if len(plot_x) != len(plot_y):
                messagebox.showerror("Length error: ", " X and Y have different length")
                return None

            if hue_name and hue_name != 'None' and hue_name in self.data.columns:
                hue_data = self.clean_hue if (self.clean_hue is not None and self.clean_hue.name == hue_name) else self.data[hue_name]
            else:
                hue_data = None

            grid = sns.relplot(
                x=plot_x, 
                y=plot_y, 
                kind=self.kind, 
                hue=hue_data, 
                **kwargs
            )
            grid.set_axis_labels(x_name, y_name)
            return grid.fig, None

        except Exception as e:
            return None, e
        
    def _ploter_displot(self, **kwargs):
        try:
            x_name = self.x_var.get()
            hue_name = self.hue_var.get()

            if not x_name:
                messagebox.showerror("Missing value error: ", " X is not selected or mising")
                return None

            plot_x = self.clean_x if (self.clean_x is not None and self.clean_x.name == x_name) else self.data[x_name]

            if hue_name and hue_name != 'None' and hue_name in self.data.columns:
                hue_data = self.clean_hue if (self.clean_hue is not None and self.clean_hue.name == hue_name) else self.data[hue_name]
            else:
                hue_data = None
    
            grid = sns.displot(
                x=plot_x, 
                hue=hue_data, 
                kind=self.kind, 
                **kwargs
            )
            return grid.fig, None
        except Exception as e:
            return None, e

    def _ploter_catplot(self, **kwargs):
        try:
            x_name = self.x_var.get()
            y_name = self.y_var.get()
            hue_name = self.hue_var.get()

            if not x_name or not y_name:
                messagebox.showerror("Missing value error: ", " X or Y is not selected or mising")
                return None

            plot_x = self.clean_x if (self.clean_x is not None and self.clean_x.name == x_name) else self.data[x_name]
            plot_y = self.clean_y if (self.clean_y is not None and self.clean_y.name == y_name) else self.data[y_name]
            
            if len(plot_x) != len(plot_y):
                messagebox.showerror("Length error: ", " X and Y have different length")
                return None

            if hue_name and hue_name != 'None' and hue_name in self.data.columns:
                hue_data = self.clean_hue if (self.clean_hue is not None and self.clean_hue.name == hue_name) else self.data[hue_name]
            else:
                hue_data = None

            grid = sns.catplot(
                x=plot_x, 
                y=plot_y, 
                kind=self.kind, 
                hue=hue_data, 
                **kwargs
            )
            grid.set_axis_labels(x_name, y_name)
            return grid.fig, None

        except Exception as e:
            return None, e


    def build_ui(self):

        from action import on_click_clean_btn, on_click_download
            
        self.frame.grid_columnconfigure(1, weight=2)

        cols = list(self.data.columns)
        hue_choice = ['None'] + cols
        self.x_var = tk.StringVar(value=cols[0])
        self.y_var = tk.StringVar(value=cols[1] if len(cols) > 1 else cols[0])
        self.hue_var = tk.StringVar(value=hue_choice[0])

        plot_type_lable = add_lable(frame = self.frame, text = 'Plot Type:')
        plot_type = add_lable(frame = self.frame, text = f'{self.kind}' + 'plot')

        x_lable = add_lable(frame = self.frame, text = 'X-axis:')
        y_lable = add_lable(frame = self.frame, text = 'Y-axis:')

        x_combo = add_combobox(frame = self.frame, textvariable = self.x_var, values = cols)
        y_combo = add_combobox(frame = self.frame, textvariable = self.y_var, values = cols)

        x_na = add_lable(frame = self.frame, text = 'X-N/A Count:')
        y_na = add_lable(frame = self.frame, text = 'Y-N/A Count:')

        self.x_na_entry = add_entry(frame = self.frame, text = '0')
        self.y_na_entry = add_entry(frame = self.frame, text = '0')

        hue_lable = add_lable(frame = self.frame, text = 'Hue:')
        hue_combo = add_combobox(frame = self.frame, textvariable = self.hue_var, values = cols)

        hue_na = add_lable(frame=self.frame, text = 'Hue N/A Count:')
        self.hue_na_entry = add_entry(frame = self.frame, text = '0')

        clean_lable = add_lable(frame = self.frame, text = 'N/A strategies:')
        clean_combo = add_combobox(frame = self.frame, textvariable = self.data_cleaner_approach, values=self._na_strategies)

        clean_btn = add_button(
            frame = self.frame, 
            text = 'Clean Data', 
            command = lambda: on_click_clean_btn(
                plot_instance = self,
                clean_strategie=self.data_cleaner_approach.get(),
                xcol=self.data[self.x_var.get()].copy() if self.x_var.get() else None,
                ycol=self.data[self.y_var.get()].copy() if self.y_var.get() else None,
                hue=self.data[self.hue_var.get()].copy() if (self.hue_var.get() and self.hue_var.get() != "None" and self.hue_var.get() in self.data.columns) else None
            )
        )

        plot_type_lable.grid(row = 0, column = 0, sticky= 'ew', padx = 10, pady = 10)
        plot_type.grid(row = 0, column = 1, columnspan = 2, sticky = 'ew', padx = 10, pady = 10)

        x_lable.grid(row = 1, column = 0, sticky= 'ew', padx = 10, pady = 5)
        x_combo.grid(row = 1, column = 1, columnspan = 2, sticky = 'ew', padx = 10, pady = 5)

        x_na.grid(row = 2, column = 0, sticky = 'ew', padx = 10, pady = 5)
        self.x_na_entry.grid(row = 2, column = 1, columnspan = 2, sticky = 'ew', padx = 10, pady = 5)

        if self.kind != 'hist' and self.kind != 'kde' and self.kind != 'ecdf':
            y_lable.grid(row = 3, column = 0, sticky = 'ew', padx = 10, pady = 5)
            y_combo.grid(row = 3, column = 1, columnspan = 2, sticky = 'ew', padx = 10, pady = 5)

            y_na.grid(row = 4, column = 0, sticky = 'ew', padx = 10, pady = 5)
            self.y_na_entry.grid(row = 4, column = 1, columnspan = 2, sticky = 'ew', padx = 10, pady = 5)

        hue_lable.grid(row = 5, column=0, columnspan=1, sticky= 'ew', padx= 10, pady = 5)
        hue_combo.grid(row = 5, column=1, columnspan=2, sticky= 'ew', padx= 10, pady = 5)

        hue_na.grid(row = 6, column=0, columnspan=1, sticky= 'ew', padx= 10, pady = 5)
        self.hue_na_entry.grid(row = 6, column=1, columnspan=2, sticky= 'ew', padx= 10, pady = 5)

        clean_lable.grid(row = 7, column = 0, sticky= 'ew', padx = 10, pady = 5)
        clean_combo.grid(row = 7, column = 1, columnspan = 2, sticky = 'ew', padx = 10, pady = 5)

        clean_btn.grid(row = 8, column=0, columnspan=3, sticky= 'ew', padx= 10, pady = 5)

        self.x_combo = x_combo
        self.y_combo = y_combo
        
        x_combo.bind("<<ComboboxSelected>>", self.update_column_info)
        y_combo.bind("<<ComboboxSelected>>", self.update_column_info)
        hue_combo.bind("<<ComboboxSelected>>", self.update_column_info)

        self.update_column_info()