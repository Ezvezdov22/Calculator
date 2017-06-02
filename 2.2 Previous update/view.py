import turtle
import model
t = turtle
t.width(5)
t.speed(0)
t.shape("blank")
s = turtle.Screen()
s.title("Calculator 2.2")
s.setup (width=400, height=700, startx=720, starty=100)
turtle.color("black", "white")


def painter(lst,key):
    if lst == model.SymbolsPrint:
        a = len(lst)
    else:
        a= 1
    for i in range(a):
        if lst == model.SymbolsPrint:
            key = i
            a = len(lst[i])
        else:
            a = len(lst[key])
        t.penup()
        t.goto(lst[key][0][0],lst[key][0][1])
        t.pendown()
        for j in range(a):
            if model.SymbolsPrint == lst and (i == 2 or i == 22 or i == 23)  :
                t.width(10)
                t.goto(lst[key][j][0],lst[key][j][1])
                t.width(5)
            t.goto(lst[key][j][0],lst[key][j][1])
    return 0

def clearall():
        t.width(1)
        t.penup()
        t.goto(-156,84)
        t.begin_fill()
        t.goto(156,84)
        t.goto(156,316)
        t.goto(-156,316)
        t.goto(-156,84)
        turtle.end_fill()
        t.width(5)

def clearonce():
    t.width(1)
    t.penup()
    t.goto(model.xy[0]-7,model.xy[1]-55)
    t.begin_fill()
    t.goto(model.xy[0]+27,model.xy[1]-55)
    t.goto(model.xy[0]+27,model.xy[1]+16)
    t.goto(model.xy[0]-7,model.xy[1]+16)
    t.goto(model.xy[0]-7,model.xy[1]-55)
    t.end_fill()
    t.width(5)

    

























    #if lst == model.ClickSymbols and (key != 10 or key != 13):
        #tmp.append(key)
        #update()

