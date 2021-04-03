from tkinter import*
from tkinter.ttk import *

root = Tk()

def myClick():
    myLabel = Label(root,text = "Starting Test Sequence")
    myLabel.pack()

photo = PhotoImage(file = "test.png")
photoimage = photo.subsample(3, 3)


myButton = Button(root,text = "Learn Cable", image = photoimage, compound = BOTTOM, command = myClick)
button_quit = Button(root, text = "Exit", command = root.quit)

myButton.pack()
button_quit.pack()

root.mainloop()