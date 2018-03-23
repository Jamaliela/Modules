######################################################################
# Author: Dr. Scott Heggen      TODO: Change this to your names
# Username: heggens             TODO: Change this to your usernames
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

import turtle               # Notice the different ways we can import modules
from math import sqrt       # Notice the different ways we can import modules; there's one more way...


def calculate_size(num_dots):
    square = sqrt(num_dots)
    if num_dots % square == 0:
        return (int(square), int(square))
    else:
        denom = num_dots // sqrt(num_dots)
        while num_dots % denom!= 0:
            denom -= 1
        return (int(denom), int(num_dots // denom))


def is_valid_size(dot_width, dot_height, distance, screen_width, screen_height):
    if dot_width * distance > screen_width or dot_height * distance > screen_height:
        return False
    return True


def draw_board(dot_distance, dottie, height, width):
    for y in range(height):
        for i in range(width):
            dottie.dot()
            dottie.forward(dot_distance)
        dottie.backward(dot_distance * width)
        dottie.right(90)
        dottie.forward(dot_distance)
        dottie.left(90)


def user_input(screen_height, screen_width):
    num_dots = "x"
    while not num_dots.isnumeric():
        num_dots = input("How many dots do you want? ")
    num_dots = int(num_dots)
    (width, height) = calculate_size(num_dots)
    dot_distance = screen_width
    first = False
    while not is_valid_size(width, height, dot_distance, screen_width, screen_height):
        if first:
            print("That won't fit on the screen; pick a smaller number")
        dot_distance = input("How far apart are the dots? ")
        while not dot_distance.isnumeric():
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
