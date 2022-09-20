import random


def dado(comand):
    # values extraction
    if len(comand) > 6:
        aux = comand.replace('/', '-')
        aux = aux.split('-')
    if len(comand) <= 6:
        aux = comand.split('-')

    values = aux
    values[0] = int(values[0])
    values[1] = int(values[1])
    if len(comand) > 6:
        values[2] = int(values[2])

    if len(comand) > 6:
        values[1] = values[1] - values[2]

    # draw number
    random_namber = random.randint(1, values[0])

    # Fail value
    if values[1] >= 50:
        fail = 100
    elif values[1] < 50:
        fail = 96

    # determining result
    if random_namber >= fail:
        result = ('Falha critica!')
    elif random_namber > values[1]:
        result = ('Falha')
    if random_namber <= values[1]:
        result = ('Sucesso normal')
    if random_namber <= (values[1]//2):
        result = ('Sucesso solido')
    if random_namber <= (values[1]//5):
        result = ('Sucesso extremo')
    if random_namber == 1:
        result = ('Sucesso critico!')
    return result, random_namber, fail, values[1]


values = dado('100-75')

print(f'{values[0]} | {values[1]} | {values[2]} | {values[3]}')
