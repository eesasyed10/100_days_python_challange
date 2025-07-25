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

def pick_color():
    colormode(255)
    r=random.randint(1,255)
    g=random.randint(1,255)
    b=random.randint(1,255)
    return (r,g,b)


# timmy.pensize(5)
def spirograph(size_of_gap):
    timmy.speed("fastest")
    for _ in range(int(360/ size_of_gap )):
        timmy.color(pick_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)



# a =int(input("what should be the gap between the circles: "))
spirograph(1)

screen=Screen()
screen.exitonclick()