import math
import model


def search_answer():
    slog1 = ''
    slog2 = ''
    act = ''
    if model.Task.count('+') == 1:
        act = '+'
        index1 = model.Task.index('+')
        index0 = 0
    elif model.Task.count('-') == 1:
        act = '-'
        index0 = 0
        index1 = model.Task.index('-')
    elif model.Task.count('*') == 1:
        act = '*'
        index0 = 0
        index1 = model.Task.index('*')
    elif model.Task.count('/') == 1:
        act = '/'
        index0 = 0
        index1 = model.Task.index('/')
    elif model.Task.count('sqrt') == 1:
        act = 'sqrt'
        index1 = len(model.Task) - 2
        index0 = 0
    else:
        index1 = 0
        index0 = 0
        answer = "error"
        return answer
    ########################
    for i in range(index0, index1):
        slog1 += model.Task[i]
    if slog1.count("minus") == 1:
        slog1 = slog1[5:len(slog1):]
        slog1 = "-" + slog1
    if slog1.count('.') == 1:
        slog1 = float(slog1)
    else:
        slog1 = int(slog1)
    ########################
    if model.Task.count("sqrt") == 0:
        for i in range(index1 + 1, len(model.Task) - 1):
            slog2 += model.Task[i]
        if slog2.count("minus") == 1:
            slog2 = slog2[5:len(slog2):]
            slog2 = "-" + slog2
        if slog2.count('.') == 1:
            slog2 = float(slog2)
        else:
            slog2 = int(slog2)
            ########################
    if act == '+':
        answer = slog1 + slog2
        answer = str(answer)
    if act == '-':
        answer = slog1 - slog2
        answer = str(answer)
    if act == '/':
        if slog2 != 0:
            answer = slog1 / slog2
            answer = str(answer)
        else:
            answer = "error"
    if act == '*':
        answer = slog1 * slog2
        answer = str(answer)
    if act == 'sqrt':
        if slog1 > 0:
            answer = math.sqrt(slog1)
            answer = str(answer)
        else:
            answer = "error"
    if len(answer) >= 2:
        if answer[-1] == '0' and answer[-2] == '.':
            answer = answer[:-2]
    if len(answer) > 9:
        if answer.count(".") == 1:
            answer = answer[:10]
        else:
            answer = answer[:9]
    return answer
