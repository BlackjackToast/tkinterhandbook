import tkinter as tk
from tkinter import ttk

def get_pos(event):
    print(f"x: {event.x} y: {event.y}")

#window
window = tk.Tk()
window.geometry("600x500")
window.title("Event binding")

#widgets
text = tk.Text(window)
text.pack()

entry = ttk.Entry(window)
entry.pack()

button = ttk.Button(window, text = "A button")
button.pack()

button.bind("<Alt-KeyPress-a>", lambda event: print(event))
button.bind("<Motion>", get_pos)

window.bind("<KeyPress>", lambda event: print(f"A button was pressed ({event.char})"))

entry.bind("<FocusIn>", lambda event: print("entry field was selected"))

text.bind("<Shift-MouseWheel>", lambda event: print("MouseWheel"))

window.mainloop()