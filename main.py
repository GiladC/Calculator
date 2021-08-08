from tkinter import *
import math
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=SyntaxWarning)

""""
equal is only for operators E (EXP button), ^ (power), * (multiply),
 + (add), - (substract), / (divide), () (parenthesis) and % (modulo).
 the operators ()², cos⁻¹, sin⁻¹, tan⁻¹, cosh, sinh, tanh, cos, sin, tan, log, ln, square root, factorial and eˣ
  are working like equal. upon clicking them, they are operated on the number
   (or mathematical expression such as 5+3) at the display, and immediately the result
 will show up at the display.
 "Ans" button gives the last answer, it can be upon pressing "=" or upon pressing any of the opeartors that immediately 
 calculate the result and put it at the display.
 Syntax Error appears if and only if at least one of these conditions is satisfied:
 1) there is a Syntax error in the mathematical expression. for example 3xx4, 3+x4, 4+(3, 4+3+, () etc...
 2) there is a syntax error regarding to the EXP/π/math.e button. for example E5, e5, π5, π+ etc...
 3) the Button "Ans" was used before that button was given a valid value. 
 Math Error appears if and only if an illegal thing was calculated. for example 0.5!, (-3)^0.5, cos⁻¹(2) etc...
 Result Too Large appears if and only if the excepted result is to high for python. namely, when an OverFlowError is thrown.
"""
root = Tk()
root.title("Scientific Calculator")
root.config(bg='#32323C')  # the RGB background color
root.resizable(width=False, height=False)  # makes the window unresizeable
root.geometry("540x640+500+90")  # the size of the window and the coords of where it opens

display = Entry(root, width=35, relief=RIDGE, bd=30, font=('David', 20, 'bold'), fg="black", bg="#E8E8E8")
display.grid(row=0, column=0, columnspan=5, padx=30, pady=15)
display.insert(0, '0')
display.config(state='readonly')

ans = [False, 0]  # the 0 entry implies whether ans is valid or notm 1 entry is the value of the last answer.


# get a string as mathematical expression (where e = 10**, ^ = **), and converting it to a number.
# throws exception if it can't be done, for example when str = "1++2e3"
def compute(Str):
    result = 0
    prblm = False
    i = 0
    while True:
        if i >= len(Str):
            break
        elif Str[i] == "e":
            if i != len(Str) -1 and Str[i+1].isdigit():
                int("This statements bring an exception")
            if i > 0 and Str[i-1].isdigit():
                Str = Str[:i] + "*" + Str[i:]
                i+=1
            Str = Str[:i] + str(math.e) + Str[i+1:]
            i+=len(str(math.e))
        elif Str[i] == "π":
            if i != len(Str) -1 and Str[i+1].isdigit():
                int("This statements bring an exception")
            if i > 0 and Str[i-1].isdigit():
                Str = Str[0:i] + "*" + Str[i:]
                i+=1
            Str = Str[:i] + str(math.pi) + Str[i+1:]
            i+=len(str(math.pi))-1
        elif Str[i] == "A":
            if Str[i - 1].isdigit():
                Str = Str[:i] + "*" + Str[i:]
                i += 1
            if ans[0]:
                Str = Str[0:i] + str(ans[1]) + Str[i + 3:]
                i += 1
            else:
                prblm = True
                i += 1
        elif Str[i] == "x":
            Str = Str[0:i] + "*" + Str[i + 1:]
            i += 1
        elif Str[i] == "E":
            if Str[i + 1] == ')':
                prblm = True
            if i != 0:
                if Str[i - 1].isdigit():
                    Str = Str[0:i] + "*" + Str[i:]
                    i += 1
            Str = Str[0:i] + "10**" + Str[i + 1:]
            i += 4
            continue
        elif Str[i] == "^":
            Str = Str[0:i] + "**" + Str[i + 1:]
            i += 2
        else:
            i += 1
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
        for i in range(len(display.get())):
            if display.get()[i] == "e":
                display.delete(i, i+1)
                display.insert(i, "E")
    except OverflowError:
        display.delete(0, END)
        display.insert(0, "Result Too Large")
    except:
        display.delete(0, END)
        display.insert(0, "Syntax Error")
    display.config(state='readonly')


