#George Robinson
#Iteration 1
#To Do List

from tkinter import * 
from PIL import Image, ImageTk 
root = Tk()
root.title("To Do") 
root.geometry("600x500") 
root.configure(bg="black") 

def frame1():
    global frame1e
    frame1e = Frame(root)
    frame1e.grid(row=0, column=0, sticky="NSEW")
    frame1e.configure(bg="black")


if 1 == 1:
    frame1()
else:
    frame1()

root.mainloop() # ends the main loop