import math

def search_answer(task):
    slog = ''
    mission = ""
    task = task[:-1]
    if len(task) > 2:
        if task[-1] == "0" and task[-2] == "/":
            return "error"
    if task.count("sqrt") == 1:
        task = task[:-1]
        for i in range(len(task)):
            slog+= task[i]
        slog = float(slog)
        if slog > 0:
            answer = str(math.sqrt(slog))
        else:
            return "error"

    else:
        for i in range(len(task)):
            if task[i] != "minus":
                mission+= task[i]
            else:
                mission+= "-"
        answer = str(eval(mission))
    if len(answer) >= 2:
        if answer[-1] == '0' and answer[-2] == '.':
            answer = answer[:-2]
    if len(answer) > 9:
        if answer.count(".") == 1:
            answer = answer[:10]
        else:
            answer = answer[:9]
    return answer