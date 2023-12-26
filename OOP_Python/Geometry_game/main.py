from random import randint
import turtle

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectange(self, rectangle):
        if rectangle.point1.x < self.x < rectangle.point2.x and rectangle.point1.y < self.y < rectangle.point2.y:
            return True
        else:
            return False

    def distance_from_point(self, x, y):
        return ((self.x - x)**2 + (self.y - y)**2) ** 0.5

class GuiPoint(Point):

    def draw(self, canvas, size=5):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size=size)

class Rectangle:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def area(self):
        return (self.point2.x - self.point1.x) * (self.point2.y - self.point1.y)

class GuiRectangle(Rectangle):

    def draw(self, canvas):
        canvas.penup()
        canvas.goto(self.point1.x, self.point1.y)

        canvas.pendown()
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)
        canvas.left(90)
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)



def main():
    gui_rectangle = GuiRectangle(Point(randint(0, 400),randint(0, 400)),Point(randint(10, 400),randint(10, 400)))


    rectangle = Rectangle(Point(randint(0, 400),randint(0, 400)),Point(randint(10, 400),randint(10, 400)))
    print(f"Rectangle coordinates: ({rectangle.point1.x},{rectangle.point1.y}) and ({rectangle.point2.x},{rectangle.point2.y})")

    user_input = GuiPoint(float(input("Guess X: ")), float(input("Guess Y: ")))

    user_area = float(input("Guess rectangle area: "))

    print(f"Your point was inside rectangle: {user_input.falls_in_rectange(rectangle)}")
    print(f"Your area was off by: {rectangle.area() - user_area}")

    myturtle = turtle.Turtle()
    gui_rectangle.draw(canvas=myturtle)
    user_input.draw(canvas=myturtle)

    turtle.done()


if __name__ == "__main__":
    main()