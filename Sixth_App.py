#Reeborg.ca/  reeborgs world game with instructions
# Functions
#Instructions fro Reeborgs World Game
# Escape the maze
'''
def turn_right():
    turn_left()
    turn_left()
    turn_left()
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
'''

#Hurdle 1 Challenge Reeborg
'''
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def rotation():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
for step in range(6):
    rotation()
'''

#Draw Square
'''
def turn_right():
    turn_left()
    turn_left()
    turn_left()
turn_left()
move()
turn_right()
move()
turn_right()
move()turn_right()
move()
'''
#Function basic
'''
def my_function():
    print("Hello, World!")
my_function()
print("Sixth App")
'''

#While loops

'''
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def rotation():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
while not at_goal():  // or while at_goal() == False or while at_goal() != True
    rotation()
'''

'''
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def rotation():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    move()
while not at_goal(): 
    if wall_in_front():
        rotation()
    else:
        move()if wall_in_front():
            rotation()
        else:
            move()
'''