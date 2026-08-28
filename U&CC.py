import tkinter as tk
import ttkbootstrap as ttk

window = ttk.Window(theme="cyborg")
window.title("Currency Converter")
window.geometry("600x200")

items = ("USD", "GPD")
curr_string = tk.StringVar(value = items[0])
combo = ttk.Combobox(window, textvariable=curr_string, values=items)
combo.pack()


def convert():
    user_input=float(entry_str.get())
    current_unit = curr_string.get()

    if current_unit == "USD":

        result = round((user_input * 1.36))
        output_string.set(f"{result} GPD: ")

    else:

        result = round((user_input * 0.74))
        output_string.set(f"{result}GPD: ")

title_label = ttk.Frame(window)
title_label.pack()

input_frame = ttk.Frame(window)
entry_str = tk.StringVar()
entry = ttk.Entry(input_frame, textvariable=entry_str)
button=ttk.Button(input_frame, text="Convert", command = convert, bootstyle="success-outline-round")
entry.pack(side = "left", padx = 10)
button.pack(side = "right")
input_frame.pack(pady = 10)



output_string = tk.StringVar()
output_label = ttk.Label(window, text="Output", font="Calibri 24", textvariable=output_string)
output_label.pack(pady = 5)
window.mainloop()
