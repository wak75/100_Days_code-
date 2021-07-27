# from turtle import Turtle,Screen

# timmy= Turtle();
# timmy.color("red")
# timmy.shape("turtle")
# timmy.forward(200)

# my_screen=Screen()
# my_screen.canvheight
# my_screen.exitonclick()


from prettytable import PrettyTable 

table=PrettyTable();
table.add_column("City",["kharar","Mohali","zirakpur","Baba Faraid Nagar", "BB wala chock","Amritsar","Bathinda"])
table.add_column("States",["Punjab", "Rajasthan", "West-bangal", "kashmir","kerela","Tamil Nadu","Assam"])
table.align["City"]="l"
print(table)