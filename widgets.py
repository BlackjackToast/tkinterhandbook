import tkinter as tk
from tkinter import ttk

def button_func2():
    print("Hello!")

def button_func():
    print("Button was pressed")

#window
window = tk.Tk()
window.title ("Window and Widgets stuff")
window.geometry("800x500")

#all widgets below

#widgets tkk label
text = tk.Text(master = window)
text.pack()

#ttk widgets tk label
label = ttk.Label(master = window, text =  "this is a test")
label.pack()


#tkk entry
entry = ttk.Entry(master = window)
entry.pack()

label2 =ttk.Label(master = window, text = "my label")
label2.pack()

button2 = tk.Button(master = window, text = "print hello", command = button_func2)
button2.pack()



#ttk button
button = ttk.Button(master = window, text = "A button", command = button_func)
button.pack()
        

#run mainloop updates da gui
window.mainloop()
