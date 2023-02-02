import json

import discord
import random
from discord.ext import commands
import string


token = 'MTA1NzU5NjU5ODk0OTAwNzM5MA.GpHxYB.wRjO35TtEsLAMM2sMALoEq0D90AMbmr-OWEwnM'
bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())


@bot.event
async def on_message(message):
    if message.channel.name == "арсений":
        if message.author.bot:
            return
        elif {i.lower().translate(str.maketrans("", "", string.punctuation)) \
              for i in message.content.split(' ')}\
                .intersection(set(json.load(open('cenz.json')))) != set():
            await message.delete()
        else:
            await message.channel.send("Марио корнеплод")



@bot.command()
async def start(m, *, a=None):
    if m.channel.name == "арсений":
        if a == 'info':
            await m.send("Я бот Сем Неби, люблю бездельничать")
        elif a == 'help':
            await m.send("Команды легкие, ну типа /sps, /start info, /start starts, /igra 1-3, /hi /start creator, /start")
        elif a == 'starts':
            await m.send("Напиши что-то из этого !start info, !start help")
        elif a is None:
            await m.send("Нет аргумента, напиши !start help")
        elif a == 'creator':
            await m.send("Создатель - @мшкфреде#4413")

@bot.command()
async def igra(l, k=None):
    if l.channel.name == "арсений":
        if k == '1':
            await l.send('Не угадал')
        elif k == '2':
            await l.send("+ ugadal")
        elif k == '3':
            await l.send('NET')
        elif k is None:
            await l.send('После !igra пиши число от 1 до 3')

@bot.command()
async def sps(k):
    if k.channel.name == "арсений":
        await k.send("Луис спс")

@bot.command()
async def hi(h):
    if h.channel.name == "арсений":
        await h.send('Привет ' + str(h.message.author))






bot.run(token)
