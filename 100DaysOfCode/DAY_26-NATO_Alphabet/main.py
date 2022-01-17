from dataclasses import dataclass
import pandas
from tkinter import *

window = Tk()
window.title("NATO - Alphabet")
window.config(padx=20,pady=20,)
window.minsize(width=400,height=200)

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data)
nato_dict = {row.letter: row.code for index, row in data.iterrows()}
# print(nato_dict)




#user_input = input("Enter a word: ")
user_input = Entry()
user_input.insert(END,string="Example")
data_label = Label(text="Here will appear NATO alphabet")

def nato():
    b_success = True
    new_list = []
    for j,i in enumerate(user_input.get()):
        try:
            new_list.append(nato_dict[i.upper()])
        except KeyError:
            print("Sorry, only letters in the alphabet please.")
            data_label.config(text="Sorry, only letters in the alphabet please.")
            b_success = False
        else:
            if j != len(user_input.get())-1:
                new_list.append("-")
        """finally:
            if i == " ":
                b_success = True
        """
    if b_success:
        print(new_list)
        data_label.config(text=new_list)

btn = Button(text="Convert",command=nato)
user_input.pack()
data_label.pack()
btn.pack()

window.mainloop()