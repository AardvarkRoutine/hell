from tkinter import *
import random as r

root = Tk()
mainframe = Frame(root)
mainframe.pack()
root.title("9 Tic Tac Toe MP")
root.geometry("590x600")
def stdGameLoop():
    canvas = Canvas(mainframe, width=400, height=400)
    canvas.pack()

    for i in range(1, 3):
        x = i * 133.33
        canvas.create_line(x, 0, x, 400, fill="black")

    for i in range(1, 3):
        y = i * 133.33
        canvas.create_line(0, y, 400, y, fill="black")

    sub_canvases = []
    for i in range(3):
        for j in range(3):
            x1 = j * 133.33
            y1 = i * 133.33
            x2 = x1 + 133.33
            y2 = y1 + 133.33
            sub_canvas = Canvas(canvas, width=133.33, height=133.33, bd=0, highlightthickness=0,bg = r.choice(["red","blue","green","yellow","orange","purple","pink","black","white"]))
            sub_canvas.place(x=x1, y=y1)
            sub_canvases.append(sub_canvas)
stdGameLoop()
root.mainloop()