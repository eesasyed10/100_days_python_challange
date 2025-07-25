from turtle import Turtle,Screen,colormode
"""draw random coloured lines"""
# colors = [
#     "red",
#     "blue",
#     "green",
#     "yellow",
#     "orange",
#     "purple",
#     "pink",
#     "cyan",
#     "magenta",
#     "brown",
#     "black",
#     "gray",
#     "lightblue",
#     "gold",
#     "violet",
#     "navy"
# ]
import random

direction=[0,90,180,270]

timmy=Turtle()
colormode(255)
def pick_color():
    r=random.randint(1,255)
    g=random.randint(1,255)
    b=random.randint(1,255)
    return (r,g,b)
     


timmy.speed("fastest")
timmy.pensize(15)
for _ in range(200):
    timmy.color(pick_color())
    timmy.forward(30)
    timmy.setheading(random.choice(direction))



screen=Screen()
screen.exitonclick()