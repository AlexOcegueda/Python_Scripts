#!/usr/bin/env python3

"""
This module contains functions related to drawing and moving a circle around the screen
"""

__author__ = 'Debbie Johnson, Alex Ocegueda'
__version__ = '2.0'
__copyright__ = "Copyright 2022.02.17, Chapter 4 Assignment"
__github__ = "https://github.com/dejohns2/CSC365_Spring2022_Code_Examples"

import random
import turtle

screen = None
user = None

hidden_x = 100  # x-coord of hidden circle
hidden_y = 100  # y-coord of hidden circle
hidden_circle_size = 50  # sets how difficult it is to find
hidden_circle_color = 'black'  # set to black to be invisible

user_circle_color = 'pink'  # user circle is default to pink until it gets hot or cold
user_circle_size = 10  # sets the size of the circle - this affects difficulty.
move_size = None  # number of steps taken by user
move_limit = 20  # number of steps limited before game over - set by user also.

# position where the turtle will be drawn at
# these values will change by plus/minus 20 as arrows are pressed
user_x = 0  # center of screen moving right or left
user_y = 0  # center of screen moving up or down
previous_x = 0  # previous location of user's x coord
previous_y = 0  # previous location of user's y coord


def reset_game():
    """
    Resets the entire game by calling main again and resetting the hiddle circle color.
    Returns:

    """
    global hidden_circle_color
    hidden_circle_color = 'black'
    main()


def debug():
    """
    Shows where hidden circle is at to make testing easier. Stays up forever.
    Returns: None

    """
    global hidden_circle_color
    hidden_circle_color = 'white'
    display_game()


def move_home():
    """
    Reset the x and y back to zero coordinate which will be used position the circle in the center
    then call draw_circle to clear & redraw the circle is on the screen based on its new location

    Returns:
        None
    """

    global user_x, user_y
    user_x = 0  # center of screen moving right or left
    user_y = 0  # center of screen moving up or down
    display_game()


def move_left():
    """
    Subtract 20 from the x coordinate which will be used move the circle to the left
    then call draw_circle to clear & redraw the circle is on the screen based on its new location

    Returns:
        None
    """

    global user_x
    user_x -= 20  # move to the left of center
    display_game()


def move_right():
    """
    Add 20 to the x coordinate which will be used move the circle to the right
    then call draw_circle to clear & redraw the circle is on the screen based on its new location

    Returns:
        None
    """

    global user_x
    user_x += 20  # move to the right of center
    display_game()


def move_up():
    """
    Add 20 to the y coordinate which will be used move the circle up
    then call draw_circle to clear & redraw the circle is on the screen based on its new location

    Returns:
        None
    """

    global user_y
    user_y += 20  # move top of center
    display_game()


def move_down():
    """
    Subtract 20 from y coordinate which will be used move the circle to the down
    then call draw_circle to clear & redraw the circle is on the screen based on its new location
    Returns:
        None
    """

    global user_y
    user_y -= 20  # move down of center
    display_game()


def check_hot_or_cold():
    """
    This checks the user's location compared to its previous location and
    sees which one is closer to hidden circle. Depending which one is closer
    will determine if the circle is 'hot' (red) or 'cold' (blue).

    """
    global previous_x, previous_y, user_circle_color, hidden_circle_color

    overlap = user_circle_size * 2 - 10

    if abs(user_x - hidden_x) < overlap and abs(user_y - hidden_y) < overlap:
        hidden_circle_color = 'green yellow'
        user_circle_color = 'green'
    else:
        if previous_x != user_x:
            if abs(previous_x - hidden_x) > abs(user_x - hidden_x):
                user_circle_color = 'red'
            else:
                user_circle_color = 'blue'

        if previous_y != user_y:
            if abs(previous_y - hidden_y) > abs(user_y - hidden_y):
                user_circle_color = 'red'
            else:
                user_circle_color = 'blue'

    previous_x = user_x
    previous_y = user_y


def check_move_limit():
    """
    Checks moves compared to the limit. If it has reached the cap it will display it and inform
    the user to reset the game when they are ready to play again.
    """
    global move_size

    if move_size >= move_limit:
        user.goto(-150, 325)
        user.write("CAP REACHED! Pressed R to reset!", font=("Verdana", 12, "bold"))
    else:
        move_size += 1


def setup_window():
    """
    Controls how the window looks.

    Returns:
        None
    """

    screen.tracer(False)  # turn animation off which causes screen flickering as the circle gets redrawn
    screen.title('Hot or Cold')  # title the title bar of the window
    screen.bgcolor('black')  # set the window's background color
    screen.setup(800, 900)  # the size of the window

    # set up the keys to listen to and what function should be called
    screen.onkeypress(reset_game, "r")
    screen.onkeypress(debug, "d")
    screen.onkeypress(move_home, "h")
    screen.onkeypress(move_up, "Up")
    screen.onkeypress(move_down, "Down")
    screen.onkeypress(move_right, "Right")
    screen.onkeypress(move_left, "Left")
    screen.listen()  # start listening for keys being pressed


