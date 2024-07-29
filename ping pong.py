from turtle import Turtle, Screen 
import time
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("pong")
screen.tracer(0)

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(position)
        
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
        
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("red")
        self.goto(0,0)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        
        
    def move(self):
        new_x = self.xcor()+self.x_move
        new_y = self.ycor()+self.y_move
        self.goto(new_x,new_y)
        
    def y_bounce(self):
        self.y_move *= -1
        self.move_speed *= 0.9
    
    def x_bounce(self):
        self.x_move *= -1
        self.move_speed *= 0.9
   
    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 1.1
        self.x_bounce()
  
class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(0,250)
        self.write("Scoreboard",align="center", font =("Courier",40,"normal"))
        self.goto(-50,200)
        self.write(self.l_score, align="center", font = ("Courier", 50, "normal"))
        self.goto(50,200)
        self.write(self.r_score, align="center", font = ("Courier", 50, "normal"))
        
        
    def update_scoreboard(self):
        self.clear()
        self.goto(0,250)
        self.write("Scoreboard",align="center", font =("Courier",40,"normal"))
        self.goto(-50,200)
        self.write(self.l_score, align="center", font = ("Courier", 50, "normal"))
        self.goto(50,200)
        self.write(self.r_score, align="center", font = ("Courier", 50, "normal"))
        
        
    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()
       
    def r_point(self):
        self.r_score += 1
        self.update_scoreboard() 

def line():
    margin = Turtle()   
    margin.color("white")
    margin.penup()
    margin.goto(0,250)
    margin.hideturtle()
    margin.right(90)
    margin.pendown()
    for _ in range(100):
        margin.forward(10)
        margin.penup()
        margin.forward(10)
        margin.pendown()
     
        
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball() 
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on = True
while game_is_on:
    line()
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)
    
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.y_bounce()
        
    if ball.distance(r_paddle)<50 and ball.xcor() >320 or ball.distance(l_paddle) <50 and ball.xcor() < - 320:
        ball.x_bounce()
        
    if ball.xcor() >380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        

screen.exitonclick()
