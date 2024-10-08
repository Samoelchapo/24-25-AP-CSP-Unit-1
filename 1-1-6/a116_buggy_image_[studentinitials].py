#   a116_bugglegs_image.plegs
import turtle as trtl

#Spiders body
spider = trtl.Turtle()
spider.pensize(40)
spider.circle(20)
#Spiders legs
L = 8
legs = 150
Ldistance = 380 / L
spider.pensize(5)
Interval = 0
#Spider legs drawing
while (Interval < L):
  spider.goto(0,0)
  spider.setheading(Ldistance*Interval)
  spider.forward(legs)
  Interval = Interval + 1
spider.hideturtle()

Ln = trtl.Screen()
Ln.mainloop()
Ln.mainloop()