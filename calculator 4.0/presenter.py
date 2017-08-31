import view
import answer

Task = []



def act_change(sign):
    """
     Change action sign
    """
    if view.numbers3 == "" and view.act != "":
        del Task[-1]
        for i in range(len(Task)):
            if Task[i] == "+"  or Task[i] ==  "-" or Task[i] ==  "/" or Task[i] ==  "*":
                Task[i] = sign
                break
        return True

def sqrt_fix():
    """
     Fix bug with act_change and sqrt
    """
    if view.act:
        view.act = ""
        view.numbers2 = ""
        view.numbers = ""
        Task.clear()
        for i in range(len(view.numbers1)):
            Task.append(view.numbers1[i])

def numbers_cut():
    """
    max numbers at line(without act's)
    """
    if len(view.numbers) == 14:
        del Task[-1]
        view.numbers = view.numbers[:-1]


def new_start(value):
    """
    New started without pressing the "Clear" button
    """
    if value == "act":
        if view.numbers3 == '= Еrror':
            view.numbers = "0"
            view.numbers2 = ""
            view.numbers3 = ""
            view.act = ""
            Task.clear()
            view.drawer()
        elif view.numbers3:
            view.numbers = view.numbers3[2:]
            view.numbers2 = ""
            view.act = ""
            Task.clear()
            for i in range(len(view.numbers3[2:])):
                Task.append(view.numbers[i])
            view.numbers3 = ""
    elif value == "number":
        if view.numbers3:
            view.clearall()
            Task.clear()
    elif value == "sign":
        if view.numbers3:
            view.numbers = view.numbers3[2:]
            view.act = ""
            view.numbers2 = ""
            view.numbers1 = ""
            view.xy = view.xy1
            Task.clear()
            for i in range(len(view.numbers3[2:])):
                Task.append(view.numbers[i])
            view.numbers3 = ""

def zero_checker():
    """
    Fixed bug with zero
    """
    if view.act and not view.numbers1:
        view.numbers1 = "0"

def click_analyzer(lst):
    """
    Analyze clicks and give subsequent commands
    """
    symbol = lst[0]
    value = lst[1]
    if view.numbers == "0":
         view.numbers = ""
         del Task[-1]
    elif view.numbers == "00":
        view.numbers = view.numbers[:-1]
        del Task[-1]

    if value == "number":
        new_start(value)
        Task.append(str(symbol))
        view.numbers += str(symbol)

    elif value == "act":
        new_start(value)
        Task.append(symbol)
        tmp = act_change(symbol)
        actsymbol = symbol
        if symbol == "*":
            actsymbol = "x"
        elif symbol == "/":
            actsymbol = "÷"
        view.act = actsymbol + " "
        if tmp != True:
            view.numbers1 = view.numbers
            view.numbers = ""
        view.xy = view.xy2


    elif symbol == view.DOT:
        if len(view.numbers) == 0:
            Task.append('0')
            view.numbers+= "0"
        if view.numbers[-1] != ".":
            Task.append(".")
            view.numbers += "."
    elif symbol == view.SIGN_CHANGE:
        new_start("sign")
        view.numbers+="1"
        if view.numbers1 == "":
            if float(view.numbers) > 0:
                Task.insert(0,"-")
                view.numbers = "-" + view.numbers
            elif float(view.numbers) < 0:
                Task[0] = ""
                view.numbers = view.numbers[1:]
        elif view.numbers1 != "":
            if float(view.numbers) > 0:
                sign = "-"
                task_sign = "-"
            else:
                view.numbers = view.numbers[1:]
                sign = ""
                task_sign = ""
            for i in range(len(Task)):
                if Task[i] == "+" or Task[i] == "minus" or Task[i] == "*" or Task[i] == "/":
                    Task.insert(i+1, task_sign)
                    break
            view.numbers =str(sign) + view.numbers
        view.numbers = view.numbers[:-1]

    elif symbol == view.CLEAR:
        Task.clear()
        view.clearall()

    elif symbol == view.BACKSPACE:
        if len(Task) != 0:
            del Task[-1]
        view.clearonce()

    elif symbol == view.COLOR:
        view.color_change()

    elif symbol == view.GRID:
        view.change_grid()

    elif symbol == view.SQRT or symbol == view.SUM:
        if Task:
            if symbol == view.SQRT:
                new_start("act")
                sqrt_fix()
                Task.append("sqrt")
                view.numbers2 = view.numbers
                view.act = "√ "
            Task.append("=")
            view.numbers2 = view.numbers
            view.numbers3 = "= "
            view.numbers3 += answer.search_answer(Task)

            if view.numbers1 == "":
                view.numbers1 = "0"
            if not view.act:
                view.numbers1 = view.numbers
                view.numbers2 = ""
                view.numbers = ""

    if view.numbers == "00":
        view.numbers = view.numbers[:-1]
        del Task[-1]
    zero_checker()
    if Task.count("sqrt") == 1:
        view.numbers1 = ""
    numbers_cut()
    view.drawer()
    click_analyzer(view.main_cycle())

view.drawer()
click_analyzer(view.main_cycle())