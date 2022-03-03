#!/usr/bin/env python3

import turtle

"""
This module contains functions related to drawing and moving a circle around the screen
"""

__author__ = 'Debbie Johnson'
__version__ = '1.0'
__copyright__ = "Copyright 2022.02.17, Chapter 4 Assignment"
__github__ = "https://github.com/dejohns2/CSC365_Spring2022_Code_Examples"

# position where the turtle will be drawn at
# these values will change by plus/minus 20 as arrows are pressed
x = 0  # center of screen moving right or left
y = 0  # center of screen moving up or down
fill_color = 'red'  # the color of the circle
screen = None
pen = None


def main():
    """
    The main function, used to test drawing a square

    Returns:
        None
    """

    global fill_color

    fill_color = 'pink'  # override the default red color

    pen.turtle_setup()  # set up the global window screen & turtle and bring window to front

    setup_window('black')  # configure how the turtle window screen will look like

    draw_circle(50)  # draw the initial shape based on diameter

    pen.screen.mainloop()  # keep the turtle window open until the user closes it

    pen.screen_recreation()  # recreate the window screen so it's ready for the next drawing


# if this is the program starting module, then run the main function
if __name__ == '__main__':
    global screen, pen

    screen = turtle.Screen()
    pen = turtle.Turtle
    main()
