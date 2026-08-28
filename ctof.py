import tkinter as tk
import ttkbootstrap as ttk





window = ttk.Window(theme = "cyborg")
window.title("Fahrenheit To Celsius")
window.geometry("600x200")


items = ("Fahrenheit", "Celsius")
temp_string = tk.StringVar(value = items[0])
combo = ttk.Combobox(window, textvariable=temp_string)

def convert():
    user_input = entry_Int.get()
    current_unit = temp_string.get()

    if current_unit == "Fahrenheit":
        
        result = round((user_input - 32) / 1.8, 2)
        output_string.set(f"{result} °C")
    else:
       
        result = round((user_input * 1.8) + 32, 2)
        output_string.set(f"{result} °F")



combo["values"] = items
combo.pack()



title_label = ttk.Label(window, text = "Fahrenheit to Celcius", font = "Calibri 24")
title_label.pack()

input_frame = ttk.Frame(window)
entry_Int = tk.IntVar()
entry = ttk.Entry(input_frame, textvariable = entry_Int)
button = ttk.Button(input_frame, text = "Convert", command = convert, bootstyle="success-outline-round")
entry.pack(side = "left", padx = 10)
button.pack(side = "right")
input_frame.pack(pady = 10)


output_string = tk.StringVar()
output_label = ttk.Label(window, text = "Output", font = "Calibri 24", textvariable = output_string)
output_label.pack(pady = 5)

window.mainloop()

    