import turtle
import math
t = turtle
t.width(5)
t.speed(0)
t.shape("blank")
s = turtle.Screen()
s.title("Calculator 2.0")
s.setup (width=400, height=700, startx=720, starty=100)

xy = [-150,300]
SymbolsPrint=[
  [[-160,-320],[160,-320],[160,320],[-160,320],[-160,-320],[-160,-240],[80,-240],[80,-160],[160,-160],[-160,-160],[-160,-80],[160,-80],[160,0],[-160,0],[-160,80],[160,80],[80,80],[80,-320],[0,-320],[0,80],[-80,80],[-80,80],[-80,-320]],  #grid
  [[-130,-250],[-110,-250],[-100,-260],[-100,-300],[-110,-310],[-130,-310],[-140,-300],[-140,-260],[-130,-250]], #0
  [[-40,-280],[-40,-280]], #dot
  [[20,-270],[60,-270]], #=1
  [[20,-290],[60,-290]], #=2
  [[90,-240],[150,-240],[120,-240],[120,-210],[120,-270]], #+
  [[-130,-190],[-110,-170],[-110,-230]], #1
  [[-60,-180],[-50,-170],[-30,-170],[-20,-180],[-20,-190],[-60,-230],[-20,-230]], #2
  [[20,-220],[30,-230],[50,-230],[60,-220],[60,-210],[50,-200],[30,-200],[50,-200],[60,-190],[60,-180],[50,-170],[50,-170],[30,-170],[20,-180]], #3
  [[-110,-150],[-110,-90],[-140,-130],[-100,-130]], #4
  [[-20,-90],[-60,-90],[-60,-110],[-30,-110],[-20,-120],[-20,-140],[-30,-150],[-50,-150],[-60,-140]], #5
  [[60,-100],[50,-90],[30,-90],[20,-100],[20,-140],[30,-150],[50,-150],[60,-140],[60,-130],[50,-120],[20,-120]], #6
  [[100,-120],[140,-120]],  #-
  [[-140,-20],[-130,-10],[-90,-10],[-130,-70],[-110,-40],[-130,-40],[-90,-40]], #7
  [[-50,-10],[-30,-10],[-20,-20],[-20,-30],[-30,-40],[-20,-50],[-20,-60],[-30,-70],[-50,-70],[-60,-60],[-60,-50],[-50,-40],[-30,-40],[-50,-40],[-60,-30],[-60,-20],[-50,-10]], #8
  [[20,-60],[30,-70],[50,-70],[60,-60],[60,-40],[60,-20],[50,-10],[30,-10],[20,-20],[20,-30],[30,-40],[60,-40]], #9
  [[100,-60],[140,-20],[120,-40],[100,-20],[140,-60]], #*
  [[-100,70],[-130,70],[-140,60],[-140,20],[-130,10],[-100,10]], #claer
  [[-10,10],[-10,70],[-50,70],[-70,40],[-50,10],[-10,10]], #BackspaceGrid
  [[-45,30],[-25,50],[-35,40],[-45,50],[-25,30]], #BackSpaceSymbol
  [[15,40],[30,40],[40,10],[50,60],[70,60]], #sqrt
  [[100,40],[140,40]], #divline
  [[120,50],[120,50]], #divdot1
  [[120,30],[120,30]]] #divdot2
