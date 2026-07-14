import tkinter as tk
from tkinter import ttk
import pandas as pd
from data_loader import load_dataset_from_system
from data_preview import data_preview_left
from layout import *
from action import *

'''data = pd.DataFrame({
    "ID": [101, 102, 103, 104, 105, 106],
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"],
    "Score": [88.5, 92.0, 79.3, 85.1, 91.4, 84.0],
    "Status": ["Active", "Active", "Pending", "Active", "Review", "Active"]
}) '''


plot_type = ['scatter plot', 'line plot','hist plot', 
             'kde plot', 'ecdf plot', 'strip plot', 'swarm plot', 'box plot', 'violin plot', 'bar plot', 'point plot']


# 1. Initialize the main application window
root = tk.Tk()
root.title("Dava")
root.geometry("1024x512")

selected_plot = tk.StringVar(value=plot_type[0])

# 2. Main Container: Horizontal Split (Left vs Right)
main_paned =  split_window(root, 'HORIZONTAL')
main_paned.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

# 3. Left Partition
left_paned = split_window(main_paned, 'VERTICAL')
add_frame(main_paned,left_paned, 1)

# 4. Right Partition
right_frame = create_frame(main_paned, relief=tk.SUNKEN, width=450)
add_frame(main_paned,right_frame, 2)

# 5. Create Top and Bottom frames inside the Left PanedWindow
top_left_frame = create_frame(left_paned, relief=tk.SUNKEN, height=150)
mid_left_frame  = create_frame(left_paned, relief=tk.SUNKEN, height=150)
bottom_left_frame = create_frame(left_paned, relief=tk.SUNKEN, height=250)

#Add them to the left vertical split
add_frame(left_paned,top_left_frame)
add_frame(left_paned,mid_left_frame)
add_frame(left_paned,bottom_left_frame)

#Top-Left Partition
add_lable(top_left_frame, text="File Controls").pack(pady = 5)
data_load_btn = add_button(top_left_frame, text="Add Data", command=lambda: on_click_add_data(mid_left_frame))
data_load_btn.pack(fill=tk.X, padx=10, pady=2)
visualize_btn = add_button(top_left_frame, text="Visualize")
visualize_btn.pack(fill=tk.X, padx=10, pady=2)

#cb_frame = create_frame(top_left_frame, relief = tk.SUNKEN, height = 20)
#add_frame(top_left_frame,cb_frame)
plot_type_cb = add_combobox(top_left_frame, values = plot_type, textvariable = 'selected_plot')
plot_type_cb.pack(fill=tk.X, padx=10, pady=2)

#mid-left partition
add_lable(mid_left_frame, text="Data Preview", font=("Arial", 10, "bold")).pack(pady=(10, 5), padx=10, anchor=tk.W)

#Populate Bottom-Left Partition
add_lable(bottom_left_frame, text="Plot Controls").pack(pady=5)
file_list = tk.Listbox(bottom_left_frame)
file_list.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
file_list.insert(tk.END, f"this is where the controls for plot will be")

#Populate Right Partition
add_lable(right_frame, text= 'Plot', font=("Arial", 11, "bold")).pack(pady=10)


text_area = tk.Text(right_frame, wrap=tk.WORD)
text_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

text_area.insert(tk.END, f'this is where the plot will be visualized')

root.mainloop()