def AC(event):
    display.config(state='normal')
    display.delete(0, END)
    display.config(state='readonly')


# concatenating the button to the what currently represented in the display
def concat(event):
    display.config(state='normal')
    if (display.get() == "Syntax Error" or display.get() == "Math Error"):
        display.delete(0, END)
    text = event.widget['text']
    if text == "Mod":
        text = "%"
    if text == "EXP":
        text = "E"
    display.insert(len(display.get()), text)
    display.config(state='readonly')


def delet(event):
    display.config(state='normal')
    if display.get() == "Syntax Error" or display.get() == "" or display.get() == "Math Error" or display.get() == "Result Too Large":
        display.delete(0, END)
    elif display.get()[-1] == "s":
        display.delete(len(display.get()) - 3, END)
    else:
        display.delete(len(display.get()) - 1, END)
    display.config(state='readonly')


# concatenating the numbers (when there's "0", it requires special treatment)
def num(event):
    display.config(state='normal')
    if (display.get() == "Syntax Error" or display.get() == "Math Error" or display.get() == "Result Too Large"):
        display.delete(0, END)
    text = event.widget['text']
    currStr = display.get()
    if currStr == "0":
        display.delete(0, END)
        display.insert(0, text)
    else:
        display.insert(len(currStr), text)
    display.config(state='readonly')

funcdict = {"!" : lambda x: math.factorial(x), "eˣ" : lambda x: math.e**x, "cos" : lambda x: math.cos(x),
            "sin" : lambda x: math.sin(x), "tan" : lambda x: math.tan(x), "log" : lambda x: math.log10(x),
            "ln" : lambda x: math.log(x, math.e), chr(8730) : lambda x: math.sqrt(x), "tan⁻¹" : lambda x: math.atan(x),
            "cos⁻¹" : lambda x: math.acos(x), "sin⁻¹" : lambda x: math.asin(x), "x²" : lambda x: x**2,
            "sinh" : lambda x: math.sinh(x), "cosh" : lambda x: math.cosh(x), "tanh" : lambda x: math.tanh(x)}

trigs = {"cos", "sin", "tan"}
invtrigs = {"sin⁻¹", "cos⁻¹", "tan⁻¹"}

def mathfunc(event):
    funcStr = event.widget['text']
    valid = checkValid()
    try:
        val = valid[1]
        if trigs.__contains__(funcStr):
            val = val*valdict[Bmode['text']]
        ret = funcdict[funcStr](val)
        if invtrigs.__contains__(funcStr):
            ret = ret/valdict[Bmode['text']]
        display.insert(0, ret)
        for i in range(len(display.get())):
            if display.get()[i] == "e":
                display.delete(i, i+1)
                display.insert(i, "E")
        ans[0] = True
        ans[1] = ret
    except ValueError:
        display.insert(0, "Math Error")
    except OverflowError:
        display.insert(0, "Result Too Large")
    except:
       display.insert(0, "Syntax Error")

modedict = {"deg" : "rad", "rad" : "gra", "gra" : "deg"}

valdict = {"deg" : math.pi/180, "rad" : 1, "gra" : math.pi/200}

def modechange(event):
    prevmode = event.widget['text']
    event.widget['text'] = modedict[prevmode]
    if prevmode == "gra":
        event.widget['padx'] -=1
    elif prevmode == "deg":
        event.widget['padx'] +=1

nums = "789456123"
numBtns = []
index = 0
#an easier way to generate all the buttons of the numbers 1,2,3,4,5,6,7,8,9
for i in range(3):
    for j in range(3):
        numBtns.append(Button(root, padx=25, pady=0, font=('arial', 20), bd=5, text=nums[index], relief=RAISED))
        numBtns[index].place(x=20 + 95 * j, y=65 * i + 360)
        numBtns[index].bind("<Button-1>", num)
        index += 1

#the button of the number zero
zero = Button(root, padx=25, pady=0, font=('arial', 20), bd=5, text="0", relief=RAISED)
zero.place(x=20, y=555)
zero.bind("<Button-1>", num)

