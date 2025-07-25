from turtle import Turtle,Screen
"""draw shapes"""
timmy=Turtle()
timmy.right(90)
timmy.penup()
timmy.forward(200)
timmy.left(90)
timmy.pendown()
def draw_shape(unum):
    new_n=360/ unum
    for t in range(unum):
        timmy.forward(100)
        timmy.left(new_n)

for bb in range(3,11):
    draw_shape(bb)

# timmy.shape("circle")

screen=Screen()
screen.exitonclick()