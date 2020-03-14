from tkinter import *


def btnClick (numbers):
    global operator
    operator=operator+str(numbers)
    text_Input.set(operator)


def btnClearDisplay():
    global operator
    operator = ""
    text_Input.set("")


def btnEqualsInput():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=""


root = Tk()
root.maxsize(200,230)
root.minsize(200,230)
text_Input = StringVar()
operator = ""
txtDisplay = Entry(root, textvariable=text_Input, bd=20)
txtDisplay.pack()
topFrame = Frame(root)
topFrame.pack()
mid1Frame = Frame(root)
mid1Frame.pack()
mid2Frame = Frame(root)
mid2Frame.pack()
bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)
button1 = Button(topFrame, padx=15, pady=10, command=lambda:btnClick(7), text="7")
button1.pack(side=LEFT)
button2 = Button(topFrame, padx=15, pady=10, command=lambda:btnClick(8), text="8")
button2.pack(side=LEFT)
button3 = Button(topFrame, padx=15, pady=10, command=lambda:btnClick(9), text="9")
button3.pack(side=LEFT)
button4 = Button(topFrame, padx=15, pady=10, command=lambda:btnClick("/"), text="/")
button4.pack(side=LEFT)
button5 = Button(mid1Frame, padx=15, pady=10, command=lambda:btnClick(4), text="4")
button5.pack(side=LEFT)
button6 = Button(mid1Frame, padx=15, pady=10, command=lambda:btnClick(5), text="5")
button6.pack(side=LEFT)
button7 = Button(mid1Frame, padx=15, pady=10, command=lambda:btnClick(6), text="6")
button7.pack(side=LEFT)
button8 = Button(mid1Frame, padx=15, pady=10, command=lambda:btnClick("*"), text="*")
button8.pack(side=LEFT)
button9 = Button(mid2Frame, padx=15, pady=10, command=lambda:btnClick(1), text="1")
button9.pack(side=LEFT)
button10 = Button(mid2Frame, padx=15, pady=10, command=lambda:btnClick(2), text="2")
button10.pack(side=LEFT)
button11 = Button(mid2Frame, padx=15, pady=10, command=lambda:btnClick(3), text="3")
button11.pack(side=LEFT)
button12 = Button(mid2Frame, padx=15, pady=10, command=lambda:btnClick("-"), text="-")
button12.pack(side=LEFT)
button13 = Button(bottomframe, padx=15, pady=10, command=btnClearDisplay, text="c")
button13.pack(side=LEFT)
button14 = Button(bottomframe, padx=15, pady=10, command=lambda:btnClick(0), text="0")
button14.pack(side=LEFT)
button15 = Button(bottomframe, padx=14, pady=10, command=btnEqualsInput, text="=")
button15.pack(side=LEFT)
button16 = Button(bottomframe, padx=13, pady=10, command=lambda:btnClick("+"),text="+")
button16.pack(side=LEFT)

root.mainloop()

