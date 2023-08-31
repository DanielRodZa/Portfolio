import colorgram
import turtle
import random

file_name = 'color.jpg'
num_colors = 12
number_of_rows = 10
number_of_dots = 100

def get_colors(file_name, num_colors):
    colors = colorgram.extract(file_name, num_colors)
    color_list = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]
    

    return color_list


def main():
    """
        Extracts colors from an image file and uses Turtle module to draw a pattern on the screen.
    """
    color_list = get_colors(file_name, num_colors)
    turtle.colormode(255)
    tim = turtle.Turtle()
    tim.speed("fastest")
    tim.penup()
    tim.hideturtle()

    tim.setheading(225)
    tim.forward(250)
    tim.setheading(0)
    for _ in range(number_of_rows):
        for _ in range(int(number_of_dots/number_of_rows)):

            tim.dot(20, random.choice(color_list))
            tim.forward(50)

        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


    screen = turtle.Screen()
    screen.exitonclick()


if __name__ == '__main__':
    main()