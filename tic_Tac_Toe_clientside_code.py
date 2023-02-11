from tkinter import *

root = Tk()
root.title("9 Tic Tac Toe MP")
root.geometry("590x600")
def startscreen():
    title = Label(root, text="Tic Tac Toe Multiplayer", font=("Arial", 20))
    title.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
    disp = Canvas(root, width=400, height=400, bg="white")

    disp.create_line(0, 133, 400, 133, width=2)
    disp.create_line(0, 266, 400, 266, width=2)
    disp.create_line(133, 0, 133, 400, width=2)
    disp.create_line(266, 0, 266, 400, width=2)
    disp.grid(row=1, column=0, rowspan=3, columnspan=3, padx=10, pady=10)

    notify = Label(root, text="Waiting for Player 2...", font=("Arial", 15), wraplength=150)
    notify.grid(row=1, column=3, rowspan=3, columnspan=2, padx=10, pady=10)

    new = Button(root, text="New Game", font=("Arial", 15), command=newGame())
    new.grid(row=4, column=0, columnspan=5, padx=10, pady=10)

    join = Button(root, text="Join", font=("Arial", 15), command=joinGame())
    join.grid(row=5, column=0, columnspan=5, padx=10, pady=10)

def newGame():
    pass

def joinGame():
    pass

startscreen()
root.mainloop()