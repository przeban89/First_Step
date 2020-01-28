import turtle

qazi_turtle = turtle.Turtle()
qazi_turtle.speed(0)
qazi_turtle.color("#285078", "#a0c8f0")
def square(f, r):
    for i in range(4):
        qazi_turtle.forward(f)
        qazi_turtle.right(r)

def circle(z, f, r):
    for i in range(72):
        square(f, r)
        qazi_turtle.right(z)
f = 100
x = 0
while x < 10:
    circle(11, f, 90)
    x += 1
    f += 15

"""
x = 0
y = 60
z = 60
while x < 50:
    x += 1
    y -= 10
    z -= 10
    square(50, 45)
    qazi_turtle.forward(z)
    square(50, 45)
    qazi_turtle.forward(y)

z = 105
for i in range(25):
    square(50,90)
    qazi_turtle.right(z)
for i in range(25):
    square(100,90)
    qazi_turtle.right(z)
"""