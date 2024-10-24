import turtle as trtl
#import Def

global turtle
turtle = trtl.Turtle()
painter = trtl.Turtle()
turtle.speed(100)
painter.penup()
painter.goto(-350, 350)
painter.pendown()
def crescent_moon():
    global turtle
    # Small crescent size

    turtle = trtl.Turtle()
    turtle.hideturtle()
    painter.color('white')
    turtle.begin_fill()

    painter.speed(100)
    painter.pensize(5)
    painter.right(180)
    painter.circle(70, 100)
# Big crescent
    painter.begin_fill()
    painter.left(120)
    painter.penup()
    painter.goto(-350, 350)
    painter.left(120)
    painter.pendown()
    painter.circle(100, 250)
    painter.penup()
    painter.goto(-417, 265)
    painter.pendown()
    painter.left(250)
    painter.circle(150, 50)

    painter.end_fill()


def draw_star():
    global turtle

    turtle.begin_fill()
    turtle.fillcolor('white')
    for numbers in range(5):
        turtle.forward(50)
        turtle.right(145)
    turtle.end_fill()

    #Big crescent

    '''
    turtle.left(120)
    turtle.penup()
    turtle.goto(-350,350)
    turtle.left(120)
    turtle.pendown()
    turtle.circle(100,250)
    turtle.penup()
    turtle.goto(-417,265)
    turtle.pendown()
    turtle.left(250)
    turtle.circle(150,50)


    #Small crescent size
    turtle = trtl.Turtle()
    turtle.penup()
    turtle.goto(-350,350)
    turtle.pendown()
    turtle.speed(2)
    turtle.pensize(5)
    turtle.fillcolor('white')
    turtle.right(180)
    turtle.circle(70,100)
    #Big crescent


    turtle.left(120)
    turtle.penup()
    turtle.goto(-350,350)
    turtle.left(120)
    turtle.pendown()
    turtle.circle(100,250)
    turtle.penup()
    turtle.goto(-417,265)
    turtle.pendown()
    turtle.left(250)
    turtle.circle(150,50)
'''

turtle.color('red')
turtle.begin_fill()
turtle.goto(470,0)
turtle.goto(470,400)
turtle.goto(-490,400)
turtle.goto(-490,0)
turtle.goto(0,0)
turtle.end_fill()
turtle.penup()
turtle.goto(-350,350)
turtle.pendown()
crescent_moon()

turtle.color('white')
turtle.begin_fill()
turtle.goto(470,0)
turtle.goto(470,-400)
turtle.goto(-500,-400)
turtle.goto(-490,0)
turtle.goto(0,0)
turtle.end_fill()
turtle.penup()
turtle.goto(-250,350)
turtle.begin_fill()
turtle.pendown()
draw_star()

turtle.end_fill()

turtle.penup()
turtle.goto(-200,300)
turtle.left(5)
turtle.pendown()
turtle.begin_fill()
draw_star()
turtle.end_fill()

turtle.penup()
turtle.goto(-210,250)
turtle.left(5)
turtle.pendown()
turtle.begin_fill()
draw_star()
turtle.end_fill()

turtle.penup()
turtle.goto(-300,300)
turtle.left(5)
turtle.pendown()
turtle.begin_fill()
draw_star()
turtle.end_fill()

turtle.penup()
turtle.goto(-280, 250)
turtle.left(5)
turtle.pendown()
turtle.begin_fill()
draw_star()
turtle.end_fill()












wn = trtl.Screen()
wn.mainloop()
