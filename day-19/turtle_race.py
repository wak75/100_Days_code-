from turtle import Turtle, Screen, color, pencolor, screensize
import random
import turtle

is_game_on=False
screen=Screen()
screen.setup(width=500,height=500)
bet=screen.textinput(prompt="Who will win", title="Enter the color")

color=["violet","indigo","brown","green","yellow","orange","red"]
'''x=-220
y=-180
violet=Turtle(shape="turtle")
violet.color(color[0])
violet.penup()
violet.goto(x,y)


indigo=Turtle(shape="turtle")
indigo.color(color[1])
indigo.penup()
indigo.goto(x,y+50)

brown=Turtle(shape="turtle")
brown.color(color[2])
brown.penup()
brown.goto(x,y+100)

green=Turtle(shape="turtle")
green.color(color[3])
green.penup()
green.goto(x,y+150)

yellow=Turtle(shape="turtle")
yellow.color(color[4])
yellow.penup()
yellow.goto(x,y+200)


orange=Turtle(shape="turtle")
orange.color(color[5])
orange.penup()
orange.goto(x,y+250)


red=Turtle(shape="turtle")
red.color(color[6])
red.penup()
red.goto(x,y+300)
'''

y=[-180,-130,-80,-30,20,70,120]
all_tims=[]

for i in range(7):
    tim=Turtle(shape="turtle")
    tim.penup()
    tim.color(color[i])
    tim.goto(-230,y[i])
    all_tims.append(tim)

if bet:
    is_game_on=True

while is_game_on:
    for i in all_tims:
        if i.xcor()>230:
            is_game_on=False
            winning_col=i.pencolor()
            if winning_col==bet:
                print(f"congrats you win, {winning_col} is the winner")
            else:
                print(f"sorry you loose, {winning_col} is the winner")
        dist=random.randint(0,10)
        i.forward(dist)
screen.exitonclick()
