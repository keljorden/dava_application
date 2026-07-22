import tkinter as tk
from wrapper import *
from action import *

plot_type = ['scatter', 'line','hist', 
             'kde', 'ecdf', 'strip', 'swarm', 'boxen', 'violin', 'bar', 'point']


# 1. Initialize the main application window
root = tk.Tk()
root.title("Dava")
root.geometry("1024x720")
root.state( 'zoomed')

selected_plot = tk.StringVar(value=plot_type[0])

# 2. Main Container: Horizontal Split (Left vs Right)
main_paned =  split_window(root, 'HORIZONTAL')
main_paned.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

# 3. Left Partition
left_paned = split_window(main_paned, 'VERTICAL')
add_frame(main_paned,left_paned, 0)
left_paned.config(width=350)

# 4. Right Partition
right_paned = split_window(main_paned, 'VERTICAL')
add_frame(main_paned,right_paned)

right_title_frame = create_frame(right_paned, relief=tk.SUNKEN, width=450)
add_frame(right_paned, right_title_frame, 0)

right_plot_frame = create_frame(right_paned, relief=tk.SUNKEN, width=450)
add_frame(right_paned,right_plot_frame)

right_download_frame = create_frame(right_paned, relief=tk.SUNKEN, width=450)
add_frame(right_paned, right_download_frame, 0)

#Populate Right Partition

right_download_frame.grid_columnconfigure(0, weight = 1)
add_lable(right_title_frame, text = 'Plot.').pack(pady=5)
download_btn = add_button(right_download_frame, text = 'Download Plot.', padding = (0, 15), command = on_click_download)
download_btn.grid(row = 0, column = 0, sticky = 'ew')
text_area = tk.Text(right_plot_frame, wrap=tk.WORD)
text_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
text_area.insert(tk.END, f'this is where the plot will be visualized')

# 5. Create Top, Mid and Bottom frames inside the Left PanedWindow

top_left_paned = split_window(main_paned, 'VERTICAL')
add_frame(left_paned,top_left_paned, 0)
top_left_paned.config( height = 320)

mid_left_lable_frame = create_frame(left_paned, relief=tk.SUNKEN, height=20) 
mid_left_frame  = create_frame(left_paned, relief=tk.SUNKEN, height=150)
bottom_left_lable_frame = create_frame(left_paned, relief=tk.SUNKEN, height=20) 
bottom_left_frame = create_frame(left_paned, relief=tk.SUNKEN, height=250)

top_left_file_control_frame = create_frame(top_left_paned, relief=tk.SUNKEN, height=80)
top_left_data_desc_frame = create_frame(top_left_paned, relief=tk.SUNKEN, height=200)

#Add them to the left vertical split
add_frame(top_left_paned, top_left_file_control_frame, 0)
add_frame(top_left_paned, top_left_data_desc_frame,0)
add_frame(left_paned,mid_left_lable_frame,0)
add_frame(left_paned,mid_left_frame,0)
add_frame(left_paned,bottom_left_lable_frame,0)
add_frame(left_paned,bottom_left_frame)

#top left file control frame

# Configure Column Weights (Ratio 1 : 3) 
top_left_file_control_frame.grid_columnconfigure(0, weight=3)
top_left_file_control_frame.grid_columnconfigure(1, weight=1)

add_lable(top_left_file_control_frame, text="File Controls").grid( row=0, column=0, columnspan=2, pady=5)

data_load_btn = add_button(top_left_file_control_frame, text="Add Data", command=lambda: on_click_add_data(mid_left_frame, top_left_data_desc_frame))
data_load_btn.grid(row=1, column=0, columnspan=2, sticky="ew", padx=10, pady=2)

visualize_btn = add_button(top_left_file_control_frame, text="Visualize", padding = (0, 8), command = lambda: on_click_visualize(frame = right_plot_frame))
visualize_btn.grid(row=2, column=0, columnspan=2, sticky="ew", padx=10, pady=2)

plot_type_cb = add_combobox(top_left_file_control_frame, values=plot_type, textvariable=selected_plot )
plot_type_cb.grid(row=3, column=0, sticky="ew", padx=10, pady=2)

select_plot_btn = add_button(top_left_file_control_frame, text="Select", command=lambda: on_click_select(bottom_left_frame, selected_plot, data_load_btn_state['df']))
select_plot_btn.grid( row=3, column=1, sticky="ew", padx=(2,10), pady=2 )

#top_left_data_desc_frame
add_lable(top_left_data_desc_frame, text="Dataset Properties").pack(pady=5)

#mid-left partition
add_lable(mid_left_lable_frame, text="Dataset Preview", font=("Arial", 10, "bold")).pack(pady=2)

#Populate Bottom-Left Partition
add_lable(bottom_left_lable_frame, text="Plot Controls", font=("Arial", 10, "bold")).pack(pady=2)
file_list = tk.Listbox(bottom_left_frame)
file_list.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
file_list.insert(tk.END, f"this is where the controls for plot will be")

root.mainloop()