ClickSymbols = [
  [[xy[0],xy[1]-5],[xy[0],xy[1]-45],[xy[0]+5,xy[1]-50],[xy[0]+15,xy[1]-50],[xy[0]+20,xy[1]-45],[xy[0]+20,xy[1]-5],[xy[0]+15,xy[1]],[xy[0]+5,xy[1]],[xy[0],xy[1]-5]], #0
  [[xy[0],xy[1]-20],[xy[0]+15,xy[1]],[xy[0]+15,xy[1]-50]], #1
  [[xy[0]+20,xy[1]-50],[xy[0],xy[1]-50],[xy[0]+20,xy[1]-15],[xy[0]+20,xy[1]-5],[xy[0]+20,xy[1]-5],[xy[0]+15,xy[1]],[xy[0]+5,xy[1]],[xy[0],xy[1]-5],[xy[0],xy[1]-15]], #2
  [[xy[0],xy[1]-5],[xy[0]+5,xy[1]],[xy[0]+15,xy[1]],[xy[0]+20,xy[1]-5],[xy[0]+15,xy[1]-20],[xy[0],xy[1]-20],[xy[0]+15,xy[1]-20],[xy[0]+20,xy[1]-25],[xy[0]+20,xy[1]-45],[xy[0]+15,xy[1]-50],[xy[0],xy[1]-50]],#3
  [[xy[0]+20,xy[1]-50],[xy[0]+20,xy[1]],[xy[0],xy[1]-30],[xy[0]+25,xy[1]-30]], #4
  [[xy[0]+20,xy[1]],[xy[0],xy[1]],[xy[0],xy[1]-20],[xy[0]+15,xy[1]-20],[xy[0]+20,xy[1]-25],[xy[0]+20,xy[1]-40],[xy[0]+15,xy[1]-50],[xy[0]+5,xy[1]-50],[xy[0],xy[1]-45]], #5
  [[xy[0]+20,xy[1]-5],[xy[0]+15,xy[1]],[xy[0]+5,xy[1]],[xy[0],xy[1]-5],[xy[0],xy[1]-45],[xy[0]+5,xy[1]-50],[xy[0]+15,xy[1]-50],[xy[0]+20,xy[1]-45],[xy[0]+20,xy[1]-30],[xy[0]+15,xy[1]-25],[xy[0],xy[1]-25]], #6
  [[xy[0],xy[1]-50],[xy[0]+7,xy[1]-30],[xy[0]+15,xy[1]-30],[xy[0],xy[1]-30],[xy[0]+7,xy[1]-30],[xy[0]+20,xy[1]],[xy[0],xy[1]],[xy[0]-3,xy[1]-3]], #7
  [[xy[0],xy[1]-5],[xy[0]+5,xy[1]],[xy[0]+15,xy[1]],[xy[0]+20,xy[1]-5],[xy[0]+20,xy[1]-15],[xy[0]+15,xy[1]-20],[xy[0]+5,xy[1]-20],[xy[0],xy[1]-25],[xy[0],xy[1]-45],[xy[0]+5,xy[1]-50],[xy[0]+15,xy[1]-50],[xy[0]+20,xy[1]-45],[xy[0]+20,xy[1]-25],[xy[0]+15,xy[1]-20],[xy[0]+5,xy[1]-20],[xy[0],xy[1]-15],[xy[0],xy[1]-5]],#8
  [[xy[0],xy[1]-45],[xy[0]+5,xy[1]-50],[xy[0]+15,xy[1]-50],[xy[0]+20,xy[1]-45],[xy[0]+20,xy[1]-5],[xy[0]+15,xy[1]],[xy[0]+5,xy[1]],[xy[0],xy[1]-5],[xy[0],xy[1]-25],[xy[0]+5,xy[1]-30],[xy[0]+20,xy[1]-30]],
  [[xy[0]-5,xy[1]-50],[xy[0]-5,xy[1]-50]],#.
  [[-155,200],[-125,200],[-140,200],[-140,220],[-140,180]], #+
  [[-150,180],[-130,220],[-140,200],[-150,220],[-130,180]], #*
  [[-150,200],[-130,200]], #divline
  [[-140,210],[-140,210]], #divdot1
  [[-140,190],[-140,190]],  #divdot2
  [[-150,200],[-130,200]], #-
  [[-150,280],[-130,250],[-120,310]], #sqrt
  [[xy[0]-10,xy[1]+10],[xy[0]+30,xy[1]+10]], #sqrtline
  [[-150,125],[-130,125]], #=line1
  [[-150,115],[-130,115]], #=line2
  [[-90,140],[-110,140],[-110,115],[-90,115],[-110,115],[-110,90],[-90,90]],  #error[e]
  [[-80,90],[-80,125],[-75,130],[-65,130],[-60,125],[-60,115],[-65,110],[-80,110],[-60,90]], #error[r]
  [[-50,90],[-50,125],[-45,130],[-35,130],[-30,125],[-30,115],[-35,110],[-50,110],[-30,90]], #error[r2]
  [[-20,95],[-20,125],[-15,130],[-5,130],[0,125],[0,95],[-5,90],[-15,90],[-20,95]], #error[o]
  [[10,90],[10,125],[15,130],[25,130],[30,125],[30,115],[25,110],[10,110],[30,90]] #error[r2]
]
tmp = []
def painter(lst,key):
    if lst == SymbolsPrint:
        a = len(lst)
    else:
        a= 1
    for i in range(a):
        if lst == SymbolsPrint:
            key = i
            a = len(lst[i])
        else:
            a = len(lst[key])
        t.penup()
        t.goto(lst[key][0][0],lst[key][0][1])
        t.pendown()
        for j in range(a):
            if i == 2 and lst == SymbolsPrint or i == 22 and lst == SymbolsPrint or i == 23 and lst == SymbolsPrint or key == 14 and lst == ClickSymbols or key == 15 and lst == ClickSymbols  :
                t.width(10)
                t.goto(lst[key][j][0],lst[key][j][1])
                t.width(5)
            t.goto(lst[key][j][0],lst[key][j][1])
    if lst == ClickSymbols and key != 10 or key != 13 and lst == ClickSymbols:
        tmp.append(key)
        update()

