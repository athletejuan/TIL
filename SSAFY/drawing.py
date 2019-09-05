import turtle

ggobugi = turtle.Turtle()
ggobugi.setposition(-200, 0)
ggobugi.color('red')
ggobugi.width(1)
ggobugi.speed(20)
unibugi = turtle.Turtle()
unibugi.setposition(200, 0)
unibugi.color('green')
unibugi.width(1)
unibugi.speed(20)
turtle_king = turtle.Turtle()
turtle_king.setposition(0,0)
turtle_king.color('yellow')
turtle_king.width(1)
turtle_king.speed(20)

# turtle.speed(10)
# turtle.color('blue')
# turtle.width(1)

# def make_square(turtle):
#     turtle.forward(100)
#     turtle.right(90)
#     turtle.forward(100)
#     turtle.right(90)
#     turtle.forward(100)
#     turtle.right(90)
#     turtle.forward(100)
#     turtle.right(90)

# for i in range(100):
#     make_square(ggobugi)
#     ggobugi.right(5)
#     make_square(unibugi)
#     unibugi.right(5)
#     make_square(turtle_king)   
#     turtle_king.right(5)

def make_star(turtle):
    turtle.forward(100)
    turtle.right(120)
    turtle.forward(100)
    turtle.right(120)
    turtle.forward(100)
    # turtle.right(60)
    # turtle.forward(100)

for i in range(360):
    make_star(ggobugi)
    ggobugi.right(1)
    make_star(unibugi)
    unibugi.right(1)
    make_star(turtle_king)   
    turtle_king.right(1)