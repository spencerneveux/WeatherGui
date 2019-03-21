from tkinter import  *
from tkinter import ttk

# Instantiate the base window
root = Tk()
button = ttk.Button(root, text="Click Me")

# Label
label = ttk.Label(root, text = "YO Mutha fucka")
label.pack()


# Handling button clicking
def callback():
    print('Clicked')


# put button on window
button.pack()
button.config(command=callback)

# Run the program
root.mainloop()