def set_hidden_location():
    """
    Generate a random x & y location for the hidden circle based on the default screen size
    Making sure that the hidden circle isn't too close to the user's circle and
    abs(x) & abs(y) can't be within twice the user's circle size + 10
    """

    global hidden_x, hidden_y
    while True:
        hidden_x = random.randint(-420, 420)  # left & right max: -420 & 420
        hidden_y = random.randint(-300, 300)  # bottom & top max: -300 & 300

        # This checks to see if hidden circle is too close to user circle when placed
        if abs(hidden_x) > (user_circle_size * 2 + 10) and abs(hidden_y) > (user_circle_size * 2 + 10):
            break


def set_user_location():
    global user_x, user_y

    center_pos = int(user_circle_size / 2) * -1

    user_x = center_pos
    user_y = center_pos


def set_user_settings():
    global hidden_circle_size, user_circle_size, move_limit, move_size
    move_size = -1

    try:
        user_circle_size = int(turtle.numinput('Circle', 'Size of circles (10-100)'))
        hidden_circle_size = user_circle_size
    except:
        user_circle_size = 50
        hidden_circle_size = 50

    try:
        move_limit = int(turtle.numinput('Circle', 'Size of move (10-100)'))
    except:
        move_limit = 50


def draw_instructions():
    # write text on the screen
    user.penup()
    user.goto(-350, 350)  # from the current position which is center after clear, move left 350 up 350
    user.pencolor('white')  # text color
    user.write("Use arrows to move", font=("Verdana", 12, "bold"))
    user.goto(-350, 325)  # from the current position which is center after clear, move left 350 up 350
    user.write("R = Reset game", font=("Verdana", 12, "bold"))
    user.goto(-350, 300)  # from the current position which is center after clear, move left 350 up 350
    user.write("D = Debug/Show hidden", font=("Verdana", 12, "bold"))
    user.goto(-350, 275)  # from the current position which is center after clear, move left 350 up 350
    user.write("H = Return circle to center", font=("Verdana", 12, "bold"))
    user.goto(275, 350)  # from the current position which is center after clear, move left 350 up 350
    user.write("Moves: " + str(move_size), font=("Verdana", 12, "bold"))


def draw_hidden_circle():
    """
    clear the screen and draw the circle based on the x & y coordinates

    """

    user.speed('fastest')  # draw quickly

    # draw circle
    user.goto(hidden_x, hidden_y)  # move to the updated x (left-right) and y (up-down) location from center
    user.pendown()  # start drawing the outline of the circle
    user.fillcolor(hidden_circle_color)  # fill color of the circle
    user.begin_fill()  # start the fill of whatever is being drawn
    user.circle(hidden_circle_size)  # diameter of the circle
    user.end_fill()  # done drawing the object to complete the fill


def draw_user_circle():
    """
    clear the screen and draw the circle based on the x & y coordinates

    """

    user.speed('fastest')  # draw quickly

    # draw circle
    user.goto(user_x, user_y)  # move to the updated x (left-right) and y (up-down) location from center
    user.pendown()  # start drawing the outline of the circle
    user.fillcolor(user_circle_color)  # fill color of the circle
    user.begin_fill()  # start the fill of whatever is being drawn
    user.circle(user_circle_size)  # diameter of the circle
    user.end_fill()  # done drawing the object to complete the fill


def display_game():
    """
    Displays everything needed after a key was pressed by the user.

    """
    user.clear()  # clear the previous screen for the update circle location

    user.hideturtle()  # don't show the icon
    check_hot_or_cold()
    check_move_limit()
    user.pencolor('black')
    user.penup()  # avoid a trail when drawing next object
    draw_user_circle()
    user.penup()  # avoid a trail when drawing next object
    draw_hidden_circle()
    draw_instructions()
    user.penup()  # # avoid a trail when drawing next object


def main():
    """
    The main function, used to test drawing a square

    """
    set_user_settings()
    setup_window()  # configure how the turtle window screen will look like
    set_user_location()  # sets user's circle to the center based on difficulty selected
    set_hidden_location()  # displays a fresh hidden location
    display_game()  # draws everything on screen according to user input
    screen.mainloop()  # keep the turtle window open until the user closes it


# if this is the program starting module, then run the main function
if __name__ == '__main__':
    screen = turtle.Screen()
    user = turtle.Turtle(visible=False)
    main()
