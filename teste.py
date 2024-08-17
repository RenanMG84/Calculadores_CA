import tkinter as tk
from tkinter import messagebox

# Functions for menu actions
def new_file():
    messagebox.showinfo("New File", "New file created!")

def open_file():
    messagebox.showinfo("Open File", "File opened!")

def save_file():
    messagebox.showinfo("Save File", "File saved!")

def exit_app():
    root.quit()

def option_one():
    messagebox.showinfo("Option One", "Option One selected!")

def option_two():
    messagebox.showinfo("Option Two", "Option Two selected!")

def sub_option_one():
    messagebox.showinfo("Sub Option One", "Sub Option One selected!")

def sub_option_two():
    messagebox.showinfo("Sub Option Two", "Sub Option Two selected!")

# Create the main application window
root = tk.Tk()
root.title("Nested Submenus Example")
root.geometry("400x300")

# Create the menu bar
menu_bar = tk.Menu(root)

# Create the File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)

# Create a submenu under the File menu
sub_menu = tk.Menu(file_menu, tearoff=0)
sub_menu.add_command(label="Option 1", command=option_one)
sub_menu.add_command(label="Option 2", command=option_two)

# Create a nested submenu under the first submenu
nested_sub_menu = tk.Menu(sub_menu, tearoff=0)
nested_sub_menu.add_command(label="Sub Option 1", command=sub_option_one)
nested_sub_menu.add_command(label="Sub Option 2", command=sub_option_two)

# Add the nested submenu to the first submenu
sub_menu.add_cascade(label="More Sub Options", menu=nested_sub_menu)

# Add the first submenu to the File menu
file_menu.add_cascade(label="More Options", menu=sub_menu)

file_menu.add_separator()  # Add a separator line
file_menu.add_command(label="Exit", command=exit_app)
menu_bar.add_cascade(label="File", menu=file_menu)

# Create the Edit menu
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Undo")
edit_menu.add_command(label="Redo")
edit_menu.add_separator()
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Create the Help menu
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=lambda: messagebox.showinfo("About", "This is a sample menu with nested submenus"))
menu_bar.add_cascade(label="Help", menu=help_menu)

# Configure the root window to display the menu
root.config(menu=menu_bar)

# Start the Tkinter event loop
root.mainloop()
