# Pong Game using Turtle
# Dominick Smith

import turtle

# import os    
import winsound

# ! WINDOW SETUP
win = turtle.Screen()
win.title("AI Pong")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)  # stops the window to update automatically

# SCORES
score_a = 0
score_b = 0


# PADDLE A
paddle_a = turtle.Turtle()
paddle_a.speed(0)  # * speed of animation 0 -> max possible speed
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# PADDLE B
paddle_b = turtle.Turtle()
paddle_b.speed(0)  # * speed of animation 0 -> max possible speed
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# BALL
ball = turtle.Turtle()
ball.speed(0)  # * speed of animation 0 -> max possible speed
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)

# Setting its movement 
ball.dx = 0.15
ball.dy = 0.15

# PEN
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0  Player 2: 0", align="center", font=("Courier", 24, "bold"))


# Paddle mvmt
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# controls
win.listen()
win.onkeypress(paddle_a_up, "w")              
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")


# main game loop
while True:
    win.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Checking that the ball bounces
    if ball.ycor() > 282:
        ball.sety(282)
        ball.dy *= -1  # reverses direction
        # os.system("afplay bounce.wav&") # only for mac
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    elif ball.ycor() < -282:
        ball.sety(-282)
        ball.dy *= -1
        # os.system("afplay bounce.wav&") # only for mac
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 382:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(
            f"Player A: {score_a}  Player B: {score_b}",
            align="center",
            font=("Courier", 24, "bold"),
        )

    elif ball.xcor() < -382:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(
            f"Player A: {score_a}  Player B: {score_b}",
            align="center",
            font=("Courier", 24, "bold"),
        )

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (
        ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40
    ):
        ball.setx(340)
        ball.dx *= -1
        # os.system("afplay bounce.wav&") # only for mac
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (
        ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40
    ):
        ball.setx(-340)
        ball.dx *= -1
        # os.system("afplay bounce.wav&") # only for mac
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # AI Player
    if paddle_b.ycor() < ball.ycor() and abs(paddle_b.ycor() - ball.ycor()) > 10:
        paddle_b_up()
    elif paddle_b.ycor() > ball.ycor() and abs(paddle_b.ycor() - ball.ycor()) > 10:
        paddle_b_down()
