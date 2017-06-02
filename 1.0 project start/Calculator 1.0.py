import turtle
import math
s = turtle.Screen()
s.screensize(100,200)
s.setup (width=250, height=450, startx=720, starty=300)
s.title("Calculator")
t = turtle
t.speed(0)
t.width(5)
t.shape("blank")

def grid():
    t.penup()
    t.goto(-100, -200)
    t.pendown()
    t.goto(100, -200)
    t.goto(100, 200)
    t.goto(-100, 200)
    t.goto(-100, -200)
    t.goto(-100, -150)
    t.goto(50, -150)
    t.penup()
    t.goto(-100, -100)
    t.pendown()
    t.goto(100, -100)
    t.penup()
    t.goto(-100, -50)
    t.pendown()
    t.goto(100, -50)
    t.penup()
    t.goto(-100, 0)
    t.pendown()
    t.goto(100, 0)
    t.penup()
    t.goto(-100, 50)
    t.pendown()
    t.goto(100, 50)
    t.penup()
    t.goto(-50, 50)
    t.pendown()
    t.goto(-50, -200)
    t.goto(0, -200)
    t.goto(0, 50)
    t.goto(50, 50)
    t.goto(50, -200)


def numbers():
    t.penup()
    t.goto(-75, -185)  # zero
    t.pendown()
    t.circle(10)
    ################
    t.penup()
    t.goto(-25, -175)  # dot
    t.dot(5)
    ###############
    t.penup()
    t.goto(20, -175)
    t.pendown()
    t.goto(30, -175)
    t.penup()  # =
    t.goto(20, -185)
    t.pendown()
    t.goto(30, -185)
    t.penup()
    ##############
    t.penup()
    t.goto(60, -150)
    t.pendown()
    t.goto(90, -150)  # plus
    t.penup()
    t.goto(75, -165)
    t.pendown()
    t.goto(75, -135)
    ###############
    t.penup()
    t.goto(-75, -140)
    t.pendown()  # one
    t.goto(-75, -110)
    t.goto(-85, -120)
    ################
    t.penup()
    t.goto(-35, -110)
    t.pendown()
    t.goto(-20, -110)
    t.goto(-20, -125)  # two
    t.goto(-35, -125)
    t.goto(-35, -140)
    t.goto(-20, -140)
    ##################
    t.penup()
    t.goto(20, -110)
    t.pendown()
    t.goto(35, -110)
    t.goto(35, -140)
    t.goto(20, -140)  # three
    t.penup()
    t.goto(20, -125)
    t.pendown()
    t.goto(35, -125)
    ################
    t.penup()
    t.goto(-70, -90)
    t.pendown()       # four
    t.goto(-70, -60)
    t.goto(-85, -80)
    t.goto(-65, -80)
    ################
    t.penup()
    t.goto(-30, -90)
    t.pendown()
    t.goto(-15, -90)  # five
    t.goto(-15, -75)
    t.goto(-30, -75)
    t.goto(-30, -60)
    t.goto(-15, -60)
    ###############
    t.penup()
    t.goto(35, -60)
    t.pendown()
    t.goto(20, -60)  # six
    t.goto(20, -90)
    t.goto(35, -90)
    t.goto(35, -75)
    t.goto(20, -75)
    ###############
    t.penup()
    t.goto(85, -75)
    t.pendown()  # minus
    t.goto(65, -75)
    ###############
    t.penup()
    t.goto(-85, -10)
    t.pendown()  # seven
    t.goto(-65, -10)
    t.goto(-80, -40)
    ##############
    t.penup()
    t.goto(-30, -10)
    t.pendown()
    t.goto(-15, -10)
    t.goto(-15, -40)
    t.goto(-30, -40)  # eight
    t.goto(-30, -10)
    t.goto(-30, -25)
    t.goto(-15, -25)
    ################
    t.penup()
    t.goto(20, -40)
    t.pendown()
    t.goto(35, -40)
    t.goto(35, -10)  # nine
    t.goto(20, -10)
    t.goto(20, -25)
    t.goto(35, -25)
    #################
    t.penup()
    t.goto(65, -35)
    t.pendown()
    t.goto(85, -15)  # cross
    t.penup()
    t.goto(65, -15)
    t.pendown()
    t.goto(85, -35)
    ##################
    t.penup()
    t.goto(-70, 35)
    t.pendown()  # clear
    t.goto(-85, 35)
    t.goto(-85, 15)
    t.goto(-70, 15)
    ##################
    t.penup()
    t.goto(-10,10)
    t.pendown()
    t.goto(-10,40)
    t.goto(-30,40)
    t.goto(-40,25)
    t.goto(-30,10)
    t.goto(-10,10)
    t.width(3)
    t.penup()
    t.goto(-28,20)
    t.pendown()
    t.goto(-18,30)
    t.penup()
    t.goto(-28,30)
    t.pendown()
    t.goto(-18,20)
    t.width(5)
    ##################
    t.penup()
    t.goto(10,25)
    t.pendown()
    t.goto(15,25)   #sqrt
    t.goto(20,10)
    t.goto(25,35)
    t.goto(40,35)
    #################
    t.penup()
    t.goto(75, 15)
    t.dot(9)
    t.goto(75, 35)  # div
    t.dot(9)
    t.goto(60, 25)
    t.pendown()
    t.goto(90, 25)
    ##################

