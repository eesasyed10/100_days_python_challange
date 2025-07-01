import turtle

t = turtle.Turtle()
t.pensize(5)
t.speed(1)

# 1. Move turtle to center-left
t.penup()
t.goto(-100, 0)  # Go to the left side of the screen
t.pendown()

# 2. Draw letter N
t.left(90)
t.forward(100)
t.right(135)
t.forward(140)
t.left(135)
t.forward(100)

# 3. Move to the right with some space
t.penup()
t.right(90)
t.forward(50)  # space between N and I
t.pendown()

# 4. Draw letter I
t.left(90)
t.forward(100)

turtle.done()