def update():
    xy[0]+=30
    if tmp[-1] == 11 or tmp[-1] == 14 or tmp[-1] == 12 or tmp[-1] == 15 or tmp[-1] == 16:
        xy[0] = -120
        xy[1] = 220
    if tmp[-1] == 20:
        xy[0] = -120
        xy[1] = 140
        t.penup()
    if len(Task) == 0:
        xy[0] = -150
        xy[1] = 300
        tmp.clear()
    ClickSymbols[0] = [[xy[0],xy[1]-5],[xy[0],xy[1]-45],[xy[0]+5,xy[1]-50],[xy[0]+15,xy[1]-50],[xy[0]+20,xy[1]-45],[xy[0]+20,xy[1]-5],[xy[0]+15,xy[1]],[xy[0]+5,xy[1]],[xy[0],xy[1]-5]] #0
    ClickSymbols[1] = [[xy[0],xy[1]-20],[xy[0]+15,xy[1]],[xy[0]+15,xy[1]-50]] #1
    ClickSymbols[2] = [[xy[0]+20,xy[1]-50],[xy[0],xy[1]-50],[xy[0]+20,xy[1]-15],[xy[0]+20,xy[1]-5],[xy[0]+20,xy[1]-5],[xy[0]+15,xy[1]],[xy[0]+5,xy[1]],[xy[0],xy[1]-5],[xy[0],xy[1]-15]] #2
    ClickSymbols[3] = [[xy[0],xy[1]-5],[xy[0]+5,xy[1]],[xy[0]+15,xy[1]],[xy[0]+20,xy[1]-5],[xy[0]+15,xy[1]-20],[xy[0],xy[1]-20],[xy[0]+15,xy[1]-20],[xy[0]+20,xy[1]-25],[xy[0]+20,xy[1]-45],[xy[0]+15,xy[1]-50],[xy[0],xy[1]-50]]
    ClickSymbols[4] = [[xy[0]+20,xy[1]-50],[xy[0]+20,xy[1]],[xy[0],xy[1]-30],[xy[0]+25,xy[1]-30]] #4
    ClickSymbols[5] = [[xy[0]+20,xy[1]],[xy[0],xy[1]],[xy[0],xy[1]-20],[xy[0]+15,xy[1]-20],[xy[0]+20,xy[1]-25],[xy[0]+20,xy[1]-40],[xy[0]+15,xy[1]-50],[xy[0]+5,xy[1]-50],[xy[0],xy[1]-45]] #5
    ClickSymbols[6] = [[xy[0]+20,xy[1]-5],[xy[0]+15,xy[1]],[xy[0]+5,xy[1]],[xy[0],xy[1]-5],[xy[0],xy[1]-45],[xy[0]+5,xy[1]-50],[xy[0]+15,xy[1]-50],[xy[0]+20,xy[1]-45],[xy[0]+20,xy[1]-30],[xy[0]+15,xy[1]-25],[xy[0],xy[1]-25]]
    ClickSymbols[7] = [[xy[0],xy[1]-50],[xy[0]+7,xy[1]-30],[xy[0]+15,xy[1]-30],[xy[0],xy[1]-30],[xy[0]+7,xy[1]-30],[xy[0]+20,xy[1]],[xy[0],xy[1]],[xy[0]-3,xy[1]-3]]
    ClickSymbols[8] = [[xy[0],xy[1]-5],[xy[0]+5,xy[1]],[xy[0]+15,xy[1]],[xy[0]+20,xy[1]-5],[xy[0]+20,xy[1]-15],[xy[0]+15,xy[1]-20],[xy[0]+5,xy[1]-20],[xy[0],xy[1]-25],[xy[0],xy[1]-45],[xy[0]+5,xy[1]-50],[xy[0]+15,xy[1]-50],[xy[0]+20,xy[1]-45],[xy[0]+20,xy[1]-25],[xy[0]+15,xy[1]-20],[xy[0]+5,xy[1]-20],[xy[0],xy[1]-15],[xy[0],xy[1]-5]]
    ClickSymbols[9] = [[xy[0],xy[1]-45],[xy[0]+5,xy[1]-50],[xy[0]+15,xy[1]-50],[xy[0]+20,xy[1]-45],[xy[0]+20,xy[1]-5],[xy[0]+15,xy[1]],[xy[0]+5,xy[1]],[xy[0],xy[1]-5],[xy[0],xy[1]-25],[xy[0]+5,xy[1]-30],[xy[0]+20,xy[1]-30]]
    ClickSymbols[10] = [[xy[0]-5,xy[1]-50],[xy[0]-5,xy[1]-50]] #.
    if len(tmp) >= 2 and tmp.count(17) == 1 and  tmp.count(20) != 1:
        sqrtline()
