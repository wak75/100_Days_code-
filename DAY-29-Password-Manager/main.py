import random
from tkinter import *
from tkinter import messagebox
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    password_letter=[random.choice(letters) for _ in range(nr_letters)]
    password_symbol=[random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers=[random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letter+password_symbol+password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    # for char in password_list:
    #   password += char
    passin.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def savedata():
    with open("saved_password_details", "a") as file:
        if web_input.get()=="":
            messagebox.showerror(title="error", message="'Website' filed cannot be left empty")
            web_input.focus()
        else:            
            website=web_input.get()
        
        if emailinput.get()=="":
            messagebox.showerror(title="error", message="'Email/Username' filed cannot be left empty")
            emailinput.focus()
        else:
            email=emailinput.get()
        
        if passin.get()=="":
            messagebox.showerror(title="error", message="'Password' filed cannot be left empty")
            passin.focus()
        
        else:
            password=passin.get()


        ok_or_not=messagebox.askokcancel(title="confirm??",message=f"This are the data \n" 
                                                f" Website: {website} \n Email: {email} \n Password: {password}" )
        if ok_or_not:    
            file.write( website +" | "+email +" | "+ password +"\n")
            messagebox.showinfo(title="Success", message="The data is saved sussessfully")
            emailinput.delete(0,END)
            web_input.delete(0,END)
            passin.delete(0,END)




# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.minsize(width=200,height=200)
window.config(padx=20, pady=20, )
window.title("Password Manager")

canvas=Canvas(width=200,height=200, )
logo=PhotoImage(file="./logo.png")
canvas.create_image(100,100,image=logo)
canvas.grid(column=1, row=0)

websitelabel=Label(text="Website", font=("ariel",10,"normal"))
websitelabel.grid(column=0, row=1)

emaillab=Label(text="Email/Username", font=("ariel",10,"normal"))
emaillab.grid(column=0, row=2)

passwordlab=Label(text="Password", font=("ariel",10,"normal"))
passwordlab.grid(column=0, row=3)



web_input=Entry(width=35)
web_input.grid(column=1,row=1)

emailinput=Entry(width=35)
emailinput.grid(column=1, row=2)

passin=Entry(width=21)
passin.grid(column=1,row=3)

genbutt=Button(text="Generate password",font=("ariel",10,"normal"), command=password_gen)
genbutt.grid(column=2, row=3)

addbutt= Button(text="Add", font=("ariel",10,"normal"), width=36, command=savedata)
addbutt.grid(column=1, row=4)

window.mainloop()