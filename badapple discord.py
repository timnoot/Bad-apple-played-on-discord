import asyncio
import time

import discord
from discord.ext import commands

file = open(f"frames/frames.txt", "r", encoding='utf8')
l = file.readlines()
file.close()
framecounter = 1
r = []
dict = {}
count = 0
for i in range(len(l)):
    try:
        int(l[i])
        pass
    except:
        r.append(l[i])
    if len(r) >= 37:
        dict[int(l[count])] = r
        r = []
        count += 38


def image(frame):
    global dict
    l1 = dict[int(frame)]
    em = ""
    for i in l1:
        em = em + i
    return "```" + em + "```"


client1 = commands.Bot(command_prefix='!')
client2 = commands.Bot(command_prefix='owo')
client3 = commands.Bot(command_prefix='owo')
client4 = commands.Bot(command_prefix='owo')
client5 = commands.Bot(command_prefix='owo')
client6 = commands.Bot(command_prefix='owo')
client7 = commands.Bot(command_prefix='owo')
client8 = commands.Bot(command_prefix='owo')
client9 = commands.Bot(command_prefix='owo')
client10 = commands.Bot(command_prefix='owo')
client11 = commands.Bot(command_prefix='owo')
client12 = commands.Bot(command_prefix='owo')
client13 = commands.Bot(command_prefix='owo')
client14 = commands.Bot(command_prefix='owo')
client15 = commands.Bot(command_prefix='owo')

clients = []
clients.append(client1)
clients.append(client2)
clients.append(client3)
clients.append(client4)
clients.append(client5)
clients.append(client6)
clients.append(client7)
clients.append(client8)
clients.append(client9)
clients.append(client10)
clients.append(client11)
clients.append(client12)
clients.append(client13)
clients.append(client14)
clients.append(client15)

TOKENmain = ""
TOKEN2 = ""
TOKEN3 = ""
TOKEN4 = ""
TOKEN5 = ""
TOKEN6 = ""
TOKEN7 = ""
TOKEN8 = ""
TOKEN9 = ""
TOKEN10 = ""
TOKEN11 = ""
TOKEN12 = ""
TOKEN13 = ""
TOKEN14 = ""
TOKEN15 = ""


@client1.command()
async def frame(ctx, frame):
    await ctx.send(image(frame))


@client1.command()
async def start(ctx):
    framecounter = 1

    clients = []
    clients.append(client1)
    clients.append(client2)
    clients.append(client3)
    clients.append(client4)
    clients.append(client5)
    clients.append(client6)
    clients.append(client7)
    clients.append(client8)
    clients.append(client9)
    clients.append(client10)
    clients.append(client11)
    clients.append(client12)
    clients.append(client13)
    clients.append(client14)
    clients.append(client15)
    channels = []
    for i in range(15):
        channels.append(clients[i].get_channel(840150806682664973))  # change this channel id to whatever channel u want
    try:
        await ctx.author.voice.channel.connect()
    except discord.errors.ClientException:
        pass
    guild = ctx.guild
    voice_client: discord.VoiceClient = discord.utils.get(client1.voice_clients, guild=guild)
    audio_source = discord.FFmpegPCMAudio(f"frames/badapple.mp3")
    voice_client.play(audio_source)
    start_time = time.time()
    curclient = 1
    for i in range(2194):
        if curclient >= 15:
            curclient = 1
        if start_time + framecounter * 0.1 <= time.time():
            delay = (((time.time() - start_time) / 0.1) - framecounter) * 0.1
            print(f"delay of {delay} seconds")
            channel = channels[curclient]
            framecounter += 1
            if delay >= 0.3:
                framecounter += 1
            clients[curclient].loop.create_task(channel.send(image(framecounter)))
        else:
            print(f"delay of {(((time.time() - start_time) / 0.1) - framecounter) * 0.1} seconds")
            await asyncio.sleep(abs((((time.time() - start_time) / 0.1) - framecounter) * 0.1))
            channel = channels[curclient]
            clients[curclient].loop.create_task(channel.send(image(framecounter)))
        curclient += 1
        framecounter += 1


loop = asyncio.get_event_loop()
loop.create_task(client1.start(TOKENmain))
loop.create_task(client2.start(TOKEN2))
loop.create_task(client3.start(TOKEN3))
loop.create_task(client4.start(TOKEN4))
loop.create_task(client5.start(TOKEN5))
loop.create_task(client6.start(TOKEN6))
loop.create_task(client7.start(TOKEN7))
loop.create_task(client8.start(TOKEN8))
loop.create_task(client9.start(TOKEN9))
loop.create_task(client10.start(TOKEN10))
loop.create_task(client11.start(TOKEN11))
loop.create_task(client12.start(TOKEN12))
loop.create_task(client13.start(TOKEN13))
loop.create_task(client14.start(TOKEN14))
loop.create_task(client15.start(TOKEN15))

loop.run_forever()

# Made by: timnoot#0001 | inspired by: Lamp | Code: https://bit.ly/2Q6VjIW
