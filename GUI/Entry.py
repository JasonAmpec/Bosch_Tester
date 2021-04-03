from tkinter import*

root = Tk()

e = Entry(root, width = 50)
e.pack()

def myClick():
    myLabel = Label(root,text = "Hellow," + e.get())
    myLabel.pack()

myButton = Button(root,text = "Learn Cable",padx = 50, pady = 50, command = myClick)

myButton.pack()

root.mainloop()