#Default
#Harsh Tripathi
Aero = ['c', 'C', 'cls', 'CLS', 'del', 'DEL', 'delete', 'DELETE']
Array1 = ''
ArrayArithz = ['.', '+', '-', '*', '/']
import datetime as dt
def nowdt():
    date = dt.datetime.now()
    nowdate = date.strftime("%I.%M %p %d.%m.%Y")
    return nowdate
import mysql.connector as MyCon
MyConn = MyCon.connect(user= 'root', host= 'localhost', passwd= 'Aarsh')
MyCurr = MyConn.cursor()
MyCurr.execute('Show Databases')
MyFetch = MyCurr.fetchall()
if ('mycalc',) in MyFetch:
    print('Already..!')
    MyCurr.execute('Use MyCalc')
    pass
else:
    MyCurr.execute('Create Database MyCalc')
    MyCurr.execute('Use MyCalc')
    MyCurr.execute('Create Table MyCalc(Id int not null auto_increment primary key, Equation varchar(56), Solutions varchar(56), DateTimes varchar(69));')
Aspect = str(input('What UI You Want To Use CLI Or GUI..?\nI\'ll Use.: '))
NumbList = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

def Array1z(a):
    global Array1
    Array1 = Array1 + a
    Ans.config(text=Array1)

def Array1Keyz(event):
    global Array1
    if event.char in Aero or event.keysym == 'Delete':
        Array1 = ''
        Ans.config(text=Array1)
    elif event.char in ['=', '\r']:
        FEval('a')
    elif event.char == '\x08' or event.keysym == 'Delete':
        Array1 = Array1[:-1]
        Ans.config(text=Array1)
    elif event.keysym.isdigit() or event.char in ArrayArithz:
        Array1 = Array1 + event.char
        Ans.config(text=Array1)

def FSnap(c):
    global Array1
    Array1 = ''
    Ans.config(text='')

def FEval(e):
    global Array1
    global MyCurr
    if len(Array1) == 0:
        Ans.config(text=Array1)
    elif len(Array1) == 1:
        if Array1 == '0':
            Array1 = ''
        Ans.config(text=Array1)
    elif Array1 == '0.0' or '0'*len(Array1) in Array1:
            Array1 = '0'
            Ans.config(text=Array1)
    else:
        BEval('p')
        if Array1[-2:] == '/0':
            Array1 = 'Infinite'
            Ans.config(text=Array1); Array1 = ''
        elif Array1[-1] in ['+', '-', '*', '/']:
            Array1 = Array1 + Array1[:-1]
            Array2 = Array1; Array1 = str(eval(Array1))
            Ans.config(text=Array1)
            MyCurr.execute("Insert Into MyCalc(Equation, Solutions, DateTimes)\nValues('%s', '%s', '%s');" %(Array2, Array1, nowdt()))
        elif Array1 != '+ - * ** / % //':
            Array2 = Array1
            Array1 = str(eval(Array1))
            Ans.config(text=Array1); Array1 = Array1
            MyCurr.execute("Insert Into MyCalc(Equation, Solutions, DateTimes)\nValues('%s', '%s', '%s');" %(Array2, Array1, nowdt()))

def BEval(p):
    global Array1
    if len(Array1) == 0:
        Array1 = ''
    for i in Array1:
        if len(Array1) < 1:
            break
        if Array1[0] == '0' and Array1[1] in NumbList:
            Array1 = Array1[1:]
    for u in Array1:
        if len(Array1) < 1:
            Array1 = ''
            break
        if u in ['+', '-', '*', '/']:
            Aindex = Array1.index(u)
            for v in Array1:
                if len(Array1[Aindex:]) > 2:
                    if Array1[Aindex + 1] == '0' and Array1[Aindex + 2] in NumbList:
                        Array1 = Array1[:Aindex + 1] + Array1[Aindex + 2:]
                    else:
                        break        

if  Aspect in ['cli', 'CLI']:
    #Harsh Tripathi
    a1, a2, a4, a8, n1, n2 = 2, 4, 8, 16, None, None
    while True:
        #Input At Run
        if n1 == None or n1 in Aero:
            n1 = input('First Number.: ')
        else:
            print('First Number.: ', n1)
        if(str(n1) in Aero):
            continue
        n2 = input('Second Number.: ')
        if(str(n2) in Aero):
            n1 = None
            continue
        
        #Asking For Operator
        n1, n2 = float(n1), float(n2)
        print('You Can Use [ + - * / ^ ! ]')
        n4 = str(input('Arithmetic Operation To Perform.: '))

        #Addition
        if(n4 == '+'):
            a1 = n1 + n2; n1 = a1
            print('The Addition Is.: ', a1, '\n')

        #Subtraction
        elif(n4 == '-'):
            a2 = n1 - n2; n1 = a2
            print('The Difference Is.: ', a2, '\n')

        #Multiplication
        elif(n4 == '*'):
            a4 = n1 * n2; n1 = a4
            print('The Multiplication Is.: ', a4, '\n')

        #Division Or Quotient
        elif(n4 == '/'):
            a8 = n1 / n2; n1 = a8
            print('The Quotient Is.: ', a8, '\n')

        #Number Times Itself
        elif(n4 == '^'):
            a5 = n1 ** n2; n1 = a5
            print('The Exponent Form Is.: ', a5, '\n')

        #Finding Square Root
        elif(n4 == '!' and n2 == 2):
            n1 = int(n1)
            for r1 in range(1, n1, 1):
                if(n1 / r1 / r1 == 1):
                    n1 = r1
                    print('The Square Root Is.: ', r1, '\n')

        #Finding Cube Root Of Number
        elif(n4 == '!' and n2 == 3):
            n1 = int(n1)
            for r2 in range(1, n1, 1):
                if(n1 / r2 / r2 / r2 == 1):
                    n1 = r2
                    print('The Cube Root Is.: ', r2, '\n')
        
        #Telling User To Insert Valid Input
        else:
            print('Provide A Arithmetic Operation. Next Time..!')
