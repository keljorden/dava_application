import matplotlib
matplotlib.use('TkAgg')
import tkinter as tk
from tkinter import ttk
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from ploter import PlotBuilder as pl


# Main Tkinter Application
def main():
    root = tk.Tk()
    root.title("Seaborn + Tkinter Integration")
    root.geometry("800x650")
    
    label = ttk.Label(root, text="Seaborn Figure-Level Plot in Tkinter", font=("Helvetica", 16, "bold"))
    label.pack(pady=10)

    tips = sns.load_dataset("tips")
    chart = pl('violin', data=tips, x='day', y='total_bill', hue='smoker', split=True)

    canvas = FigureCanvasTkAgg(chart.fig, master=root)
    canvas.draw()
    
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    toolbar_frame = ttk.Frame(root)
    toolbar_frame.pack(fill=tk.X)
    toolbar = NavigationToolbar2Tk(canvas, toolbar_frame)
    toolbar.update()

    root.mainloop()

if __name__ == "__main__":
    main()