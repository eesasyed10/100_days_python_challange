def right():
    turn_left()
    turn_left()
    turn_left()




def jump():
    turn_left()
    move()
    while wall_on_right()==True:
        if front_is_clear()==True:
            move()
        else:
            right()
        
        
    right()
    move()
    right()
    move()
    while not wall_in_front():
        if front_is_clear()==True:
            move()
        else:
            turn_left()

while not at_goal():
    if front_is_clear():
        move()

    elif wall_in_front():
        jump()