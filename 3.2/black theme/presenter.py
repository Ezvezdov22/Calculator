import view
import model
import turtle
import answer

s = turtle.Screen()
previous = []

view.painter(model.SymbolsPrint, 0)


def print_answer(answer):
    model.last.append("end")
    for i in range(len(answer)):
        if answer[i] == '.':
            model.last.append(".")
            view.painter(model.ClickSymbols, 10)
        elif answer[i] == '-':
            view.painter(model.ClickSymbols, 24)
        else:
            view.painter(model.ClickSymbols, int(answer[i]))
        model.update()
        if model.last[-1] == ".":
            model.last.append("end")
    if model.last[-2] != "minus":
        model.Task.clear()
        model.last.clear()


def previous_def():
    if len(model.Task) == 0 and len(model.last) == 0 and len(previous) == 1:
        view.clearall()
        model.xy = [-150, 300]
        model.last.append(999)
        model.update()
        for i in range(len(previous[-1])):
            print(model.last)
            model.Task.append(previous[-1][i])
            if previous[-1][i] == '.':
                model.last.append(".")
                view.painter(model.ClickSymbols, 10)
            elif previous[-1][i] == '-':
                view.painter(model.ClickSymbols, 24)
            else:
                view.painter(model.ClickSymbols, int(previous[-1][i]))
            if model.last.count(".") == 1:
                del model.last[-1]
            model.update()
def new_start():
    if len(model.Task) == 1 and len(model.last) == 1 and len(previous) == 1:
        view.clearall()
        model.xy = [-180,300]
        model.update()

def del_act():
    if model.Task[-1] == "*" or model.Task[-1] == "minus" or model.Task[-1] == "/" or model.Task[-1] == "+":
        del model.Task[-1]
        model.xy = [-150,220]
        view.clearonce(model.xy)

def click_search():
    def click(x, y):
        if x < -80 and y < -240:
            model.last.append(0)
            model.Task.append('0')
            new_start()
            view.painter(model.ClickSymbols, 0)
            model.update()
        if x < -80 and y < -160 and y > -240:
            model.last.append(1)
            model.Task.append('1')
            new_start()
            view.painter(model.ClickSymbols, 1)
            model.update()
        if x < 0 and x > -80 and y < -160 and y > -240:
            model.last.append(2)
            model.Task.append('2')
            new_start()
            view.painter(model.ClickSymbols, 2)
            model.update()
        if x > 0 and x < 80 and y > -240 and y < -160:
            model.last.append(3)
            model.Task.append('3')
            new_start()
            view.painter(model.ClickSymbols, 3)
            model.update()
        if x < -80 and y < -80 and y > -160:
            model.last.append(4)
            model.Task.append("4")
            new_start()
            view.painter(model.ClickSymbols, 4)
            model.update()
        if x < 0 and x > -80 and y < -80 and y > -160:
            model.last.append(5)
            model.Task.append("5")
            new_start()
            view.painter(model.ClickSymbols, 5)
            model.update()
        if x < 80 and x > 0 and y < -80 and y > -160:
            model.last.append(6)
            model.Task.append("6")
            new_start()
            view.painter(model.ClickSymbols, 6)
            model.update()
        if x < -80 and y < 0 and y > -80:
            model.last.append(7)
            model.Task.append("7")
            new_start()
            view.painter(model.ClickSymbols, 7)
            model.update()
        if x < 0 and x > -80 and y < 0 and y > -80:
            model.last.append(8)
            model.Task.append("8")
            new_start()
            view.painter(model.ClickSymbols, 8)
            model.update()
        if x > 0 and x < 80 and y < 0 and y > -80:
            model.last.append(9)
            model.Task.append("9")
            new_start()
            view.painter(model.ClickSymbols, 9)
            model.update()
        if x < 0 and x > -80 and y < -240:
            if len(model.Task) == 0:
                model.Task.append('0')
                model.last.append(0)
                view.painter(model.ClickSymbols, 0)
                model.update()
            model.Task.append(".")
            model.last.append(10)
            view.painter(model.ClickSymbols, 10)
            model.update()
        if x > 80 and y < -240:
            previous_def()
            if len(model.Task) == 0 and len(model.last) == 0 and len(previous) == 1:
                '''
                Добавление "-" к previous
                '''
                if previous[-1][0] != "-":
                    previous[-1] = "-" + previous[-1]
                else:
                    previous[-1] = previous[-1][1:]

            if model.Task.count('+') == 0 and model.Task.count("minus") == 0 and model.Task.count('*') == 0 and model.Task.count('/') == 0:
                view.clearall()
                model.xy = [-180,300]
                model.update()
                model.Task.insert(0, "-")
                if len(model.Task) >= 2:
                    if model.Task[0] == model.Task[1]:
                        del model.Task[0]
                        del model.Task[0]
                model.last.append("minus")
                print(model.Task)
                print_answer(model.Task)
            else:
                if model.Task.count("+") == 1:
                    index = model.Task.index("+")
                elif model.Task.count("minus") == 1:
                    index = model.Task.index("minus")
                elif model.Task.count("*") == 1:
                    index = model.Task.index("*")
                elif model.Task.count("/") == 1:
                    index = model.Task.index("/")
                view.clearline()
                model.xy = [-150, 220]
                model.last.append("minus")
                model.update()
                model.Task.insert(index+1, "-")
                cut = model.Task[index+1:]
                print_answer(cut)
        if x > 80 and y < -160 and y > -240:
            previous_def()
            del_act()
            model.Task.append("+")
            model.last.append("act")
            view.painter(model.ClickSymbols, 11)
            model.update()
        if x > 80 and y < 0 and y > -80:
            previous_def()
            del_act()
            model.Task.append("*")
            model.last.append("act")
            view.painter(model.ClickSymbols, 12)
            model.update()
        if x > 80 and y < 80 and y > 0:
            previous_def()
            del_act()
            model.Task.append("/")
            model.last.append("act")
            view.painter(model.ClickSymbols, 13)
            view.painter(model.ClickSymbols, 14)
            view.painter(model.ClickSymbols, 15)
            model.update()
        if x > 80 and y < -80 and y > -160:
            previous_def()
            del_act()
            model.Task.append("minus")
            model.last.append("act")
            view.painter(model.ClickSymbols, 16)
            model.update()
        if x < -80 and y > 0 and y < 80:
            model.Task.clear()
            previous.clear()
            view.clearall()
            model.update()
        if x < 0 and x > -80 and y < 80 and y > 0:
            model.xy[0] -= 30
            del model.Task[-1]
            view.clearonce(model.xy)
            model.xy[0] -= 30
            model.update()

        if x < 80 and x > 0 and y < -240 or x > 0 and x < 80 and y < 80 and y > 0:
            previous_def()
            if x > 0 and x < 80 and y < 80 and y > 0:
                model.Task.append("sqrt")
            model.Task.append("=")
            model.last.append("=")
            view.painter(model.ClickSymbols, 17)
            view.painter(model.ClickSymbols, 18)
            model.update()
            previous.clear()
            previous.append(answer.search_answer(model.Task))
            if previous[-1] != "error":
                print_answer(previous[-1])
            else:
                view.painter(model.ClickSymbols, 19)
                view.painter(model.ClickSymbols, 20)
                view.painter(model.ClickSymbols, 21)
                view.painter(model.ClickSymbols, 22)
                view.painter(model.ClickSymbols, 23)

        turtle.update()
    s.onclick(click, 1)
    turtle.mainloop()

click_search()