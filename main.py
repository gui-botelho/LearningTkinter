# Attempt at calculator program in TKinter
from tkinter import *

root = Tk()
root.title('Calculator')
display = Entry(width=50)
screen_text = ''
display.insert(0, screen_text)
body = Frame(root)


def clear_display():
    display.delete(0, END)


def func(number):
    global screen_text
    current_text = display.get()
    display.delete(0, END)
    display.insert(0, str(current_text) + str(number))


def result():
    insertion = str(display.get())
    separation = insertion.split(' ')
    print(separation)
    while len(separation) > 1:
        if 'x' in separation:
            while 'x' in separation:
                mult = float(separation[separation.index('x') - 1]) * float(separation[separation.index('x') + 1])
                print(separation)
                separation.pop(separation.index('x') - 1)
                print(separation)
                separation.pop(separation.index('x') + 1)
                print(separation)
                separation[separation.index('x')] = mult

        if '/' in separation:
            while '/' in separation:
                division = float(separation[separation.index('/') - 1]) / float(separation[separation.index('/') + 1])
                print(separation)
                separation.pop(separation.index('/') - 1)
                print(separation)
                separation.pop(separation.index('/') + 1)
                print(separation)
                separation[separation.index('/')] = division

        if '-' in separation:
            while '-' in separation:
                subbing = float(separation[separation.index('-') - 1]) - float(separation[separation.index('-') + 1])
                print(separation)
                separation.pop(separation.index('-') - 1)
                print(separation)
                separation.pop(separation.index('-') + 1)
                print(separation)
                separation[separation.index('-')] = subbing

        if '+' in separation:
            while '+' in separation:
                adding = float(separation[separation.index('+') - 1]) + float(separation[separation.index('+') + 1])
                print(separation)
                separation.pop(separation.index('+') - 1)
                print(separation)
                separation.pop(separation.index('+') + 1)
                print(separation)
                separation[separation.index('+')] = adding

    display.delete(0, END)
    display.insert(0, str(separation[0]))


button0 = Button(text='0', width=10, height=5, command=lambda: func('0'))
button1 = Button(text='1', width=10, height=5, command=lambda: func('1'))
button2 = Button(text='2', width=10, height=5, command=lambda: func('2'))
button3 = Button(text='3', width=10, height=5, command=lambda: func('3'))
button4 = Button(text='4', width=10, height=5, command=lambda: func('4'))
button5 = Button(text='5', width=10, height=5, command=lambda: func('5'))
button6 = Button(text='6', width=10, height=5, command=lambda: func('6'))
button7 = Button(text='7', width=10, height=5, command=lambda: func('7'))
button8 = Button(text='8', width=10, height=5, command=lambda: func('8'))
button9 = Button(text='9', width=10, height=5, command=lambda: func('9'))
buttonplus = Button(text='+', width=10, height=5, command=lambda: func(' + '))
buttonminus = Button(text='-', width=10, height=5, command=lambda: func(' - '))
buttonmult = Button(text='x', width=10, height=5, command=lambda: func(' x '))
buttondiv = Button(text='/', width=10, height=5, command=lambda: func(' / '))
buttonequal = Button(text='=', width=10, height=5, command=result)
buttonclear = Button(text='Clear', width=45, height=5, command=clear_display)
buttondot = Button(text='.', width=10, height=5, command=lambda: func('.'))

display.grid(row=0, column=0, columnspan=5)

buttondiv.grid(row=4, column=4)
buttonmult.grid(row=3, column=4)
buttonminus.grid(row=2, column=4)
buttonplus.grid(row=1, column=4)
button0.grid(row=4, column=0)
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)
buttondot.grid(row=4, column=1)
buttonequal.grid(row=4, column=2)
buttonclear.grid(row=5, column=0, columnspan=5)

root.mainloop()
