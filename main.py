import tkinter as tk

root = tk.Tk()
root.title("Hello wold")
root.geometry("300x300")

hello = tk.Label(text="Hello world!")
hello.pack()
button = tk.Button(text="Click me!")
button.pack()

tk.mainloop()