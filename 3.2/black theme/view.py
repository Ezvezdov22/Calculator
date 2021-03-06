import turtle

paintercounter = [0]
t = turtle
t.width(5)
t.speed(0)
t.shape("blank")
s = turtle.Screen()
s.title("Calculator 3.2")
s.setup(width=400, height=700, startx=720, starty=100)
s.bgcolor("black")
turtle.color("white","black")
turtle.tracer(0, 0)


def painter(lst, key):
    if len(paintercounter) == 1:
        a = len(lst)
    else:
        a = 1
    for i in range(a):
        if len(paintercounter) == 1:
            key = i
            a = len(lst[i])
        else:
            a = len(lst[key])
        t.penup()
        t.goto(lst[key][0][0], lst[key][0][1])
        t.pendown()
        for j in range(a):
            if len(paintercounter) == 1 and (i == 2 or i == 25 or i == 26):
                t.width(10)
                t.goto(lst[key][j][0], lst[key][j][1])
                t.width(5)
            t.goto(lst[key][j][0], lst[key][j][1])
    paintercounter.append(0)
    return 0


def clearall():
    t.width(1)
    t.penup()
    t.goto(-156, 84)
    t.begin_fill()
    t.goto(156, 84)
    t.goto(156, 316)
    t.goto(-156, 316)
    t.goto(-156, 84)
    turtle.end_fill()
    t.width(5)


def clearonce(xy):
    t.width(1)
    t.penup()
    t.goto(xy[0] - 7, xy[1] - 55)
    t.begin_fill()
    t.goto(xy[0] + 27, xy[1] - 55)
    t.goto(xy[0] + 27, xy[1] + 16)
    t.goto(xy[0] - 7, xy[1] + 16)
    t.goto(xy[0] - 7, xy[1] - 55)
    t.end_fill()
    t.width(5)

def clearline():
    t.width(1)
    t.penup()
    t.goto(-125,240)
    t.begin_fill()
    t.goto(-125,160)
    t.goto(155,160)
    t.goto(155,240)
    t.goto(-125,240)
    t.end_fill()
    t.width(5)