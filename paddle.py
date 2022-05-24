from turtle import Turtle

WIDTH = 20
HEIGHT = 100
MOVE_DISTANCE = 20
UP = 90
DOWN = 270



class Paddle:

    def __init__(self, position_list):
        self.segment = []
        self.starting_position = position_list
        self.initialise()
        self.head = self.segment[0]
        self.tail = self.segment[-1]

    def initialise(self):
        for position in self.starting_position:
            new_segment = Turtle("square")
            new_segment.color("pink")
            new_segment.speed("fastest")
            new_segment.penup()
            new_segment.goto(position)
            self.segment.append(new_segment)

    def move_up(self):
        for seg_num in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def move_down(self):
        for seg_num in range(len(self.segment) - 1):
            new_x = self.segment[seg_num + 1].xcor()
            new_y = self.segment[seg_num + 1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
        self.tail.forward(MOVE_DISTANCE)

    def up(self):
        self.head.setheading(UP)
        self.move_up()

    def down(self):
        self.tail.setheading(DOWN)
        self.move_down()





