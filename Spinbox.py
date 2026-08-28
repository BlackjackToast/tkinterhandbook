import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("600x400")
window.title("Combo and Spin")

#combobox
items = ("idfk", "idek", "idrk")
idk_string = tk.StringVar(value = items[0])
items2 = ("A", "B", "C", "D", "E")
combo = ttk.Combobox(window, textvariable=idk_string)
combo["values"]  = items
combo.pack()


combo.bind("<<ComboboxSelected>>", lambda event: combo_label.config(text = f"selected value: {idk_string.get()}"))
combo_label = ttk.Label(window, text = "a label")
combo_label.pack()

spin_int = tk.IntVar(value = 12)
spin= ttk.Spinbox(window, from_ = 3, to = 20, command = lambda: print(spin_int.get()), textvariable = spin_int)
spin.bind("<<Increment>>", lambda event: print("up"))
spin.bind("<<Decrement>>", lambda event: print("down"))
#spin["value"] = (1,2,3,4,5)
spin.pack()

spin2 = ttk.Spinbox(window,)




window.mainloop()