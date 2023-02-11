import tkinter as tk
import random as r
root = tk.Tk()
root.title("9 Square Canvas")
global num
num= 0
# Erstelle einen Canvas, der die gesamte Größe des Fensters einnimmt
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Zeichne Linien, um den Canvas in 9 quadratische Teile zu unterteilen
for i in range(1, 3):
    x = i * 133.33
    canvas.create_line(x, 0, x, 400, fill="black")

for i in range(1, 3):
    y = i * 133.33
    canvas.create_line(0, y, 400, y, fill="black")

# Erstelle 9 quadratische Sub-Canvases
sub_canvases = []
for i in range(3):
    for j in range(3):
        x1 = j * 133.33
        y1 = i * 133.33
        x2 = x1 + 133.33
        y2 = y1 + 133.33
        sub_canvas = tk.Canvas(canvas, width=133.33, height=133.33, bd=0, highlightthickness=0,bg = r.choice(["red","blue","green","yellow","orange","purple","pink","black","white"]))
        sub_canvas.place(x=x1, y=y1)
        sub_canvases.append(sub_canvas)
print(sub_canvases)
root.mainloop()
