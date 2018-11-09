######################################################################
# Author: Tom West & Ela Jamali
# Username: Westth & Jamalie
#
# Assignment: T12: Modules
#
# Purpose: A special game from my (and likely, many of your) childhood
#
######################################################################
# Acknowledgements:
#
# Idea inspired by original code from: https://michael0x2a.com/blog/turtle-examples
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

import turtle           # Notice the different ways we can import modules
from math import sqrt   # Notice the different ways we can import modules; there's one more way,
                        # which you've seen before (see a06_genes_test.py)


def calculate_size(num_dots):
    """takes in the number of dots and put it in to length and width values
     :param: num_dots is number of dots
     :return: square length & width values
     :return : denom length and width values after value
     """
    square = sqrt(num_dots) # does the square root of the number
    if num_dots % square == 0: # checks to make sure its an even square
        return (int(square), int(square))
    else:                                   # if it is not a an even square it makes a rectangle
        denom = num_dots // sqrt(num_dots)
        while num_dots % denom != 0:
            denom -= 1
        return (int(denom), int(num_dots // denom))


def is_valid_size(dot_width, dot_height, distance, screen_width, screen_height):
    """takes the dot width and height and make sure it will fit the window
    :param: dot_width  dot width
    :param: dot_height  dot height
    :param: distance    distance between dots
    :param: screen_width screen height
    :param: screen_height screen width
    """
    if dot_width * distance > screen_width or dot_height * distance > screen_height: # makes sure we don't fall off the page
        return False
    return True


def draw_board(dot_distance, dottie, height, width):
    """draws the grid of dots"""
    for y in range(height): # draws the dots with a loop
        for i in range(width):
            dottie.dot()
            dottie.forward(dot_distance)
        dottie.backward(dot_distance * width)
        dottie.right(90)
        dottie.forward(dot_distance)
        dottie.left(90)


def user_input(screen_height, screen_width):
    """takes user input to make the dots
    :param: screen_height
    :param: screen_width
    :return: dot_distance
    :return: height:
    :return: width:
    """
    num_dots = "x"
    while not num_dots.isnumeric():
        num_dots = input("How many dots do you want? ") # makes sure we have correct input for dots
    num_dots = int(num_dots) # makes dots an int
    (width, height) = calculate_size(num_dots) # throws it up to cal
    dot_distance = screen_width # screen width it set equal to dot distances
    first = False
    while not is_valid_size(width, height, dot_distance, screen_width, screen_height):
        if first:
            print("That won't fit on the screen; pick a smaller number") # keeps the number small enough to fit the screen
        dot_distance = input("How far apart are the dots? ")
        while not dot_distance.isnumeric(): # make sure it is a number
            dot_distance = input("Let's try an integer instead. \nHow far apart are the dots? ")
        first = True
        dot_distance = int(dot_distance)
    return dot_distance, height, width


def main():
    screen_width = 1100
    screen_height = 650

    (dot_distance, height, width) = user_input(screen_height, screen_width)
    wn = turtle.Screen()
    wn.setup(width=screen_width, height=screen_height, startx=0, starty=0)

    dottie = turtle.Turtle()
    dottie.speed(0)
    dottie.penup()
    dottie.setpos(-(screen_width/2-50), screen_height/2-25)

    draw_board(dot_distance, dottie, height, width)
    dottie.hideturtle()

    wn.exitonclick()


if __name__ == "__main__":
    main()