########################################################################################################################




grid()
numbers()
t.speed(0)
t.width(3)

xy = [-95, 190]
#################################
def sqrt():
    if A[0] == 'sqrt':
        t.penup()
        t.goto(xy[0]-5,xy[1]+5)
        t.pendown()
        t.goto(xy[0]+15,xy[1]+5)
###################################
A = []
def click(x, y):
    if x < -50 and y < -150:
        A.append('0')
        sqrt()
        t.penup()
        t.goto(xy[0], xy[1])
        t.pendown()
        t.goto(xy[0] + 10, xy[1])
        t.goto(xy[0] + 10, xy[1] - 30)
        t.goto(xy[0], xy[1] - 30)
        t.goto(xy[0], xy[1])  # write zero
        t.penup()
        t.goto(xy[0], xy[1] - 30)
        t.pendown()
        t.width(1)
        t.goto(xy[0] + 10, xy[1])
        t.width(3)
        xy[0] += 15
    if x < -50 and y < -100 and y > -150:
        A.append('1')
        sqrt()
        t.penup()
        t.goto(xy[0] + 3, xy[1] - 10)
        t.pendown()
        t.goto(xy[0] + 10, xy[1])  # write one
        t.goto(xy[0] + 10, xy[1] - 30)
        xy[0] += 15
    if x < 0 and x > -50 and y < -100 and y > -150:
        A.append('2')
        sqrt()
        t.penup()
        t.goto(xy[0], xy[1])
        t.pendown()
        t.goto(xy[0] + 8, xy[1])
        t.goto(xy[0] + 8, xy[1] - 15)  # write two
        t.goto(xy[0], xy[1] - 15)
        t.goto(xy[0], xy[1] - 30)
        t.goto(xy[0] + 10, xy[1] - 30)
        xy[0] += 15
    if x < 50 and x > 0 and y < -100 and y > -150:
        A.append('3')
        sqrt()
        t.penup()
        t.goto(xy[0], xy[1])
        t.pendown()
        t.goto(xy[0] + 10, xy[1])
        t.goto(xy[0] + 10, xy[1] - 30)
        t.goto(xy[0], xy[1] - 30)
        t.penup()
        t.goto(xy[0], xy[1] - 15)
        t.pendown()
        t.goto(xy[0] + 10, xy[1] - 15)
        xy[0] += 15
    if x < -50 and y < -50 and y > -100:
        A.append('4')
        sqrt()
        t.penup()
        t.goto(xy[0], xy[1])
        t.pendown()
        t.goto(xy[0], xy[1] - 15)
        t.goto(xy[0] + 10, xy[1] - 15)
        t.penup()
        t.goto(xy[0] + 10, xy[1])
        t.pendown()
        t.goto(xy[0] + 10, xy[1] - 30)
        xy[0] += 15
    if x < 0 and x > -50 and y < -50 and y > -100:
        A.append('5')
        sqrt()
        t.penup()
        t.goto(xy[0] + 10, xy[1])
        t.pendown()
        t.goto(xy[0], xy[1])
        t.goto(xy[0], xy[1] - 15)
        t.goto(xy[0] + 10, xy[1] - 15)
        t.goto(xy[0] + 10, xy[1] - 30)
        t.goto(xy[0], xy[1] - 30)
        xy[0] += 15
    if x > 0 and x < 50 and y < -50 and y > -100:
        A.append('6')
        sqrt()
        t.penup()
        t.goto(xy[0] + 10, xy[1])
        t.pendown()
        t.goto(xy[0], xy[1])
        t.goto(xy[0], xy[1] - 30)
        t.goto(xy[0] + 10, xy[1] - 30)
        t.goto(xy[0] + 10, xy[1] - 15)
        t.goto(xy[0], xy[1] - 15)
        xy[0] += 15
    if x < -50 and y < 0 and y > -50:
        A.append('7')
        sqrt()
        t.penup()
        t.goto(xy[0], xy[1])
        t.pendown()
        t.goto(xy[0] + 10, xy[1])
        t.goto(xy[0], xy[1] - 30)
        xy[0] += 15
    if x < 0 and x > -50 and y < 0 and y > -50:
        A.append('8')
        sqrt()
        t.penup()
        t.goto(xy[0], xy[1])
        t.pendown()
        t.goto(xy[0] + 10, xy[1])
        t.goto(xy[0] + 10, xy[1] - 30)
        t.goto(xy[0], xy[1] - 30)
        t.goto(xy[0], xy[1])
        t.penup()
        t.goto(xy[0], xy[1] - 15)
        t.pendown()
        t.goto(xy[0] + 10, xy[1] - 15)
        xy[0] += 15
    if x > 0 and x < 50 and y < 0 and y > -50:
        A.append('9')
        sqrt()
        t.penup()
        t.goto(xy[0], xy[1] - 30)
        t.pendown()
        t.goto(xy[0] + 10, xy[1] - 30)
        t.goto(xy[0] + 10, xy[1])
        t.goto(xy[0], xy[1])
        t.goto(xy[0], xy[1] - 15)
        t.goto(xy[0] + 10, xy[1] - 15)
        xy[0] += 15
    if x > 50 and y < -100:
        A.append('+')
        xy[0] = -80
        xy[1] = 140
        t.penup()
        t.goto(-90, 130)
        t.pendown()
        t.goto(-90, 120)
        t.penup()
        t.goto(-95, 125)
        t.pendown()
        t.goto(-85, 125)
    if x > 50 and y < -50 and y > -100:
        A.append('-')
        xy[0] = -80
        xy[1] = 140
        t.penup()
        t.goto(-95, 125)
        t.pendown()
        t.goto(-85, 125)
    if x > 50 and y < 0 and y > -50:
        A.append('*')
        xy[0] = -80
        xy[1] = 140
        t.penup()
        t.goto(-95, 120)
        t.pendown()
        t.goto(-85, 135)
        t.penup()
        t.goto(-95, 135)
        t.pendown()
        t.goto(-85, 120)
    if x > 50 and y < 50 and y > 0:
        A.append('/')
        xy[0] = -80
        xy[1] = 140
        t.penup()
        t.goto(-95, 125)
        t.pendown()
        t.goto(-85, 125)
        t.penup()
        t.goto(-90, 130)
        t.dot(5)
        t.penup()
        t.goto(-90, 120)
        t.dot(5)
    if x < 0 and x > -50 and y < -150:
        A.append('.')
        t.penup()
        t.goto(xy[0], xy[1] - 30)
        t.dot(5)
        xy[0] += 5
    if x < 50 and x > 0 and y > 0 and y < 50:
        A.append('sqrt')
        t.penup()
        t.goto(-95,175)
        t.pendown()
        t.goto(-90,160)
        t.goto(-85,195)
        t.goto(-85,195)
        xy[0]+=15
    if x < -50 and y < 50 and y > 0:
        A.clear()
        turtle.color("black", "white")
        t.penup()
        t.width(1)
        t.goto(-96, 196)
        t.begin_fill()
        t.goto(95, 196)
        t.goto(95, 55)
        t.goto(-96, 55)
        t.goto(-96, 196)
        turtle.end_fill()
        t.width(3)
        xy[0] = -95
        xy[1] = 190
        s.onclick(click, 1)
        turtle.done
    if x > -50 and x < 0 and y > 0 and y < 50:
        t.color("black","white")
        xy[0] -= 15
        del A[len(A)-1]
        print(A)
        t.penup()
        t.goto(xy[0]+16, xy[1]+6)
        t.begin_fill()
        t.goto(xy[0]-1,xy[1]+6)
        t.goto(xy[0]-1,xy[1]-40)
        t.goto(xy[0]+16,xy[1]-40)
        t.goto(xy[0]+16,xy[1]+6)
        t.end_fill()
    if x > 0 and x < 50 and y < -150:
        xy[0]= -95
        A.append('=')
        t.penup()
        t.goto(-95, 80)
        t.pendown()
        t.goto(-85, 80)
        t.penup()
        t.goto(-95, 70)
        t.pendown()
        t.goto(-85, 70)
        t.penup()
        xy[0]+=15
        xy[1] = 90
        main()


