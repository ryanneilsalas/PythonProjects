from turtle import Turtle

move_distance = 20
Up = 90
Down = 270
Left = 180
Right = 0


class Snake_Brain:
    def __init__(self, snake_coordinate, snake_segments):
        self.coordinate = snake_coordinate
        self.segments = snake_segments

    def create_snake(self):
        for coord in self.coordinate:
            self.add_segment(coord)

    def snake_move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(move_distance)

    def add_segment(self, coord):
        new_body = Turtle("square")
        new_body.color("white")
        new_body.penup()
        new_body.goto(coord)
        self.segments.append(new_body)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def up(self):
        if self.segments[0].heading() != Down:
            self.segments[0].setheading(Up)

    def left(self):
        if self.segments[0].heading() != Right:
            self.segments[0].setheading(Left)

    def down(self):
        if self.segments[0].heading() != Up:
            self.segments[0].setheading(Down)

    def right(self):
        if self.segments[0].heading() != Left:
            self.segments[0].setheading(Right)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,  1000)
        self.segments.clear()
        self.create_snake()
