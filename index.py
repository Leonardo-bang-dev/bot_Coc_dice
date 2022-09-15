import random
import discord
from discord.ext import commands

# fuction


def dado(comand):
    # values extraction
    aux = comand.split('-')
    values = aux
    values[0] = int(values[0])
    values[1] = int(values[1])
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
    return result, random_namber, fail


bot = commands.Bot("!")


@bot.event
async def on_ready():
    print(f'Estou conectado como {bot.user}')


@bot.command(name='d')
async def mandar_oi(ctx, *expression):
    expression = ''.join(expression)
    result = dado(expression)
    await ctx.send(f'{result[0]} | {result[1]} | {result[2]}')

bot.run("NDY0NjEyMDk3MjM4NzYxNDcz.GYlqsK.Iasw8NpTBInbHxLjd50OsX9KgoKQDj86vgPX7I")