#decimal point
decimal = Button(root, padx=29, pady=0, font=('arial', 20), bd=5, text=".", relief=RAISED)
decimal.place(x=115, y=555)
decimal.bind("<Button-1>", concat)
""""
EXP button represented as "E" and represents the power of 10. for example E35 = 10^35, En = 10^n
rules: every expression EX where x is a number, is translated to 10**X. 
for every expression yE(rest of display), where y is a number, we translate it to y*E(rest of display)
exp doesn't support parenthesis. for example (3+e)5 is a syntax error
examples: ex3 is Syntax Error, e as the last char in the entry is a Syntax Error,
3*e5=3*10**5=300000, 3+e2 = 3+10**2 = 103, ee2 = 10**10**2 = 10**100,
e+3 = 10**+3=10**3=100, e-1 = 10**-1=0.1
"""
exp = Button(root, padx=7, pady=0, font=('arial', 20), bd=5, text="EXP", relief=RAISED)
exp.place(x=210, y=555)
exp.bind("<Button-1>", concat)

#plus operator
plus = Button(root, padx=24, pady=0, font=('arial', 20), bd=5, text="+", relief=RAISED)
plus.place(x=305, y=555)
plus.bind("<Button-1>", concat)

#minus operator
minus = Button(root, padx=29, pady=0, font=('arial', 20), bd=5, text="-", relief=RAISED)
minus.place(x=400, y=555)
minus.bind("<Button-1>", concat)
"""
upon pressing the delete button the last character at the display is deleted. special cases are when the last thing is "Ans",
and it deletes the 3 last characters (namely, deletes the Ans at the end). another special case is when there is either
"Syntax Error", "Math Error" or "Result Too Large" on the display, then it operates like allclear (clears the entire display)
"""
delete = Button(root, padx=6, pady=0, font=('arial', 20), bd=5, text="DEL", relief=RAISED)
delete.place(x=305, y=360)
delete.bind("<Button-1>", delet)

#calculates the expression in the display according to the rules specified at the first comment. the function eval() is used.
equal = Button(root, padx=25, pady=0, font=('arial', 20), bd=5, text="=", relief=RAISED)
equal.place(x=400, y=425)
equal.bind("<Button-1>", equalFunc)

#Clears the entire display
allclear = Button(root, padx=14, pady=0, font=('arial', 20), bd=5, text="AC", relief=RAISED)
allclear.place(x=400, y=360)
allclear.bind("<Button-1>", AC)

#the multiplication button
mult = Button(root, padx=26, pady=0, font=('arial', 20), bd=5, text="x", relief=RAISED)
mult.place(x=305, y=490)
mult.bind("<Button-1>", concat)

#the division button
div = Button(root, padx=29, pady=0, font=('arial', 20), bd=5, text="/", relief=RAISED)
div.place(x=400, y=490)
div.bind("<Button-1>", concat)

#the Ans button
answer = Button(root, padx=9, pady=0, font=('arial', 20), bd=5, text="Ans", relief=RAISED)
answer.place(x=305, y=425)
answer.bind("<Button-1>", concat)

#the % (modulo) button
mod = Button(root, padx=5, pady=0, font=('arial', 13), bd=7, text="Mod", relief=RAISED)
mod.place(x=30, y=295)
mod.bind("<Button-1>", concat)

#the factorial operator. n!= 1*2*3*...*n
factorial = Button(root, padx=18, pady=0, font=('arial', 13), bd=7, text="!", relief=RAISED)
factorial.place(x=107, y=295)
factorial.bind("<Button-1>", mathfunc)

#the parenthesis "(" button
openpt = Button(root, padx=18, pady=0, font=('arial', 13), bd=7, text="(", relief=RAISED)
openpt.place(x=184, y=295)
openpt.bind("<Button-1>", concat)

#the parenthesis ")" button
clspt = Button(root, padx=18, pady=0, font=('arial', 13), bd=7, text=")", relief=RAISED)
clspt.place(x=261, y=295)
clspt.bind("<Button-1>", concat)

#the power operator. a^n = a*a*a*...*a n times
pwr = Button(root, padx=18, pady=0, font=('arial', 13), bd=7, text="^", relief=RAISED)
pwr.place(x=338, y=295)
pwr.bind("<Button-1>", concat)

#this operator returns e to the power of the number at the display
EXPe = Button(root, padx=16, pady=0, font=('arial', 13), bd=7, text="eˣ", relief=RAISED)
EXPe.place(x=415, y=295)
EXPe.bind("<Button-1>", mathfunc)

