# import math
# import turtle

# def xt(t):
#     return 16 * math.sin(t) ** 3

# def yt(t):
#     return 13 * math.cos(t) - 5 * \
# math.cos(2 * t) - 2 * \
# math.cos(3 * t) - \
# math.cos(4 * t)

# t = turtle.Turtle()
# t.speed(999)
# turtle.colormode(255)
# turtle.Screen().bgcolor(0, 0, 0)
# for i in range(2550):
#     t.goto((xt(i) * 20, yt (i) * 20))
#     t.pencolor((255 - i) % 255, i % 255, (255 + i) // 2 % 255)
#     t.goto (0, 0)
# t.hideturtle()
# turtle.update()
# turtle.mainloop()


import turtle

# Основные цвета для пеерсонажа
BODY_COLOR = 'red'
GLASS_COLOR = 'skyblue'

# Объект
t = turtle.Turtle()

def budy():
    t.pensize(30)
    t.fillcolor(BODY_COLOR)
    t.begin_fill()

# сторона справа
    t.right(90)
    t.forward(50)
    t.right(180)
    t.circle(40, -180)
    t.right(180)
    t.forward(200)

# голова
    t.right(180)
    t.circle(100, -180)

# сторона левая
    t.backward(20)
    t.left(15)
    t.circle(500, -20)
    t.backward(20)

    t.circle(40, -180)
    t.left(7)
    t.backward(50)

    t.up()
    t.left(90)
    t.forward(10)
    t.right(90)
    t.down()

    t.up()
    t.left(90)
    t.forward(10)
    t.right(90)
    t.down()

    t.right(240)
    t.circle(50, -70)

    t.end_fill()

# очки
def glass():
    t.up()
    t.right(230)
    t.forward(100)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.down()

    # уст. цвета
    t.fillcolor(GLASS_COLOR)
    t.begin_fill()

    t.right(150)
    t.circle(90, -55)

    t.right(180)
    t.forward(1)
    t.right(180)
    t.circle(10, -65)
    t.right(180)
    t.forward(110)
    t.right(180)

    t.circle(50, -190)
    t.right(170)
    t.forward(80)

    t.right(180)
    t.circle(45, -30)

    t.end_fill()

# Рюкзак
def backpage():
    t.up()
    t.right(60)
    t.forward(100)
    t.right(90)
    t.forward(75)

    t.fillcolor(GLASS_COLOR)
    t.begin_fill()

    t.down()
    t.forward(30)
    t.right(255)

    t.circle(300, -30)
    t.right(260)
    t.forward(30)
    t.end_fill()

budy()
glass()
backpage()

turtle.done()


