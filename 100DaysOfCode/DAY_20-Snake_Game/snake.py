from turtle import Turtle, Screen
STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
SHAPES = {"hu":"Snake_img\\snake_head_up.gif","hl":"Snake_img\\snake_head_left.gif", "hd":"Snake_img\\snake_head_down.gif", "hr":"Snake_img\\snake_head_right.gif",\
        "bud":"Snake_img\\snake_bod_up_down.gif","blr": "Snake_img\\snake_bod_left_right.gif",\
        "tul":"Snake_img\\snake_turn_up_left.gif", "tur":"Snake_img\\snake_turn_up_right.gif", "tdl":"Snake_img\\snake_turn_down_left.gif", "tdr":"Snake_img\\snake_turn_down_right.gif",\
        "tr":"Snake_img\\snake_tail_right.gif", "tl":"Snake_img\\snake_tail_left.gif", "tu":"Snake_img\\snake_tail_up.gif", "td":"Snake_img\\snake_tail_down.gif"}
HR = SHAPES["hr"]
HL = SHAPES["hl"]
HD = SHAPES["hd"]
HU = SHAPES["hu"]
BUD = SHAPES["bud"]
BLR = SHAPES["blr"]
TUL = SHAPES["tul"]
TUR = SHAPES["tur"]
TDL = SHAPES["tdl"]
TDR = SHAPES["tdr"]
TR = SHAPES["tr"]
TL = SHAPES["tl"]
TU = SHAPES["tu"]
TD = SHAPES["td"]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake(Turtle):
    
    def __init__(self):
        super().__init__()
        self.add_shapes(SHAPES)
        self.segments  =[]
        self.create_snake()
        self.head = self.segments[0]
        self.head.shape(HR)
        #self.shapesize(stretch_len=2,stretch_wid=2)
        self.segments[-1].shape(TR)
        
    def create_snake(self):
        for pos in STARTING_POSITION:
            self.add_segment(pos)


    def add_segment(self,pos):
        new_seg = Turtle("square")
        new_seg.shape(BLR)
        new_seg.color("white")
        new_seg.penup()
        new_seg.goto(pos)
        self.segments.append(new_seg)

    def extend(self):
        self.add_segment(self.segments[-1].position())
    
    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            self.tail = self.segments[-1]
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
            old_heading = self.segments[seg_num].heading()
            self.segments[seg_num].setheading(self.segments[seg_num-1].heading())
            new_heading = self.segments[seg_num].heading()
            
            if (new_heading == UP and\
                 old_heading == LEFT) or\
                     (new_heading == RIGHT and\
                         old_heading == DOWN):
                self.segments[seg_num].shape(TDR)
            elif (new_heading == UP and\
                 old_heading == RIGHT) or\
                     (new_heading == LEFT and\
                         old_heading == DOWN):
                self.segments[seg_num].shape(TDL)
            elif (new_heading == DOWN and\
                 old_heading == RIGHT) or\
                     (new_heading == LEFT and\
                         old_heading == UP):
                self.segments[seg_num].shape(TUL)
            elif (new_heading == RIGHT and\
                 old_heading == UP) or\
                     (new_heading == DOWN and\
                         old_heading == LEFT):
                self.segments[seg_num].shape(TUR)
            elif new_heading == 90 or new_heading == 270:
                self.segments[seg_num].shape(BUD)
            else:
                self.segments[seg_num].shape(BLR)
        if self.tail.heading() == RIGHT:
            self.tail.shape(TR)
        elif self.tail.heading() == LEFT:
            self.tail.shape(TL)
        elif self.tail.heading() == UP:
            self.tail.shape(TU)
        elif self.tail.heading() == DOWN:
            self.tail.shape(TD)
            
        
        self.head.forward(MOVE_DISTANCE)

    def add_shapes(self,shape):
        for _,j in shape.items():
            self.screen.addshape(j)


    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
            self.head.shape(HU)
    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)
            self.head.shape(HD)
    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)
            self.head.shape(HL)
    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)
            self.head.shape(HR)