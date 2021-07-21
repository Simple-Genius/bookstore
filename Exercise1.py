from tkinter import *

shape = Tk()

def kg_to_g():
    grams = float(e1_value.get()) * 1000
    t2.insert(END, grams)

def kg_to_pounds():
    pounds = float(e1_value.get()) * 2.20462
    t3.insert(END, pounds)

def kg_to_ounces():
    ounces = float(e1_value.get()) * 35.274
    t4.insert(END, ounces)

b1 = Button(shape, text = "convert", command = lambda:[kg_to_g(), kg_to_ounces(), kg_to_pounds()])
b1.grid(row = 0, column = 1)

e1_value = StringVar()
e1 = Entry(shape, textvariable = e1_value)
e1.grid(row = 1, column = 1)

t2 = Text(shape, height = 1, width = 30)
t2.grid(row = 1, column = 4)

t3 = Text(shape, height = 1, width = 30)
t3.grid(row = 2, column = 4)

t4 = Text(shape, height = 1, width = 30)
t4.grid(row = 3, column = 4)

l1 = Label(shape, text = "  =")
l1.grid(row =1, column = 3)

l2 = Label(shape, text = "  =")
l2.grid(row = 2, column = 3)

l3 = Label(shape, text = "  =")
l3.grid(row = 3, column = 3)

l4 = Label(shape, text = "kg")
l4.grid(row = 1, column = 2)

l5 = Label(shape, text = "grams")
l5.grid(row = 1, column = 5)

l6 = Label(shape, text = "ounces")
l6.grid(row = 2, column = 5)

l7 = Label(shape, text = "pounds")
l7.grid(row = 3, column = 5)

shape = mainloop()
