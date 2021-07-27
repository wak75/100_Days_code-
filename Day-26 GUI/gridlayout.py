from tkinter import *

window=Tk()
window.minsize(600,600)
window.title("This is demonstration of a grid layout")
window.config(padx=30, pady=30)


lable1=Label(text="label text", font=("algerian",20,"bold"))
lable1.grid(column=0,row=0)
lable1.config(padx=10, pady=10)

button1=Button(text="Button1")
button1.grid(column=2, row=0)
button1.config(padx=10, pady=10)

button2=Button(text="Button2")
button2.grid(column=1,row=1)
button2.config(padx=10, pady=10)

input=Entry(width=20)
input.insert(END,string="this is entry field")
input.grid(column=3, row=2)
# inputs.config(padx=10, pady=10)








window.mainloop()