def sqrtline():
    t.penup()
    t.goto(xy[0]-35,xy[1]+10)
    t.pendown()
    t.goto(xy[0],xy[1]+10 )
        
    
            
painter(SymbolsPrint,0)

                    #################
Task = []
def click(x,y):
    if x < -80 and y < -240:
        Task.append('0')
        painter(ClickSymbols,0)
    if x < -80 and y < -160 and y > -240:
        Task.append('1')
        painter(ClickSymbols,1)
    if x < 0 and x > -80 and y < -160 and y > -240:
        Task.append('2')
        painter(ClickSymbols,2)
    if x > 0 and x < 80 and y > -240 and y < -160:
        Task.append('3')
        painter(ClickSymbols,3)
    if x < -80 and y < -80 and y > -160:
        Task.append("4")
        painter(ClickSymbols,4)
    if x < 0 and x > -80 and y < -80 and y > -160:
        Task.append("5")
        painter(ClickSymbols,5)
    if x < 80 and x > 0 and y < -80 and y > -160:
        Task.append("6")
        painter(ClickSymbols,6)
    if x < -80 and y < 0 and y > -80:
        Task.append("7")
        painter(ClickSymbols,7)
    if x < 0 and x > -80 and y < 0 and y > -80:
        Task.append("8")
        painter(ClickSymbols,8)
    if x > 0 and x < 80 and y < 0 and y > -80:
        Task.append ("9")
        painter(ClickSymbols,9)
    if x < 0 and x > -80 and y < -240:
        Task.append(".")
        painter(ClickSymbols,10)
        xy[0]+=5
    if x > 80 and y < -160:
        Task.append("+")
        painter(ClickSymbols,11)
    if x > 80 and y < 0 and y > -80:
        Task.append("*")
        painter(ClickSymbols,12)
    if x > 80 and y < 80 and y > 0:
        Task.append("/")
        painter(ClickSymbols,13)
        painter(ClickSymbols,14)
        painter(ClickSymbols,15)
    if x > 80 and y < -80 and y > -160:
        Task.append("-")
        painter(ClickSymbols,16)
    if x > 0 and x < 80 and y < 80 and y > 0:
        Task.append("sqrt")
        painter(ClickSymbols,17)
        xy[0]+=5
    if x < -80 and y > 0 and y < 80:
        Task.clear()
        turtle.color("black", "white")
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
        update()
    if x < 0 and x > -80 and y < 80 and y > 0:
        xy[0]-=30
        del Task[len(Task)-1]
        t.width(1)
        t.penup()
        turtle.color("black", "white")
        t.goto(xy[0]-7,xy[1]-55)
        t.begin_fill()
        t.goto(xy[0]+27,xy[1]-55)
        t.goto(xy[0]+27,xy[1]+16)
        t.goto(xy[0]-7,xy[1]+16)
        t.goto(xy[0]-7,xy[1]-55)
        t.end_fill()
        t.width(5)
        xy[0]-=30
        update()
    if x < 80 and x > 0 and y < -240:
        Task.append("=")
        painter(ClickSymbols,19)
        painter(ClickSymbols,20)
        main()




