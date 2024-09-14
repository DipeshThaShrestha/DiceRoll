from tkinter import *
import random
root = Tk()
root.title ("Dice Roll")
root. geometry ("500x500")
label = Label (root , font = ("Helvitica", 400 , 'bold') , text = "", fg= 'red')

def rolldice ():
    dice = ['\u2680', '\u2681' , '\u2682',  '\u2683', '\u2684' , '\u2685']
    label.configure(text = f'{random. choice (dice)}')
    label.pack()

button = Button(root , font = ("Arial" , 25 , 'bold'), text = "Roll Dice", command = rolldice , bg = 'white' , fg = 'blue')
button.pack ()

root.mainloop()
