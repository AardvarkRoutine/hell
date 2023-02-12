from tkinter import *
import random as r

root = Tk()
mainframe = Frame(root)
root.title("9 Tic Tac Toe MP")
root.geometry("590x600")
def startscreen():
    title = Label(mainframe, text="Tic Tac Toe Multiplayer", font=("Arial", 20))
    title.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
    disp = Canvas(mainframe, width=400, height=400, bg="white")

    disp.create_line(0, 133, 400, 133, width=2)
    disp.create_line(0, 266, 400, 266, width=2)
    disp.create_line(133, 0, 133, 400, width=2)
    disp.create_line(266, 0, 266, 400, width=2)
    disp.grid(row=1, column=0, rowspan=3, columnspan=3, padx=10, pady=10)

    notify = Label(mainframe, text="Waiting for Player 2...", font=("Arial", 15), wraplength=150)
    notify.grid(row=1, column=3, rowspan=3, columnspan=2, padx=10, pady=10)

    new = Button(mainframe, text="New Game", font=("Arial", 15), command=newGame())
    new.grid(row=4, column=0, columnspan=5, padx=10, pady=10)

    join = Button(mainframe, text="Join", font=("Arial", 15), command=joinGame())
    join.grid(row=5, column=0, columnspan=5, padx=10, pady=10)

def newGame():
    pass

def joinGame():
    pass


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
            print("x1: ", x1, "y1: ", y1, "x2: ", x2, "y2: ", y2)
            sub_canvas = tk.Canvas(canvas, width=133.33, height=133.33, bd=0, highlightthickness=0,bg = r.choice(["red","blue","green","yellow","orange","purple","pink","black","white"]))
            sub_canvas.place(x=x1, y=y1)
            sub_canvases.append(sub_canvas)

stdGameLoop()
mainframe.mainloop()
