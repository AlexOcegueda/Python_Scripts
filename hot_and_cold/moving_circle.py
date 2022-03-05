#!/usr/bin/env python3

"""
This module contains functions related to drawing and moving a circle around the screen
"""

__author__ = 'Debbie Johnson'
__version__ = '1.0'
__copyright__ = "Copyright 2022.02.17, Chapter 4 Assignment"
__github__ = "https://github.com/dejohns2/CSC365_Spring2022_Code_Examples"

import random
import turtle
import tkinter

screen = None
user = None

hidden_x = 100
hidden_y = 100
hidden_circle_size = 50
hidden_circle_color = 'black'

user_circle_color = 'pink'
user_circle_size = 50

# position where the turtle will be drawn at
# these values will change by plus/minus 20 as arrows are pressed
user_x = 0  # center of screen moving right or left
user_y = 0  # center of screen moving up or down
fill_color = 'red'  # the color of the circle


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
    hidden_x = random.randint(-420, 420)  # left & right max: -420 & 420
    hidden_y = random.randint(-300, 300)  # bottom & top max: -300 & 300


def draw_instructions():
    # write text on the screen

    user.goto(-350, 350)  # from the current position which is center after clear, move left 350 up 350
    user.pencolor('white')  # text color
    user.write("Use arrows to move, or press 'h' for home", font=("Verdana", 12, "bold"))


def draw_hidden_circle():
    """
    clear the screen and draw the circle based on the x & y coordinates

    Returns:
        None
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

    Returns:
        None
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
    Returns:

    """
    user.clear()  # clear the previous screen for the update circle location
    user.hideturtle()  # don't show the icon
    user.penup()
    draw_user_circle()
    user.penup()  # avoid a trail when drawing next object
    draw_instructions()
    user.penup()  # don't want to see icon moving on the screen for next object
    draw_hidden_circle()


def game_menu():
    root = tkinter.Tk()
    root.title("Game Settings")
    root.geometry("300x250")

    title_font = ("Comic Sans MS", 14, "bold")
    title_label = tkinter.Label(root, text='Game Settings')
    title_label.configure(font=title_font)
    title_label.place(relx=.03, rely=.1)


def main():
    """
    The main function, used to test drawing a square

    Returns:
        None
    """
    game_menu()

    setup_window()  # configure how the turtle window screen will look like
    set_hidden_location()  # displays a fresh location
    display_game()  # draws everything on screen according to user input
    screen.mainloop()  # keep the turtle window open until the user closes it


# if this is the program starting module, then run the main function
if __name__ == '__main__':
    screen = turtle.Screen()
    user = turtle.Turtle(visible=False)
    main()
