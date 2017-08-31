import math

def search_answer(task):
    slog = ''
    mission = ""
    task = task[:-1]
    for i in range(task.count("=")):
        task = task[:-1]
    if task[-1] == "/":
        return "Еrror"
    if task[-1] == "*" or task[-1] == "-" or task[-1] == "+":
        task.append("0")
    if task.count("sqrt") == 1:
        task = task[:-1]
        for i in range(len(task)):
            slog+= task[i]
        slog = float(slog)
        if slog > 0:
            answer = str(math.sqrt(slog))
        else:
            return "Error"
    else:
        for i in range(len(task)):
            mission+= task[i]
        answer = str(eval(mission))
    if len(answer) >= 2:
        if answer[-1] == '0' and answer[-2] == '.':
            answer = answer[:-2]
    if len(answer) > 13:
        if answer.count(".") == 1:
            answer = answer[:10]
        else:
            answer = answer[:9]
    return answer