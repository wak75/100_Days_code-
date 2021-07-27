from turtle import Turtle, Screen, back, color
import random
import turtle


tim = Turtle()
tim.color("red")
tim.shape("turtle")

'''for i in range(4):
    tim.forward(100)
    tim.right(90)
'''

'''for i in range(10):
    tim.pendown()
    tim.forward(10)
    tim.penup()
    tim.forward(10)
'''
#colors = ["red", "blue","green","orange","black","purple","grey","pink","violet"]

#print(ccolor)
'''for i in range(3,10):    
    angle=360/i;
    ccolor=random.choice(colors)
    tim.color(ccolor)
    for j in range(i):
        tim.forward(50)
        tim.right(angle)
        tim.forward(50)
'''

#randaom walk
turtle.colormode(255)
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color =(r,g,b)
    return random_color

'''
angle=[0,90,180,270]
tim.pensize(4)
tim.speed(10)




for i in range(200):
    ccolor=random.choice(colors)
    tim.color(random_color())
    tim.forward(10)
    tim.setheading(random.choice(angle))
    #tim.right
    tim.forward(10)'''
tim.speed(15)
tim.pensize(5)
for i in range(40):
    tim.color(random_color())
    tim.circle(100)
    current=tim.heading()
    tim.setheading(current+10)

screen= Screen()
screen.exitonclick()