from turtle import Turtle,Screen
"""draw an alternating line"""
timmy=Turtle()
for t in range(20):
    timmy.forward(5)
    timmy.penup()
    timmy.forward(5)
    timmy.pendown()

# timmy.shape("circle")

screen=Screen()
screen.exitonclick()