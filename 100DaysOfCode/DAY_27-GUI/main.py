from tkinter import *

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500,height=300)
window.config(padx=100,pady=200)

# Label
my_label = Label(text="I Am a Label", font=("Arial",24,"bold"))
#my_label.pack()
#my_label.place(x=0,y=0)
my_label.grid(column=0,row=0)
my_label.config(padx=50,pady=50)


# Button

def button_clicked():
    print("I got Clicked!")
    #my_label.config(text=input.get())


btn = Button(text="Click Me!",command=button_clicked)
new_btn = Button(text="New Button",command=button_clicked)
#btn.pack()
btn.grid(column=1,row=1)
new_btn.grid(column=2,row=0)

# Entry

input = Entry(width=10)
#input.pack()
input.grid(column=3,row=2)

# Keep a window open
window.mainloop()