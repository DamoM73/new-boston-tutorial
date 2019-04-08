from tkinter import *


def doNothing():
    print("ok ok I won't...")

root = Tk()

mainMenu = Menu(root)
root.config(menu=mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="New...", command=doNothing)
fileMenu.add_command(label="Save", command=doNothing)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=doNothing)

editMenu = Menu(mainMenu)
mainMenu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Undo", command=doNothing)
editMenu.add_command(label="Redo", command=doNothing)

root.mainloop()