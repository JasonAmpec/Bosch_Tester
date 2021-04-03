import smbus
import time
import MCP_lib
import numpy as np
#from tkinter import*
#from tkinter.ttk import *

import tkinter as tk
from tkinter import ttk


f = open("results.txt","w")

y = 0
B_string = 0
arraysize = 0 

#initial
MCP_lib.init()

root = tk.Tk()
root.geometry("600x700")
#halv36 = tkFont.Font(family = 'Helvetica', size = 36, weight = 'bold')

def learn_store():
    global Learn
    Learn = MCP_lib.scan()
    
    Learning_status = tk.Label(root, image = Tick)
    Learning_status.grid(column = 2, row = 1)
    return Learn

def print_cable():
    Learn_cable = tk.Label(root, text = Learn)
    Learn_cable.grid(column = 2, row = 1, columnspan = 3)

def test_cable():
    global tested_cable
    tested_cable = MCP_lib.scan()
    
    print ("************tested cable************* ")
    for data in tested_cable:
        print(data)
    print ("*********Learn**************")
    for data in Learn:
        print(data)

    if ((tested_cable == Learn).all()):
        Passed = tk.Label(root, image = Pass_img)
        Passed.grid(column = 2, row = 2)
    elif ((tested_cable != Learn).any()):
        Rejected = tk.Label(root, image = Reject_img)
        Rejected.grid(column = 2, row = 2)

photo = tk.PhotoImage(file = "Learn.png")
DMM = photo.subsample(5, 5)
photo = tk.PhotoImage(file = "test.png")
test_img = photo.subsample(2, 2)
photo = tk.PhotoImage(file = "tick.png")
Tick = photo.zoom(1,1)
photo = tk.PhotoImage(file = "Passed.png")
Pass_img = photo.subsample(2,2)
photo = tk.PhotoImage(file = "Rejected.png")
Reject_img = photo.subsample(2,2)

learn_button = tk.Button(root,text = "Learn Cable", font=("Helvetica", 30), fg = "Green", image = DMM, compound = tk.BOTTOM, command = lambda: learn_store())
print_button = tk.Button(root,text = "Test Cable", font=("Helvetica",30), fg = "Red", imag = test_img, compound = tk.BOTTOM, command = test_cable)
button_quit = tk.Button(root, text = "      Exit       ", font=("Helvetica",40), fg = "Yellow", bg = "Red", command = root.quit)



learn_button.grid(column = 1, row = 1, columnspan = 1)
print_button.grid(column = 1, row = 2, columnspan = 1)
button_quit.grid(column = 2, row = 3, columnspan = 4)


#f.write("Learning Results: \n12345678\n")
#arraysize = Learn.size
#while (y < arraysize):
#    B_string = Learn[y]
#    f.write(B_string)
#    f.write("\n")
#    y= y+1
    
#f.close()
#Learn = np.delete(Learn,1)

  
print("**************END***************")

root.mainloop()

 
