import turtle

wnd = turtle.Screen()
wnd.title("Pong")
wnd.bgcolor("white")
wnd.setup(width=1280, height=720)
wnd.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("black")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-550, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("black")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(550, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("black")
ball.penup()
ball.goto(0, 0)
ball.dx = 1/3
ball.dy = 1/3

# Stats
stats = turtle.Turtle()
stats.speed(0)
stats.shape("square")
stats.color("black")
stats.penup()
stats.hideturtle()
stats.goto(0, 260)
stats.write("Player A: 0  Player B: 0", align="center", font=("bold", 24, "normal"))


# Functions
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


# Keyboard bindings
wnd.listen()
wnd.onkeypress(paddle_a_up, "w")
wnd.onkeypress(paddle_a_down, "s")
wnd.onkeypress(paddle_b_up, "Up")
wnd.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wnd.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking

    # Top and bottom
    if ball.ycor() > 350:
        ball.sety(350)
        ball.dy *= -1

    elif ball.ycor() < -350:
        ball.sety(-350)
        ball.dy *= -1

    # Left and right
    if ball.xcor() > 550:
        score_a += 1
        stats.clear()
        stats.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("bold", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -550:
        score_b += 1
        stats.clear()
        stats.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("bold", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    # Paddle and ball collisions
    if ball.xcor() < -540 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1

    elif ball.xcor() > 540 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1