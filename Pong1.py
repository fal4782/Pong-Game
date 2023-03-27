import turtle

wn = turtle.Screen()
wn.title("Pong by @Fal4782")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)  #stops the window from updating and helps in speeding up the game


#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) #sets speed to max possible speed
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup() #usually draws a line while movement but we do not want that
paddle_a.goto(-350,0)


#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) #sets speed to max possible speed
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup() #usually draws a line while movement but we do not want that
paddle_b.goto(350,0)

#Ball
ball = turtle.Turtle()
ball.speed(0) #sets speed to max possible speed
ball.shape("square")
ball.color("white")
ball.penup() #usually draws a line while movement but we do not want that
ball.goto(0,0)
ball.dx = 1 #every time ball moves in x-direction, it moves by 2 pixels
ball.dy = -1 #every time ball moves in y-direction, it moves by 2 pixels

#Function
def paddle_a_up():
    y = paddle_a.ycor() #ycor returns the y-coordinate (this value is assigned to y)
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor() #ycor returns the y-coordinate (this value is assigned to y)
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor() #ycor returns the y-coordinate (this value is assigned to y)
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor() #ycor returns the y-coordinate (this value is assigned to y)
    y -= 20
    paddle_b.sety(y)    

#Keyboard binding
wn.listen() #listen for keyboard input
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


#Main game loop   
while True:
    wn.update()  #updates the screen everytime the loop runs
    
    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1; #reverses the direction of the ball

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1; #reverses the direction of the ball

    if ball.xcor() > 390:
        ball.goto(0,0) #as if it goes off the left or ride side then that player loses and the ball resets to the centre
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.goto(0,0) #as if it goes off the left or ride side then that player loses and the ball resets to the centre
        ball.dx *= -1




