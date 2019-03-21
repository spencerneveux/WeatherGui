import tkinter as tk
from tkinter import Menu
from tkinter import ttk  # themed shit

# ================
# Functions
# ================

def _quit():
    win.quit()
    win.destroy()
    exit()


# create instance
win = tk.Tk()

# sets the gui title bar
win.title("Weather")

menubar = Menu()
win.config(menu=menubar)

# Add file menu bar
fileMenu = Menu(menubar, tearoff=0)
fileMenu.add_command(label="New")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=_quit)
menubar.add_cascade(label="File", menu=fileMenu)

# Add help bar
helpMenu = Menu(menubar, tearoff=0)
helpMenu.add_command(label="About")
menubar.add_cascade(label="Help", menu=helpMenu)

tabControl = ttk.Notebook(win)
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Tab 1')

tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='Tab 2')
tabControl.pack(expand=1, fill="both")

weather_frame = ttk.LabelFrame(tab1, text='Current Weather Conditions')
weather_frame.grid(column=0, row=0, padx=8, pady=4)
ttk.Label(weather_frame, text="Location").grid(column=0, row=0, sticky='W')

# sets the minimum size that the gui can be
win.minsize(300, 1)

# runs the program
win.mainloop()