import tkinter as tk
from tkinter import ttk


def return_pressed(event):
    print(event.keysym)


root = tk.Tk()

btn = ttk.Button(root, text='Save')
btn.bind('<KeyPress>', return_pressed)


btn.focus()
btn.pack(expand=True)

root.mainloop()