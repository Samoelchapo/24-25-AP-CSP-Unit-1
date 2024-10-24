import turtle as trtl
turtle = trtl.Turtle()



turtle.speed(0)
def draw_star():
    turtle.begin_fill()
    for numbers in range(5):
        turtle.forward(30)
        turtle.right(145)
    turtle.end_fill()

def crescent_moon():
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
wn = trtl.Screen()
wn.mainloop()

