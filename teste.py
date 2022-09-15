import random


def dado(comand):
    # values extraction
    aux = comand.split('-')
    values = aux
    values[0] = int(values[0])
    values[1] = int(values[1])
    # draw number
    random_namber = random.randint(1, values[0])

    # determining result
    if random_namber >= 96:
        result = ('Falha critica!')
    if random_namber > values[1]:
        result = ('Falha')
    if random_namber <= values[1]:
        result = ('Sucesso normal')
    if random_namber <= (values[1]//2):
        result = ('Sucesso solido')
    if random_namber <= (values[1]//5):
        result = ('Sucesso critico')
    if random_namber == 1:
        result = ('Sucesso critico!')
    return result, random_namber


values = dado('100-75')
print(values[0])
print(values[1])
