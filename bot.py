import discord
import os
import requests
import json

import datetime

VERSION    = os.environ['VERSION']
TOKEN      = os.environ['DISCORD_TOKEN']
CHANNEL_ID = os.environ['DISCORD_CHANNEL_ID']


client = discord.Client()

@client.event
async def on_ready():
    print('Start bot')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == "/help":
        my_text = get_help_text()
        await message.channel.send(my_text)
    if message.content == "/version":
        await message.channel.send("Bot Version: " + str(VERSION) + "\n" )
    if message.content == "/pp":
        await message.channel.send(message.channel, file=discord.File("img/pp.gif","pp.gif"))

def get_help_text():
    res = "Pastime Bot ver" + str(VERSION) + "\n"
    res += "[コマンド一覧]\n"
    res += "/help\t\t ヘルプを表示\n"
    res += "/pp\t\t\t God Command\n"
    return res

def get_next_pizza_party():
    now = datetime.datetime.now()
    if now.weekday() == 5:
        return "Today!"
    if now.weekday() == 4:
        return "Tomorrow!"
    else:
        np = now + datetime.timedelta(days=(5-now.weekday())%7)
        return np.strftime("%Y/%M/%D (Sat) !")

client.run(TOKEN)