#cos opeartor
Bcos = Button(root, padx=7, pady=0, font=('arial', 13), bd=7, text="cos", relief=RAISED)
Bcos.place(x=30, y=240)
Bcos.bind("<Button-1>", mathfunc)

#sin operator
Bsin = Button(root, padx=10, pady=0, font=('arial', 13), bd=7, text="sin", relief=RAISED)
Bsin.place(x=107, y=240)
Bsin.bind("<Button-1>", mathfunc)

#tan operator
Btan = Button(root, padx=10, pady=0, font=('arial', 13), bd=7, text="tan", relief=RAISED)
Btan.place(x=184, y=240)
Btan.bind("<Button-1>", mathfunc)

#log operator on base 10
Blog = Button(root, padx=10, pady=0, font=('arial', 13), bd=7, text="log", relief=RAISED)
Blog.place(x=261, y=240)
Blog.bind("<Button-1>", mathfunc)

#ln operator, which is log operator on base e (which is approx 2.718281828)
Bln = Button(root, padx=15, pady=0, font=('arial', 13), bd=7, text="ln", relief=RAISED)
Bln.place(x=338, y=240)
Bln.bind("<Button-1>", mathfunc)

#square root operator
BSQroot = Button(root, padx=18, pady=0, font=('arial', 13), bd=7, text=chr(8730), relief=RAISED)
BSQroot.place(x=415, y=240)
BSQroot.bind("<Button-1>", mathfunc)

#the inverse of tan operator
Barctan = Button(root, padx=1, pady=0, font=('arial', 13), bd=7, text="tan⁻¹", relief=RAISED)
Barctan.place(x=30, y=185)
Barctan.bind("<Button-1>", mathfunc)

#the inverse of cos operator
Barccos = Button(root, padx=0, pady=0, font=('arial', 13), bd=7, text="cos⁻¹", relief=RAISED)
Barccos.place(x=107, y=185)
Barccos.bind("<Button-1>", mathfunc)

#the inverse of sin operator
Barcsin = Button(root, padx=3, pady=0, font=('arial', 13), bd=7, text="sin⁻¹", relief=RAISED)
Barcsin.place(x=184, y=185)
Barcsin.bind("<Button-1>", mathfunc)

#the hyperbolic tan operator
Btanh = Button(root, padx=5, pady= 0, font=('arial', 13), bd=7, text="tanh", relief=RAISED)
Btanh.place(x=261, y=185)
Btanh.bind("<Button-1>", mathfunc)

#the hyperbolic cos operator
Bcosh = Button(root, padx=3, pady= 0, font=('arial', 13), bd=7, text="cosh", relief=RAISED)
Bcosh.place(x=338, y=185)
Btanh.bind("<Button-1>", mathfunc)

#the hyperbolic sin operator
Bsinh = Button(root, padx=8, pady= 0, font=('arial', 13), bd=7, text="sinh", relief=RAISED)
Bsinh.place(x=415, y=185)
Btanh.bind("<Button-1>", mathfunc)

#the square operator
Bpow = Button(root, padx=14, pady=0, font=('arial', 13), bd=7, text="x²", relief=RAISED)
Bpow.place(x=107, y=130)
Bpow.bind("<Button-1>", mathfunc)

#this button chooses which mode the operators cos, sin, tan, arccos, arcsin, arctan will work on. the choices are:
#rad (radians), deg (degrees), gra (gradients)
Bmode = Button(root, padx=7, pady=0, font=('arial', 13), bd=7, text="rad", relief=RAISED)
Bmode.place(x=30, y=130)
Bmode.bind("<Button-1>", modechange)

#this button represent the pi number (approx 3.141592653589)
Bpi = Button(root, padx=15, pady=0, font=('arial', 13), bd=7, text="π", relief=RAISED)
Bpi.place(x=338, y=130)
Bpi.bind("<Button-1>", concat)

#this button represent the e number (approx 2.718281828)
Be = Button(root, padx=18, pady=0, font=('arial', 13), bd=7, text="e", relief=RAISED)
Be.place(x=415, y=130)
Be.bind("<Button-1>", concat)

root.mainloop()
