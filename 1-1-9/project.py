import turtle as trtl


#Small crescent size
painter = trtl.Turtle()
painter.penup()
painter.goto(-350,350)
painter.pendown()
painter.speed(2)
painter.pensize(5)
painter.fillcolor('white')
painter.right(180)
painter.circle(70,100)
#Big crescent


painter.left(120)
painter.penup()
painter.goto(-350,350)
painter.left(120)
painter.pendown()
painter.circle(100,250)
painter.penup()
painter.goto(-417,265)
painter.pendown()
painter.left(250)
painter.circle(150,50)






















wn = trtl.Screen()
wn.mainloop()