from os import makedirs, stat
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REP=0
timer=None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timertext, text="00:00")
    tilable.config(text="Timer", fg=GREEN)
    tick.config(text="")
   

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start():
    global REP
    
    REP+=1
    work_sec=WORK_MIN*60
    short_break=SHORT_BREAK_MIN*60
    long_break=LONG_BREAK_MIN*60

    if REP % 8==0:
        countdown(long_break)
        tilable.config(text="Break",fg=RED,bg=YELLOW,font=("courier",35,"bold"))

    elif REP%2==1:
        countdown(work_sec)
        tilable.config(text="Work",fg=GREEN,bg=YELLOW,font=("courier",35,"bold"))
    else:
        countdown(short_break)
        tilable.config(text="Break",fg=PINK,bg=YELLOW,font=("courier",35,"bold"))
        

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(count): 
    countmins=math.floor(count/60)
    countsec=count%60

    
    if count<10:
        countsec=f"0{countsec}"
    elif countsec==0:
        countsec=="00"

    canvas.itemconfig(timertext, text=f"{countmins}:{countsec}")
    if count>0:
        global timer
        timer=window.after(1000,countdown,count-1)
    else:
        start()
        marks=""
        sessions=math.floor(REP/2)
        for i in range(sessions):
            marks+="✔"
        tick.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("POMODORO Counter")
window.minsize(width=400, height=400)
window.config(padx=100, pady=100,bg=YELLOW)


canvas=Canvas(width=205, height=230,bg=YELLOW, highlightthickness=0)
toamato_img=PhotoImage(file="./tomato.png")
canvas.create_image(103,116,image=toamato_img)
timertext=canvas.create_text(103,145,text="00:00", font=(FONT_NAME,25,"bold"),fill="white")
canvas.grid(column=1,row=1)
# countdown(6) 

tilable=Label(text="Timer",fg=GREEN,bg=YELLOW,font=("courier",35,"bold"))
tilable.grid(column=1,row=0)

startbutton=Button(text="Start",fg="black",font=("Ariel",16,"normal"),command=start,highlightthickness=0)
startbutton.grid(column=0,row=2)

resetbutton=Button(text="Reset",fg="black",font=("Ariel",16,"normal"),command=reset, highlightthickness=0)
resetbutton.grid(column=2, row=2)

tick=Label(fg=GREEN,bg=YELLOW,font=("Ariel",30,"normal"))
tick.grid(column=1, row=4)

window.mainloop()