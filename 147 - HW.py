# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 10:31:45 2023

@author: DELL
"""

from tkinter import*

root = Tk()
root.title("Ascii Values")
root.geometry("400x400")
root.configure(background = 'purple')

entry_box = Entry(root)
entry_box.place(relx = 0.5 , rely = 0.4 , anchor = CENTER)

label = Label(root , text = "Name in Ascii : " , bg = "light yellow" , fg = "black")
label_2 = Label(root , text = "Encrypted name :" , bg = "light green" ,fg = "black")

def ascii() :
    input_box = entry_box.get()
    for letter in input_box:
        label["text"] += str(ord(letter)) + " "
        number = int(ord(letter))
        encrypt = number - 1 
        label_2["text"] += str(chr(encrypt))
        
btn = Button(root, text = "Show ascii value of the name", command = ascii ,  bg = "gold" , fg = "black")
btn.place(relx = 0.5 , rely = 0.5 , anchor = CENTER)
label.place(relx = 0.5 , rely = 0.6 , anchor = CENTER)
label_2.place(relx = 0.5 , rely = 0.7 , anchor = CENTER)
root.mainloop()