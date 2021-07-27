
from tkinter import *

window=Tk()
window.minsize(300,150)
window.title("Distance convertor")
window.config(padx=25, pady=25)



user_input=Entry(width=25)
user_input.grid(column=1,row=0)


lable1=Label(text="miles", font=("ariel",12,"normal"))
lable1.grid(column=3,row=0)
lable1.config(padx=10)

lable2=Label(text="is equal to", font=("ariel",12,"normal"))
lable2.grid(column=0,row=1)


lable3=Label(text="0",font=("ariel",12,"normal"))
lable3.grid(column=1,row=1)


lable4=Label(text='km',font=(("ariel",12,"normal")))
lable4.grid(column=2,row=1)

def convert():    
    miles=float(user_input.get())
    ans=miles*1.6
    lable3.config(text=f"{ans}")


button=Button(text="Convert",command=convert)
button.grid(column=1,row=2)









window.mainloop()