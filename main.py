from tkinter import *
import math
import warnings
#warnings.filterwarnings("ignore", category=DeprecationWarning)

""""
equal is only for operators e (exp button), ^(power), *(Multiply),
 + (add), - (substract), / (divide), () (parenthesis) and % (modulu).
 operators such as cos, sin, tan, log (on base 10), ln, square root (and more) are working like equal. upon clicking them, 
 they are working on the number (or mathematical expression such as 5+3) in the entry, and immediately the result
 will show up on the entry.
 "ans" button gives the last answer.
 Syntax errors happen if one of these conditions is satisfied:
 1) there is a Syntax error in the mathematical expression. for example 3xx4, 3+x4, 4+(3, 4+3+ etc...
 2) there is a syntax error with the exp (EXP button)
 3) the variable "ans" was used before the "=" button as given a valid answer
 
"""
root = Tk()
root.title("Scientific Calculator")
root.config(bg = '#32323C')  #the RGB background color
root.resizable(width=False,height= False) #makes the window unresizeable
root.geometry("540x640+500+90") #the size of the window and the coords of where it opens

display = Entry(root, width=35, relief=RIDGE, bd=30,font=('David',20,'bold'), fg="black", bg="#E8E8E8")
display.grid(row=0,column=0,columnspan=5,padx=30,pady=15)
display.insert(0,'0')
display.config(state='readonly')

ans = [False, 0] #the 0 entry implies whether ans is valid or notm 1 entry is the value of the last answer.

#get a string as mathematical expression (where e = 10**, ^ = **), and converting it to a number.
#throws exception if it can't be done, for example when str = "1++2e3"
def compute(Str):
    result = 0
    prblm = False
    i = 0
    while True:
        if i >= len(Str):
            break
        if Str[i] == "A":
            if Str[i-1].isdigit():
                Str = Str[:i] + "*" + Str[i:]
                i+=1
            if ans[0]:
                Str = Str[0:i] + str(ans[1]) + Str[i+3:]
                i+=1
            else:
                prblm = True
                i+=1
        elif Str[i] == "x":
            Str = Str[0:i] + "*" + Str[i+1:]
            i+=1
        elif Str[i] == "e":
            if Str[i+1] == ')':
                prblm = True
            if i != 0:
                if Str[i-1].isdigit():
                    Str = Str[0:i] + "*" + Str[i:]
                    i+=1
            Str = Str[0:i] + "10**" + Str[i+1:]
            i += 4
            continue
        elif Str[i] == "^":
            Str = Str[0:i] + "**" + Str[i+1:]
            i+=2
        else:
            i+=1
    if prblm:
        int("This statements bring an exception")
    return eval(Str)

def checkValid():
    display.config(state='normal')
    mathEx = display.get()
    display.delete(0, END)
    display.config(state='normal')
    try:
        inp = compute(mathEx)
        return (True, inp)
    except:
        return (False)

def equalFunc(event):
    display.config(state='normal')
    if display.get() == "":
        return
    try:
        res = compute(display.get())
        if res == ():
            return
        ans[0] = True
        ans[1] = res
        display.delete(0, END)
        display.insert(0, res)
    except:
        display.delete(0, END)
        display.insert(0, "Syntax Error")
    display.config(state='readonly')

def AC(event):
    display.config(state='normal')
    display.delete(0, END)
    display.config(state='readonly')

#concatenating the button to the what currently represented in the display
def concat(event):
    display.config(state='normal')
    if display.get() == "Syntax Error":
        display.delete(0, END)
    text=event.widget['text']
    if text=="Mod":
        text = "%"
    if text=="EXP":
        text = "e"
    display.insert(len(display.get()), text)
    display.config(state='readonly')

def delet(event):
    display.config(state='normal')
    if display.get() == "Syntax Error" or display.get() == "":
        display.delete(0, END)
    elif display.get()[-1] == "s":
        display.delete(len(display.get())-3, END)
    else:
        display.delete(len(display.get())-1, END)
    display.config(state='readonly')

#concatenating the numbers (when there's "0", it requires special treatment)
def num(event):
    display.config(state='normal')
    if display.get() == "Syntax Error":
        display.delete(0, END)
    text=event.widget['text']
    currStr = display.get()
    if currStr == "0":
        display.delete(0, END)
        display.insert(0, text)
    else:
        display.insert(len(currStr), text)
    display.config(state='readonly')

def factorl(event):
    valid = checkValid()
    try:
        ret = math.factorial(valid[1])
        display.insert(0, ret)
        ans[0] = True
        ans[1] = ret
    except ValueError:
        display.insert(0, "Math Error")
    except:
        display.insert(0, "Syntax Error")
    display.config(state='readonly')

def eexp(event):
    valid = checkValid()
    try:
        ret = math.e**valid[1]
        display.insert(0, ret)
        ans[0] = True
        ans[1] = ret
    except:
        display.insert(0, "Syntax Error")
    display.config(state='readonly')

def cos(event):
    valid = checkValid()
    try:
        ret = math.cos(valid[1])
        display.insert(0, ret)
        ans[0] = True
        ans[1] = ret
    except:
        display.insert(0, "Syntax Error")
    display.config(state='readonly')