def main():
    a = ''
    b = ''
    act = ''
    if A.count('+') == 1:
        act = '+'
        index1 = A.index('+')
        index0 = 0
    if A.count('-') == 1:
        act = '-'
        index0 = 0
        index1 = A.index('-')
    if A.count('*') == 1:
        act = '*'
        index0 = 0
        index1 = A.index('*')
    if A.count('/') == 1:
        act = '/'
        index0 = 0
        index1 = A.index('/')
    if A.count('sqrt') == 1:
        act = 'sqrt'
        index1 = len(A) - 1
        index0 = 1
    ########################
    for i in range(index0, index1):
        a += A[i]
    if a.count('.') == 1:
        a = float(a)
    else:
        a = int(a)
    ########################
    if len(A) - 1 != index1:
        for i in range(index1 + 1, len(A) - 1):
            b += A[i]
        if b.count('.') == 1:
            b = float(b)
        else:
            b = int(b)
    ########################
    if act == '+':
        c = a + b
        c = str(c)
    if act == '-':
        c = a - b
        c = str(c)
    if act == '/':
        c = a / b
        c = str(c)
    if act == '*':
        c = a * b
        c = str(c)
    if act == 'sqrt':
        c = math.sqrt(a)
        c = str(c)
    if c[-1] == '0' and c[-2] == '.':
        c = c[:-2]
    if len(c) > 9:
        c = c[:12]
    ########################
    for i in range(len(c)):
        if c[i] == '0':
            t.penup()
            t.goto(xy[0], xy[1])
            t.pendown()
            t.goto(xy[0] + 10, xy[1])
            t.goto(xy[0] + 10, xy[1] - 30)
            t.goto(xy[0], xy[1] - 30)
            t.goto(xy[0], xy[1])
            t.penup()
            t.goto(xy[0], xy[1] - 30)
            t.pendown()
            t.width(1)
            t.goto(xy[0] + 10, xy[1])
            t.width(3)
            xy[0] += 15
        if c[i] == '1':
            t.penup()
            t.goto(xy[0] + 3, xy[1] - 10)
            t.pendown()
            t.goto(xy[0] + 10, xy[1])
            t.goto(xy[0] + 10, xy[1] - 30)
            xy[0] += 15
        if c[i] == '2':
            t.penup()
            t.goto(xy[0], xy[1])
            t.pendown()
            t.goto(xy[0] + 8, xy[1])
            t.goto(xy[0] + 8, xy[1] - 15)
            t.goto(xy[0], xy[1] - 15)
            t.goto(xy[0], xy[1] - 30)
            t.goto(xy[0] + 10, xy[1] - 30)
            xy[0] += 15
        if c[i] == '3':
            t.penup()
            t.goto(xy[0], xy[1])
            t.pendown()
            t.goto(xy[0] + 10, xy[1])
            t.goto(xy[0] + 10, xy[1] - 30)
            t.goto(xy[0], xy[1] - 30)
            t.penup()
            t.goto(xy[0], xy[1] - 15)
            t.pendown()
            t.goto(xy[0] + 10, xy[1] - 15)
            xy[0] += 15
        if c[i] == '4':
            t.penup()
            t.goto(xy[0], xy[1])
            t.pendown()
            t.goto(xy[0], xy[1] - 15)
            t.goto(xy[0] + 10, xy[1] - 15)
            t.penup()
            t.goto(xy[0] + 10, xy[1])
            t.pendown()
            t.goto(xy[0] + 10, xy[1] - 30)
            xy[0] += 15
        if c[i] == '5':
            t.penup()
            t.goto(xy[0] + 10, xy[1])
            t.pendown()
            t.goto(xy[0], xy[1])
            t.goto(xy[0], xy[1] - 15)
            t.goto(xy[0] + 10, xy[1] - 15)
            t.goto(xy[0] + 10, xy[1] - 30)
            t.goto(xy[0], xy[1] - 30)
            xy[0] += 15
        if c[i] == 6:
            t.penup()
            t.goto(xy[0] + 10, xy[1])
            t.pendown()
            t.goto(xy[0], xy[1])
            t.goto(xy[0], xy[1] - 30)
            t.goto(xy[0] + 10, xy[1] - 30)
            t.goto(xy[0] + 10, xy[1] - 15)
            t.goto(xy[0], xy[1] - 15)
            xy[0] += 15
        if c[i] == '7':
            t.penup()
            t.goto(xy[0], xy[1])
            t.pendown()
            t.goto(xy[0] + 10, xy[1])
            t.goto(xy[0], xy[1] - 30)
            xy[0] += 15
        if c[i] == '8':
            t.penup()
            t.goto(xy[0], xy[1])
            t.pendown()
            t.goto(xy[0] + 10, xy[1])
            t.goto(xy[0] + 10, xy[1] - 30)
            t.goto(xy[0], xy[1] - 30)
            t.goto(xy[0], xy[1])
            t.penup()
            t.goto(xy[0], xy[1] - 15)
            t.pendown()
            t.goto(xy[0] + 10, xy[1] - 15)
            xy[0] += 15
        if c[i] == '9':
            t.penup()
            t.goto(xy[0], xy[1] - 30)
            t.pendown()
            t.goto(xy[0] + 10, xy[1] - 30)
            t.goto(xy[0] + 10, xy[1])
            t.goto(xy[0], xy[1])
            t.goto(xy[0], xy[1] - 15)
            t.goto(xy[0] + 10, xy[1] - 15)
            xy[0] += 15
        if c[i] == '.':
            t.penup()
            t.goto(xy[0], xy[1] - 30)
            t.dot(5)
            xy[0] += 5
s.onclick(click, 1)
turtle.mainloop()