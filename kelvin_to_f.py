
import tkinter as tk
import ttkbootstrap as ttk

window = ttk.Window(themename="cyborg")
window.title("Kelvin to Fahrenheit")
window.geometry("600x250")

items = ("Kelvin", "Fahrenheit")

temp_string = tk.StringVar(value=items[0])

combo = ttk.Combobox(
    window,
    textvariable=temp_string,
    values=items,
    state="readonly"
)
combo.pack(pady=10)


def convert():
    try:
        user_input = entry_value.get()
        current_unit = temp_string.get()

        if current_unit == "Kelvin":
            result = round((user_input - 273.15) * 9 / 5 + 32, 2)
            output_string.set(f"{result} °F")
        else:
            result = round((user_input - 32) * 5 / 9 + 273.15, 2)
            output_string.set(f"{result} K")

    except ValueError:
        output_string.set("Please enter a valid number")


title_label = ttk.Label(
    window,
    text="Temperature Converter",
    font=("Calibri", 24)
)
title_label.pack(pady=10)


input_frame = ttk.Frame(window)
input_frame.pack(pady=10)

entry_value = tk.DoubleVar()

entry = ttk.Entry(
    input_frame,
    textvariable=entry_value,
    width=15
)
entry.pack(side="left", padx=10)

button = ttk.Button(
    input_frame,
    text="Convert",
    command=convert,
    bootstyle="success-outline"
)
button.pack(side="right")


output_string = tk.StringVar(value="Output")

output_label = ttk.Label(
    window,
    textvariable=output_string,
    font=("Calibri", 24)
)
output_label.pack(pady=10)


window.mainloop()