def sin(event):
    valid = checkValid()
    try:
        ret = math.sin(valid[1])
        display.insert(0, ret)
        ans[0] = True
        ans[1] = ret
    except:
        display.insert(0, "Syntax Error")
    display.config(state='readonly')

def tan(event):
    valid = checkValid()
    try:
        ret = math.tan(valid[1])
        display.insert(0, ret)
        ans[0] = True
        ans[1] = ret
    except:
        display.insert(0, "Syntax Error")
    display.config(state='readonly')

def log(event):
    valid = checkValid()
    try:
        ret = math.log10(valid[1])
        display.insert(0, ret)
        ans[0] = True
        ans[1] = ret
    except ValueError:
        display.insert(0, "Math Error")
    except:
        display.insert(0, "Syntax Error")
    display.config(state='readonly')

def ln(event):
    valid = checkValid()
    try:
        ret = math.log(valid[1], math.e)
        display.insert(0, ret)
        ans[0] = True
        ans[1] = ret
    except ValueError:
        display.insert(0, "Math Error")
    except:
        display.insert(0, "Syntax Error")
    display.config(state='readonly')

def sqroot(event):
    valid = checkValid()
    try:
        ret = math.sqrt(valid[1])
        display.insert(0, ret)
        ans[0] = True
        ans[1] = ret
    except ValueError:
        display.insert(0, "Math Error")
    except:
        display.insert(0, "Syntax Error")
    display.config(state='readonly')

nums = "789456123"
numBtns = []
index = 0
for i in range(3):
    for j in range(3):
        numBtns.append(Button(root, padx=25, pady=0,font=('arial',20),bd=5,text=nums[index], relief=RAISED))
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
for every expression Xe... where X is a number, we translate it to X*e...
exp doesn't support parenthesis. for example (3+e)5 is a syntax error
examples: ex3 is Syntax Error, e as the last char in the entry is a Syntax Error,
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
clear = Button(root, padx=14, pady=0, font=('arial', 20), bd=5, text="AC", relief=RAISED)
clear.place(x=400, y=360)
clear.bind("<Button-1>", AC)

mult = Button(root, padx=26, pady=0, font=('arial', 20), bd=5, text="x", relief=RAISED)
mult.place(x=305, y=490)
mult.bind("<Button-1>", concat)

div = Button(root, padx=29, pady=0, font=('arial', 20), bd=5, text="/", relief=RAISED)
div.place(x=400, y=490)
div.bind("<Button-1>", concat)

answer = Button(root, padx=10, pady=0, font=('arial', 20), bd=5, text="Ans", relief=RAISED)
answer.place(x=305, y=425)
answer.bind("<Button-1>", concat)

mod = Button(root, padx=3, pady=0, font=('arial', 13), bd=7, text="Mod", relief=RAISED)
mod.place(x=35, y=295)
mod.bind("<Button-1>", concat)

factorial = Button(root, padx=16, pady=0, font=('arial', 13), bd=7, text="!", relief=RAISED)
factorial.place(x=112,y=295)
factorial.bind("<Button-1>", factorl)

openpt = Button(root, padx=16, pady=0, font=('arial', 13), bd=7, text="(", relief=RAISED)
openpt.place(x=189, y=295)
openpt.bind("<Button-1>", concat)

clspt = Button(root, padx=16, pady=0, font=('arial', 13), bd=7, text=")", relief=RAISED)
clspt.place(x=266, y=295)
clspt.bind("<Button-1>", concat)

pwr = Button(root, padx=16, pady=0, font=('arial', 13), bd=7, text="^", relief=RAISED)
pwr.place(x=343, y=295)
pwr.bind("<Button-1>", concat)
EXPe = Button(root, padx=9, pady=0, font=('arial', 13), bd=7, text="e^x", relief=RAISED)
EXPe.place(x=420, y=295)
EXPe.bind("<Button-1>", eexp)

Bcos = Button(root, padx=5, pady=0, font=('arial', 13), bd=7, text="cos", relief=RAISED)
Bcos.place(x=35, y=240)
Bcos.bind("<Button-1>", cos)

Bsin = Button(root, padx=8, pady=0, font=('arial', 13), bd=7, text="sin", relief=RAISED)
Bsin.place(x=112, y=240)
Bsin.bind("<Button-1>", sin)

Btan = Button(root, padx=8, pady=0, font=('arial', 13), bd=7, text="tan", relief=RAISED)
Btan.place(x=189, y=240)
Btan.bind("<Button-1>", tan)

Blog = Button(root, padx=8, pady=0, font=('arial', 13), bd=7, text="log", relief=RAISED)
Blog.place(x=266, y=240)
Blog.bind("<Button-1>", log)

Bln = Button(root, padx=13, pady=0, font=('arial', 13), bd=7, text="ln", relief=RAISED)
Bln.place(x=343, y=240)
Bln.bind("<Button-1>", ln)

BSQroot = Button(root, padx=16, pady=0, font=('arial', 13), bd=7, text=chr(8730), relief=RAISED)
BSQroot.place(x=420, y=240)
BSQroot.bind("<Button-1>", sqroot)

root.mainloop()
