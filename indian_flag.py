import turtle

flag=turtle.Turtle()

flag.speed(5)
flag.pensize(6)
flag.color('#000080')

def draw(x,y):
    flag.penup()
    flag.goto(x,y)
    flag.pendown()

for i in range(24):
    flag.forward(80)
    flag.backward(80)
    flag.left(15)
draw(0, -80)

flag.circle(80, 360)
flag.pensize(4)


flag.color('green')
draw(0,-100)
flag.begin_fill()
flag.forward(500)
flag.backward(1000)
flag.right(90)
flag.forward(200)
flag.left(90)
flag.forward(1000)
flag.left(90)
flag.forward(200)
flag.left(90)
flag.end_fill()





flag.color('#ff9125')
draw(-500,100)
flag.begin_fill()
flag.backward(1000)
flag.right(90)
flag.forward(200)
flag.left(90)
flag.forward(1000)
flag.left(90)
flag.forward(200)
flag.end_fill()

flag.color('black')
draw(-500,300)
flag.forward(600)
flag.left(90)
flag.forward(1000)
flag.left(90)
flag.forward(600)
flag.left(90)
flag.forward(1000)



turtle.done()