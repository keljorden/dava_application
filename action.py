import tkinter as tk
import pandas as pd
from data_loader import load_dataset_from_system
from data_preview import data_preview_left
from wrapper import *
from data_desc import *
from ploter import PlotBuilder
from tkinter import messagebox, filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

plot_state = {
    'df' : None,
    'current_plot' : None 
}

data_load_btn_state = {'df': None}
def on_click_add_data(preview_frame: tk.Widget, data_desc_frame: tk.Widget):
    df = load_dataset_from_system()
    if df is not None:
        data_load_btn_state['df'] = df
        data_preview_left(preview_frame, data=df)
        describe_dataset(data_desc_frame, data=df)

def on_click_select(bottom_left_frame, selected_plot, df):
    if df is None:
        messagebox.showerror("Error:\t", 'Data set Not selected or Empty')
        return

    df = df
    for widget in bottom_left_frame.winfo_children():
        widget.destroy()
        
    chosen_plot = selected_plot.get()
    current_plot = PlotBuilder(frame = bottom_left_frame, kind = chosen_plot, data = df)
    plot_state["current_plot"] = current_plot


def on_click_visualize(frame: tk.Widget):
    plot = plot_state.get('current_plot')
    if plot is None:
        messagebox.showerror("Error:\t", "Plese select a plot type first.")
        return
        
    method_name = plot._plot_map[plot.kind]
    plot_method = getattr(plot, method_name)
    plot.plt, plot.err = plot_method()
    
    if plot.err:
        messagebox.showerror(plot.err.__class__.__name__, plot.err)
        return
    if plot.plt:
        for widget in frame.winfo_children():
            widget.destroy()
        try:
            canvas = FigureCanvasTkAgg(plot.plt, master=frame)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        except Exception as e:
            messagebox.showerror(e.__class__.__name__, e )

        
def on_click_clean_btn(plot_instance, clean_strategie: str, xcol: pd.Series = None, ycol: pd.Series = None, hue: pd.Series = None):

    series_dict = {}
    if xcol is not None: series_dict[xcol.name] = xcol
    if ycol is not None: series_dict[ycol.name] = ycol
    if hue is not None: series_dict[hue.name] = hue

    if not series_dict:
        return

    combined_df = pd.DataFrame(series_dict)
    strat = clean_strategie.lower()
    
    if "dropna" in strat:
        try:
            clean_df = combined_df.dropna()
        except Exception as e:
            messagebox.showerror("Error:\t", f'{e}')
            return
    elif "zero" in strat or "0" in strat:
        try:
            clean_df = combined_df.fillna(0)
        except Exception as e:
            messagebox.showerror("Error:\t", f'{e}')
            return
    elif "forward" in strat or "ffill" in strat:
        try:
            clean_df = combined_df.ffill()
        except Exception as e:
            messagebox.showerror("Error:\t", f'{e}')
            return
    elif "interpolate" in strat:
        try:
            clean_df = combined_df.interpolate(method='linear')
        except Exception as e:
            messagebox.showerror("Error:\t", f'{e}')
            return
    else:
        clean_df = combined_df

    plot_instance.clean_x = clean_df[xcol.name] if xcol is not None and xcol.name in clean_df.columns else None
    plot_instance.clean_y = clean_df[ycol.name] if ycol is not None and ycol.name in clean_df.columns else None
    plot_instance.clean_hue = clean_df[hue.name] if hue is not None and hue.name in clean_df.columns else None

    plot_instance.update_column_info()
    messagebox.showinfo("Successful:", "X, Y, and Hue successfully cleaned and aligned.")


    
def on_click_download():
    plot = plot_state.get('current_plot')
    
    if plot is None or plot.plt is None:
        messagebox.showerror("Error:\t", "No valid plot available to download. Please select and visualize a plot first.")
        return

    filepath = filedialog.asksaveasfilename(
        title="Save Plot As...",
        defaultextension=".pdf",
        filetypes=[
            ("PDF Document", "*.pdf"),
            ("PNG Image", "*.png"),
            ("JPEG Image", "*.jpg"),
            ("SVG Vector", "*.svg"),
            ("All Files", "*.*")
        ]
    )

    if not filepath:
        messagebox.showwarning('Warning', "Are you sure you don't want to save the plot")
        return

    try:
        plot.plt.savefig(filepath, bbox_inches='tight', dpi=300)
        messagebox.showinfo("Success", f"Plot successfully saved to:\n{filepath}")
    except Exception as e:
        messagebox.showerror("Download Error", f"Failed to save plot:\n{str(e)}")

if __name__ == '__main__':
    print("this file contains code for button actions")