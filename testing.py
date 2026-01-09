import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Tkinter Test")
root.geometry("400x300")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack(fill="both", expand=True)

tk.Label(frame, text="Hello Tkinter!").pack(pady=10)
ttk.Button(frame, text="Click Me").pack(pady=10)

root.mainloop()
