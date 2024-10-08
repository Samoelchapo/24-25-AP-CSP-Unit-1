#   a116_ladybug.py
import turtle as trtl

# create ladybug head
spider = trtl.Turtle()
ladybug = trtl.Turtle()
ladybug.pensize(40)
ladybug.circle(5)
L = 6
legs = 80
Ldistance = 380 / L
spider.pensize(4)
Interval = 0
# Spider legs drawing
while (Interval < L):
    spider.goto(0, -50)
    spider.setheading(Ldistance * Interval)
    spider.forward(legs)
    Interval = Interval + 1
    spider.hideturtle()

ladybug.penup()
ladybug.goto(0, -55)
ladybug.color("red")
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(20)
ladybug.setheading(270)
ladybug.color("black")
ladybug.penup()
ladybug.goto(0, 5)
ladybug.pensize(2)
ladybug.pendown()
ladybug.forward(75)

# config dots
num_dots = 1
xpos = -20
ypos = -55
ladybug.pensize(10)

# draw two sets of dots
for num_dots  in range (2):
  ladybug.penup()
  ladybug.goto(xpos, ypos)
  ladybug.pendown()
  ladybug.circle(3)
  ladybug.penup()
  ladybug.goto(xpos + 30, ypos + 20)
  ladybug.pendown()
  ladybug.circle(2)

  # position next dots
  xpos = ypos + 15
  xpos = xpos + 0
  num_dot = num_dots + 3
  import turtle as trtl


wn = trtl.Screen()
wn.mainloop()