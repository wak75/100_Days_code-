from tkinter import *

window=Tk()
window.title("this is GUI")
window.minsize(600,600)


lable1=Label(text="This is label baby",font=("algerian",20,"normal"))
lable1.pack()

def button_clicked():
    lable1["text"]=input.get()

button=Button(text="click me", command=button_clicked)
button.pack()


input=Entry()
input.insert(END,string="Apna time aayega")
input.pack()


text=Text(height=5, width=30)
text.focus()
text.insert(END,"I am the king")
print(text.get("1.0",END))
text.pack()



def used_spinbox():
    print(spinbox.get())


spinbox=Spinbox(from_=0, to=10,width=5, command=used_spinbox)
spinbox.pack()


def scale_used(value):
    print(value)

scale=Scale(from_=10,to=100, command=scale_used)
scale.pack()


def checkbox_used():
    print(checked_state.get())

checked_state=IntVar()
chedckbutton=Checkbutton(text="checkbutton 1",variable=checked_state, command=checkbox_used)
checked_state.get()
chedckbutton.pack()


def radio_used():
    print(radio_state.get())

radio_state=IntVar()
radiobutton1=Radiobutton(text="option 1", value=1, variable=radio_state, command=radio_used)
radiobutton2=Radiobutton(text="Option 2", value=2, variable=radio_state,command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


def listbox_used(event):
    print(listbox.get(listbox.curselection()))


listbox=Listbox(height=4)
fruits=["apple","mango","guava","pineapple","grapes"]
for item in fruits:
    listbox.insert(fruits.index(item),item)
listbox.bind("<<listboxselect>>",listbox_used)
listbox.pack()

window.mainloop()