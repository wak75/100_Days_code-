from turtle import Turtle, Screen
import random


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
colors = ["red", "blue","greem","orange","black","purple","grey","pink","violet"]
ccolor=random.choice(colors)
#print(ccolor)
for i in range(4,10):
    tim.color(ccolor)
    angle=360%i
    for j in range(i):
        tim.forward(10)
        tim.right(angle)
        tim.forward(10)



screen= Screen()
screen.exitonclick()