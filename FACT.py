from math import factorial
from tkinter import *
from tkinter import IntVar
from tkinter import StringVar
from tkinter import END
import sys

root = Tk()
root.geometry('400x410')
root.title('Find Factorial')
root.iconbitmap('think.ico')
root.resizable(0,1)

# Function to call if the length of factorial exceed 34 characters
def lenchecker(val, lineLength):
    strval = str(val)
    if len(strval) <= lineLength:
        return strval
    # elif strval[34] != ' ':
    #     return insertNewlines(text[:], lineLength + 1)
    else:
        return strval[:lineLength] + '-' + '\n' + lenchecker(strval[lineLength + 1:], lineLength)

def fact(n):
    global flabel 
    try:
        try:
            if n.get() == '' or n.get().isspace():
                raise Exception
            else:
                pass
        except:
            flabel = Label(outframe, text='Nothing entered.',bg='#121212',fg='white', font=('Montserrat', 9,))
            flabel.pack(pady=5)
            entry_no.delete(0,END)
            sys.exit(1)

        if n.get() != '':
            n = int(n.get())
            if n <= -1:
                flabel = Label(outframe, text='Factorial of negative does not exist.',bg='#121212',fg='white', font=('Montserrat', 9,))
                flabel.pack(pady=5)
                entry_no.delete(0,END)
            
            elif n >= 0:
                # f = factorial(n)         using factorial (buitl in ) in math module
                # OR
                f = 1
                for i in range(1, n+1):
                    f = f * i

                if len(str(f)) > 34:
                    ft = lenchecker(f, 34)
                    flabel = Label(outframe, text='Factorial of  ' + str(n) + '  is  ' + str(ft),bg='#121212',fg='white', font=('Montserrat', 9,))
                    flabel.pack(anchor='center', side='top', pady=5)
                    entry_no.delete(0,END)
                else:        
                    flabel = Label(outframe, text='Factorial of  ' + str(n) + '  is  ' + str(f),bg='#121212',fg='white', font=('Montserrat', 9,))
                    flabel.pack(anchor='center', side='top', pady=5)
                    entry_no.delete(0,END)

        else:
            pass
    except :
        if n.get() == '':
            pass
        else:
            flabel = Label(outframe, text='Please enter only numbers.',bg='#121212',fg='white', font=('Montserrat', 9,))
            flabel.pack(anchor='center', side='top', pady=5)
            entry_no.delete(0,END)

def clearhs():
    global flabel
    flabel.pack_forget()

def clearall():
   for widgets in outframe.winfo_children():
      widgets.destroy()

#2069e0
inframe = LabelFrame(root, bg='#2069e0')
outframe = LabelFrame(root, bg='#121212', height=250)
opframe = Frame(root, bg='black', height=250)

inframe.pack(fill='both', expand=1)
inframe.propagate(0)
outframe.pack(fill='both', expand=1)
outframe.pack_propagate(0)
opframe.pack(fill='both', expand=1)

nmbr = StringVar()
nmbr.get()
msg = Label(inframe, text='Enter No to find its factorial: ', bg='#2069e0', fg='white')
entry_no = Entry(inframe, justify='center', textvariable=nmbr)

# flabel = Label(outframe)

print(nmbr.get())
#27C4F0
btn = Button(inframe, text='Find!',bg='#00627D',fg='white',relief='ridge', command=lambda:fact(nmbr))
msg.grid(row=0, column=0, padx=(50,0), pady=(15,10))
entry_no.grid(row=0, column=1, padx=(10,60), pady=(15,10))
btn.grid(row=1, column=0, columnspan=4, ipadx=30, pady=(5,15))

qut = Button(opframe, text='  Quit  ', bg='red', fg='white',relief='flat', command=root.destroy)
qut.pack(side='left', padx=30, pady=20)

clrall = Button(opframe, text=' Clear All ', bg='#2DA512', fg='white',relief='flat', command=clearall)
clrall.pack(side='right', padx=(10,30), pady=20)

clr =Button(opframe, text='Clear Last ', bg='#2DA512', fg='white',relief='flat', command=clearhs)
clr.pack(side='right', padx=(10,10), pady=20)


root.mainloop()

