import tkinter as tk

window = tk.Tk()
window.geometry("600x400")
window.title("Canvas")

#canvas
canvas = tk.Canvas(window, bg = "white")
canvas.pack()

canvas.create_rectangle((50,20,100,200), fill = "red", width=1, dash =(4,2), outline = "orange")
canvas.create_line(0, 0, 100, 150, fill = "blue")
canvas.create_oval(200,0,300,100, fill = "green")
canvas.create_arc(200,0,300,100, fill = "red", start = 45, extent = 180, style=tk.ARC, outline = "yellow", width = 10) 
#canvas.create_polygon((0,0,100,200,300,50, 150, -50), fill = "gray")
window.mainloop()