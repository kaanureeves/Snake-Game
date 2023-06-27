from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for _ in STARTING_POSITIONS:
            self.add_segment(_)

    def add_segment(self, _):
        turtle = Turtle()
        turtle.shape("square")
        turtle.color("white")
        turtle.penup()
        turtle.goto(_)
        self.segments.append(turtle)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for _ in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[_ - 1].xcor()
            new_y = self.segments[_ - 1].ycor()
            self.segments[_].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def upKey(self):
        if self.head.heading() != DOWN:
            self.segments[0].setheading(UP)

    def downKey(self):
        if self.head.heading() != UP:
            self.segments[0].setheading(DOWN)

    def leftKey(self):
        if self.head.heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def rightKey(self):
        if self.head.heading() != LEFT:
            self.segments[0].setheading(RIGHT)

    def snake_reset(self):
        for _ in self.segments:
            _.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
