import tkinter as tk
from tkinter import filedialog

# Create the main window
root = tk.Tk()
root.title('Rename Files')

# Create the source path label and entry
source_label = tk.Label(root, text='Source Path:')
source_entry = tk.Entry(root, width=50)
source_label.pack()
source_entry.pack()

# Create the source path browse button
def browse_source():
  # Open the file dialog to select the source path
  source_path = filedialog.askdirectory(parent=root, initialdir='/', title='Select Source Path')

  # Update the source path entry
  source_entry.delete(0, tk.END)
  source_entry.insert(0, source_path)

source_button = tk.Button(root, text='Browse', command=browse_source)
source_button.pack()

# Create the output path label and entry
output_label = tk.Label(root, text='Output Path:')
output_entry = tk.Entry(root, width=50)
output_label.pack()
output_entry.pack()

# Create the output path browse button
def browse_output():
  # Open the file dialog to select the output path
  output_path = filedialog.askdirectory(parent=root, initialdir='/', title='Select Output Path')

  # Update the output path entry
  output_entry.delete(0, tk.END)
  output_entry.insert(0, output_path)

output_button = tk.Button(root, text='Browse', command=browse_output)
output_button.pack()

# Create the rename button
def rename_files():
  # Get the source and output paths
  source_path = source_entry.get()
  output_path = output_entry.get()

  # Validate the paths
  if not source_path:
    tk.messagebox.showerror('Error', 'Please select a source path')
    return
  if not output_path:
    tk.messagebox.showerror('Error', 'Please select an output path')
    return

  # Rename the files (replace this with your own code)
  print('Renaming files from', source_path, 'to', output_path)

rename_button = tk.Button(root, text='Rename', command=rename_files)
rename_button.pack()

# Run the main loop
root.mainloop()
