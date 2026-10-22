# Dava - Data Visualization Application

**Dava** is a desktop-based graphical user interface (GUI) application built with Python and Tkinter. It is designed to make data exploration, cleaning, and visualization intuitive and accessible without requiring users to write any code. By leveraging the power of **Pandas**, **Seaborn**, and **Matplotlib**, Dava allows users to load datasets, inspect data types and missing values, handle nulls, and generate beautiful plots dynamically.

---

## Features

- **Multi-Format Data Loading:** Import datasets seamlessly from your local system. Supported formats include `.csv`, `.xlsx`, `.xls`, `.json`, `.tsv`, and `.txt`.
- **Data Preview & Inspection:**
  * View tabular previews of your dataset (head and tail).
  * Check dataset dimensions (row and column counts).
  * Inspect specific columns for their data type, N/A count, and N/A percentage.
- **Extensive Plotting Options:** 11 different plot types available, categorized by Seaborn's figure-level functions:
  * *Relational:* Scatter, Line
  * *Distribution:* Hist, KDE, ECDF
  * *Categorical:* Strip, Swarm, Boxen, Violin, Bar, Point
- **Built-in Data Cleaning:** Handle missing values (`NaN`) on the fly for the selected X, Y, and Hue columns. Strategies include:
  * Leave as-is
  * Drop Missing (`dropna`)
  * Fill with Zero (`fillna(0)`)
  * Forward Fill (`ffill`)
  * Linear Interpolation
- **Export & Download:** Save your generated visualizations in multiple high-quality formats including `.pdf`, `.png`, `.jpg`, and `.svg`.

---

## Project Structure

- **`dava.py`**: The main application entry point. It initializes the Tkinter window, sets up the left/right pane layout, and acts as the master container.
- **`action.py`**: Contains the core logic for all UI button actions (loading data, triggering plot generation, cleaning data, and handling plot downloads).
- **`ploter.py`**: Defines the `PlotBuilder` class. It manages the dynamic generation of plot control widgets, maps UI selections to Seaborn functions, handles the missing-data cleaning logic, and renders the plot.
- **`data_loader.py`**: Provides the file dialog interface and Pandas logic to load various file formats safely.
- **`data_desc.py`**: Manages the "Dataset Properties" frame, dynamically updating UI elements to show column data types and missing value metrics.
- **`data_preview.py`**: Renders a `ttk.Treeview` table to show a snapshot of the loaded dataset.
- **`wrapper.py`**: A utility module containing wrapper functions to simplify and standardize the creation of Tkinter widgets (frames, buttons, labels, comboboxes).
- **`sample.py`**: A standalone test script demonstrating the basic integration of Seaborn figure-level plots into a Tkinter canvas.

---

## Installation & Setup

1. **Prerequisites:** Ensure you have Python 3.7+ installed on your system.
2. **Install Dependencies:** Install the required Python packages using pip:
   
```bash
pip install pandas matplotlib seaborn openpyxl
```
*(Note: `openpyxl` is required for reading `.xlsx` files)*

3. **Run the Application:**

```bash
python dava.py
```

---

## How to Use

- **Load Data:** Click the "Add Data" button in the top left corner and select a valid dataset file.
- **Inspect Data:** Once loaded, the middle-left frame will show a preview of your data, and the top-left frame will show column properties. You can select different columns from the dropdown to check for missing values.
- **Select Plot Type:** Choose a plot type (e.g., scatter, violin, hist) from the dropdown and click "Select".
- **Configure Plot:** In the bottom-left "Plot Controls" panel:
  - Select your X-axis, Y-axis, and Hue columns.
  - Review the N/A counts for the chosen columns.
  - If there are missing values, select a cleaning strategy from the "N/A strategies" dropdown and click "Clean Data".
- **Visualize:** Click the "Visualize" button in the top-left "File Controls" section. The plot will render in the right-hand panel.
- **Download:** Click "Download Plot" at the top of the right panel to save your visualization to your local machine.

---

## Technologies Used

- **GUI Framework:** Tkinter (tkinter, ttk)
- **Data Manipulation:** Pandas (pandas)
- **Visualization:** Seaborn (seaborn), Matplotlib (matplotlib)