import tkinter as tk


class myGUI:
    def __init__(self):
        self.root = tk.Tk()

        self.label = tk.Label(root, text="this", font=("Arial", 32))

        self.label.pack()

        self.root.mainloop()
