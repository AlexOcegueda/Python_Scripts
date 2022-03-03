import turtle

x = 0
y = 0
pen = None
screen = None
fill_color = 'pink'

# Place the hidden object randomly on the screen
# It will begin in the center of the screen

# User determines difficulty of game by controlling size

# Change the objects color depending on whether they are hotter or colder

# Notify them how many moves they made to find the hidden object

# key listeners: s = hidden object H = hides the object R = reset the game


def draw_circle(diameter=10):
    """
    clear the screen and draw the circle based on the x & y coordinates

    Args:
        diameter (int): the diameter size of the circle (default 10)
        fill_color (str): the inside color of the circle (default red)

    Returns:
        None
        :param pen: Turtle which the user controls
    """

    global x, y, fill_color

    pen.hideturtle()  # don't show the icon
    pen.speed('fastest')  # draw quickly

    pen.clear()  # clear the previous screen for the update circle location

    # write text on the screen
    pen.penup()  # don't want to see icon moving on the screen
    pen.goto(-350, 350)  # from the current position which is center after clear, move left 350 up 350
    pen.pencolor('white')  # text color
    pen.write("Use arrows to move, or press 'h' for home", font=("Verdana", 12, "bold"))

    # draw circle
    pen.goto(x, y)  # move to the updated x (left-right) and y (up-down) location from center
    pen.pendown()  # start drawing the outline of the circle
    pen.fillcolor(fill_color)  # fill color of the circle
    pen.begin_fill()  # start the fill of whatever is being drawn
    pen.circle(50)  # diameter of the circle
    pen.end_fill()  # done drawing the object to complete the fill


def main():
    """
    The main function, used to test drawing a square

    Returns:
        None
    """

    draw_circle()
    turtle.mainloop()


# if this is the program starting module, then run the main function
if __name__ == '__main__':
    screen = turtle.Screen()
    pen = turtle.Turtle()
    main()
