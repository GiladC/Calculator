from tkinter import *
import math


""""
equal is only for operators e (exp button), ^(power), *(Multiply),
 + (add), - (substract), / (divide), () (parenthesis) and % (modulu).
 operators such as cos, sin, tan, log (on base 10), ln, square root (and more) are working like equal. upon clicking them, 
 they are working on the number (or mathematical expression such as 5+3) in the entry, and immediately the result
 will show up on the entry.
"""


root = Tk()
root.title("Scientific Calculator")
root.config(bg = '#32323C')  #the RGB background color
root.resizable(width=False,height= False) #makes the window unresizeable
root.geometry("540x640+500+90") #the size of the window and the coords of where it opens

display = Entry(root, width=35, relief=RIDGE, bd=30,font=('David',20,'bold'), fg="black", bg="#E8E8E8")
display.grid(row=0,column=0,columnspan=5,padx=30,pady=15)
display.insert(0,'0')
#get a string as mathematical expression (where e = 10**, ^ = **), and converting it to a number.
#throws exception if it can't be done, for example when str = "1++2e3"
def compute(str):
    result = 0
    prblm = False
    i = 0
    while True:
        if i == len(str):
            break
        if str[i] == "x":
            str = str[0:i] + "*" + str[i+1:]
            i+=1
        elif str[i] == "e":
            if i != 0:
                if str[i-1].isdigit():
                    prblm = True
            str = str[0:i] + "10**" + str[i+1:]
            i += 4
            continue
        elif str[i] == "^":
            str = str[0:i] + "**" + str[i+1:]
            i+=2
        else:
            i+=1
    if prblm:
        int("This statements bring an Error")
    return eval(str)

def equalFunc(event):
    try:
        res = compute(display.get())
        display.delete(0, END)
        display.insert(0, res)
    except:
        display.delete(0, END)
        display.insert(0, "Syntax Error")

def AC(event):
    display.delete(0, END)
#concatenating the button to the what currently represented in the display
def concat(event):
    if display.get() == "Syntax Error":
        display.delete(0, END)
    text=event.widget['text']
    if text=="Mod":
        text = "%"
    if text=="EXP":
        text = "e"
    display.insert(len(display.get()), text)
def delet(event):
    display.delete(len(display.get())-1, END)
#concatenating the numbers (when there's "0", it requires special treatment)
def num(event):
    if display.get() == "Syntax Error":
        display.delete(0, END)
    text=event.widget['text']
    currStr = display.get()
    if currStr == "0":
        display.delete(0, END)
        display.insert(0, text)
    else:
        display.insert(len(currStr), text)
str = "789456123"
numBtns = []
index = 0
for i in range(3):
    for j in range(3):
        numBtns.append(Button(root, padx=25, pady=0,font=('arial',20),bd=5,text=str[index], relief=RAISED))
        numBtns[index].place(x=20+95*j,y=65*i+360)
        numBtns[index].bind("<Button-1>",num)
        index+=1
zero = Button(root, padx=25, pady=0, font=('arial', 20), bd=5, text="0", relief=RAISED)
zero.place(x=20, y=555)
zero.bind("<Button-1>", num)
decimal = Button(root, padx=29, pady=0, font=('arial', 20), bd=5, text=".", relief=RAISED)
decimal.place(x=115, y=555)
decimal.bind("<Button-1>", concat)
""""
exp button represented as "e" and represents the power of 10. for example e35 = 10^35, en = 10^n
rules: every expression eX where x is a number, is translated to 10**X.
3e5 is Syntax Error, ex3 is Syntax Error, e as the last char is Syntax Error,
3*e5=3*10**5=300000, 3+e2 = 3+10**2 = 103, ee2 = 10**10**2 = 10**100,
e+3 = 10**+3=10**3=100, e-1 = 10**-1=0.1
"""
exp = Button(root, padx=7, pady=0, font=('arial', 20), bd=5, text="EXP", relief=RAISED)
exp.place(x=210, y=555)
exp.bind("<Button-1>", concat)
plus = Button(root, padx=24, pady=0, font=('arial', 20), bd=5, text="+", relief=RAISED)
plus.place(x=305, y=555)
plus.bind("<Button-1>", concat)
minus = Button(root, padx=29, pady=0, font=('arial', 20), bd=5, text="-", relief=RAISED)
minus.place(x=400, y=555)
minus.bind("<Button-1>", concat)
#delete last character
delete = Button(root, padx=5, pady=0, font=('arial', 20), bd=5, text="DEL", relief=RAISED)
delete.place(x=305, y=360)
delete.bind("<Button-1>",delet)
equal = Button(root, padx=25, pady=0, font=('arial', 20), bd=5, text="=", relief=RAISED)
equal.place(x=400, y=425)
equal.bind("<Button-1>", equalFunc)
#clears the entry
clear = Button(root, padx=6, pady=0, font=('arial', 20), bd=5, text="CLR", relief=RAISED)
clear.place(x=400, y=360)
clear.bind("<Button-1>", AC)
mult = Button(root, padx=26, pady=0, font=('arial', 20), bd=5, text="x", relief=RAISED)
mult.place(x=305, y=490)
mult.bind("<Button-1>", concat)
div = Button(root, padx=29, pady=0, font=('arial', 20), bd=5, text="/", relief=RAISED)
div.place(x=400, y=490)
div.bind("<Button-1>", concat)
mod = Button(root, padx=5, pady=0, font=('arial', 20), bd=5, text="Mod", relief=RAISED)
mod.place(x=305, y=425)
mod.bind("<Button-1>", concat)
root.mainloop()

