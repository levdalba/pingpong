from turtle import Turtle


class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, -280)
        self.setheading(90)
        self.pensize(5)
        self.pencolor("white")
        self.pendown()
        for _ in range(20):
            self.forward(20)
            self.penup()
            self.forward(20)
            self.pendown()