else:
    #Window Default
    fgc = '#000000'
    bgc = '#b2cdb2'
    from tkinter import *
    font1 = ('Ink Free', 22, 'bold')

    #Window Main
    tk = Tk()

    #Window Style
    tk.title('Az I Calc..!')
    tk.geometry('369x496')
    tk.config(bg='#b2cdb2')
    #'296x469' #'369x496' #'496x669' #'696x869'

    #Window Arrey
    Ans = Label(tk, fg=fgc, bg=bgc, text=Array1)
    tk.bind('<KeyPress>', Array1Keyz)
    Ans.place(relx=0, rely=0, relwidth=1, relheight=0.20)
    Ans.config(font=font1)

    #Windows Active
    But1 = Button(tk, text='1', fg=fgc, bg=bgc, command=lambda: Array1z('1'))
    But1.place(relx=0, rely=0.20, relwidth=0.25, relheight=0.20)
    But1.config(font=font1)

    But2 = Button(tk, text='2', fg=fgc, bg=bgc, command=lambda: Array1z('2'))
    But2.place(relx=0.25, rely=0.20, relwidth=0.25, relheight=0.20)
    But2.config(font=font1)

    But4 = Button(tk, text='3', fg=fgc, bg=bgc, command=lambda: Array1z('3'))
    But4.place(relx=0.50, rely=0.20, relwidth=0.25, relheight=0.20)
    But4.config(font=font1)

    But8 = Button(tk, text='+', fg=fgc, bg=bgc, command=lambda: Array1z('+'))
    But8.place(relx=0.75, rely=0.20, relwidth=0.25, relheight=0.20)
    But8.config(font=font1)

    But16 = Button(tk, text='4', fg=fgc, bg=bgc, command=lambda: Array1z('4'))
    But16.place(relx=0, rely=0.40, relwidth=0.25, relheight=0.20)
    But16.config(font=font1)

    But32 = Button(tk, text='5', fg=fgc, bg=bgc, command=lambda: Array1z('5'))
    But32.place(relx=0.25, rely=0.40, relwidth=0.25, relheight=0.20)
    But32.config(font=font1)

    But64 = Button(tk, text='6', fg=fgc, bg=bgc, command=lambda: Array1z('6'))
    But64.place(relx=0.50, rely=0.40, relwidth=0.25, relheight=0.20)
    But64.config(font=font1)

    But128 = Button(tk, text='-', fg=fgc, bg=bgc, command=lambda: Array1z('-'))
    But128.place(relx=0.75, rely=0.40, relwidth=0.25, relheight=0.20)
    But128.config(font=font1)

    But256 = Button(tk, text='7', fg=fgc, bg=bgc, command=lambda: Array1z('7'))
    But256.place(relx=0, rely=0.60, relwidth=0.25, relheight=0.20)
    But256.config(font=font1)

    But512 = Button(tk, text='8', fg=fgc, bg=bgc, command=lambda: Array1z('8'))
    But512.place(relx=0.25, rely=0.60, relwidth=0.25, relheight=0.20)
    But512.config(font=font1)

    But1024 = Button(tk, text='9', fg=fgc, bg=bgc, command=lambda: Array1z('9'))
    But1024.place(relx=0.50, rely=0.60, relwidth=0.25, relheight=0.20)
    But1024.config(font=font1)

    But2048 = Button(tk, text='*', fg=fgc, bg=bgc, command=lambda: Array1z('*'))
    But2048.place(relx=0.75, rely=0.60, relwidth=0.25, relheight=0.20)
    But2048.config(font=font1)

    But4096 = Button(tk, text='C', fg=fgc, bg=bgc, command=lambda: FSnap('C'))
    But4096.place(relx=0, rely=0.80, relwidth=0.25, relheight=0.20)
    But4096.config(font=font1)

    But8192 = Button(tk, text='0', fg=fgc, bg=bgc, command=lambda: Array1z('0'))
    But8192.place(relx=0.25, rely=0.80, relwidth=0.25, relheight=0.20)
    But8192.config(font=font1)

    But16384 = Button(tk, text='=', fg=fgc, bg=bgc, command=lambda: FEval('='))
    But16384.place(relx=0.50, rely=0.80, relwidth=0.25, relheight=0.20)
    But16384.config(font=font1)

    But32768 = Button(tk, text='/', fg=fgc, bg=bgc, command=lambda: Array1z('/'))
    But32768.place(relx=0.75, rely=0.80, relwidth=0.25, relheight=0.20)
    But32768.config(font=font1)


    #Window Static
    tk.mainloop()
    MyConn.commit()

#I Am Harsh The Solo Person In Programming This..!
