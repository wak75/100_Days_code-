
from turtle import Turtle,Screen

tim=Turtle()

def mv_forward():
    tim.forward(10)
def mv_backward():
    tim.backward(10)

def mv_right():
    tim.right(15)

def mv_left():
    tim.left(15)

def saaf():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screenn= Screen()
screenn.listen()

screenn.onkey(mv_forward,"w")
screenn.onkey(mv_backward,"s")
screenn.onkey(mv_right,"d")
screenn.onkey(mv_left,"a")
screenn.onkey(saaf,"c")

screenn.exitonclick()