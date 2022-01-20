import discord
from discord.ext import commands  

client = commands.Bot(command_prefix = "!")

@client.command()

async def play(ctx, url : str):
    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='general')
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if not voice.is_connected():
        await voiceChannel.connect()

@client.command()

async def leave (ctx):
    voice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("el bot no esta conectado al canal de voz")    

@client.command()
async def  pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("no se esta reproduciendo")

@client.command()

async def resume (ctx):
     voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

     if voice.is_pause():
         voice.resume()
     else:
         await ctx.send("no esta pausado")

client.command()
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()
    









client.run ('OTMzNDcwODA0NTA5ODc2MjU1.YeiAbg.kXf8T2KWmCkPdNcdXZulZKLWM9Y')

