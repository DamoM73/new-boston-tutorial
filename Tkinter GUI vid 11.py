from tkinter import *


def doNothing():
    print("ok ok I won't...")

root = Tk()

# ***** Main Menu *****

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

# ***** Toolbar *****

toolbar = Frame(root, bg="light blue")

newBtn = Button(toolbar,text="New", command=doNothing)
newBtn.pack(side=LEFT, padx=2, pady=2)
saveBtn = Button(toolbar, text="Save", command=doNothing)
saveBtn.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

# ***** Status Bar *****

status = Label(root, text="Preparing to do nothing...", bd=1, relief=SUNKEN, bg="light grey", anchor=W)
status.pack(side=BOTTOM, fill=X)

root.mainloop()