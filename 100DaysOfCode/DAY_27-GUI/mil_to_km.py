
from tkinter import *

window = Tk()
window.config(padx=20,pady=20)
# Functions
b_swaped = False
def calculate():
    if not b_swaped:
        miles = eval(input.get())
        km = format(miles * 1.609344,".2f")
        mil_val.config(text=km)
    else:
        kilometers = eval(input.get())
        miles = format(kilometers * 0.621371192,".2f")
        mil_val.config(text=miles)

count = 0
def swap_units():
    global count
    global b_swaped
    if count % 2 == 0:
        mil.grid(column=2,row=1)
        km.grid(column=2,row=0)
        b_swaped = True
    else:
        mil.grid(column=2,row=0)
        km.grid(column=2,row=1)
        b_swaped = False
    count+=1



# Entry
input = Entry()
input.insert(END, string=0)
input.grid(column=1,row=0)

# Labels
mil = Label(text="Miles")
mil.grid(column=2,row=0)
equality = Label(text="is equal to")
equality.grid(column=0,row=1)
mil_val = Label(text="0")
mil_val.grid(column=1,row=1)
km = Label(text="Km")
km.grid(column=2,row=1)

# Button
btn = Button(text="Calculate",command=calculate)
swap = Button(text="Swap",command=swap_units)
btn.grid(column=1,row=2)
swap.grid(column=0,row=2)


window.mainloop()