def main():
    xy = [-150,140]
    a = ''
    b = ''
    act = ''
    if Task.count('+') == 1:
        act = '+'
        index1 = Task.index('+')
        index0 = 0
    if Task.count('-') == 1:
        act = '-'
        index0 = 0
        index1 = Task.index('-')
    if Task.count('*') == 1:
        act = '*'
        index0 = 0
        index1 = Task.index('*')
    if Task.count('/') == 1:
        act = '/'
        index0 = 0
        index1 = Task.index('/')
    if Task.count('sqrt') == 1:
        act = 'sqrt'
        index1 = len(Task) - 1
        index0 = 1
    ########################
    for i in range(index0, index1):
        a += Task[i]
    if a.count('.') == 1:
        a = float(a)
    else:
        a = int(a)
    ########################
    if len(Task) - 1 != index1:
        for i in range(index1 + 1, len(Task) - 1):
            b += Task[i]
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
        if b != 0:
            c = a / b
            c = str(c)
        else:
            painter(ClickSymbols,21)
            painter(ClickSymbols,22)
            painter(ClickSymbols,23)
            painter(ClickSymbols,24)
            painter(ClickSymbols,25)
            c= ''
    if act == '*':
        c = a * b
        c = str(c)
    if act == 'sqrt':
        c = math.sqrt(a)
        c = str(c)
    if len(c) >= 2:
        if c[-1] == '0' and c[-2] == '.':
            c = c[:-2]
    if len(c) > 9:
        c = c[:12]
    tmp.append(999)
    ########################
    for i in range(len(c)):
        if c[i] == '0':
            painter(ClickSymbols,0)
        if c[i] == '1':
            painter(ClickSymbols,1)
        if c[i] == '2':
            painter(ClickSymbols,2)
        if c[i] == '3':
            painter(ClickSymbols,3)
        if c[i] == '4':
            painter(ClickSymbols,4)
        if c[i] == '5':
            painter(ClickSymbols,5)
        if c[i] == '6':
            painter(ClickSymbols,6)
        if c[i] == '7':
            painter(ClickSymbols,7)
        if c[i] == '8':
            painter(ClickSymbols,8)
        if c[i] == '9':
            painter(ClickSymbols,9)
        if c[i] == '.':
            painter(ClickSymbols,10)
    tmp.append("end")







s.onclick(click, 1)
turtle.mainloop()
