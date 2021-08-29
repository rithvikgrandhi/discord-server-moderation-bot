import os
import discord
from discord.ext import commands
from webserver import keep_alive

#000000000000000000000000000000000

client = commands.Bot(command_prefix="pes ")
@client.event
async def on_ready():
    print("the bot is ready")
@client.command()
async def ping(ctx):
    await ctx.send(f"Ping: {round(client.latency * 1000)} ms") 
@client.command()
async def hello(ctx):
    await ctx.send("Hi")

@client.command()
async def noob(ctx):
    await ctx.send("no you")
    
@client.command()
async def pride(ctx):
   await ctx.send("https://tenor.com/view/pes-pesuniversity-pesu-may-the-pride-of-pes-may-the-pride-of-pes-be-with-you-gif-21274060")

@client.command()
async def god(ctx):
    await ctx.send("that is <@676050443180179468>")

snipe_message_author = {}
snipe_message_content = {}

@client.event
async def on_message_delete(message):
     snipe_message_author[message.channel.id] = message.author
     snipe_message_content[message.channel.id] = message.content
     
     del snipe_message_author[message.channel.id]
     del snipe_message_content[message.channel.id]

@client.command(name = 'snipe')
async def snipe(ctx):
    channel = ctx.channel
    try: #This piece of code is run if the bot finds anything in the dictionary
        em = discord.Embed(name = f"Last deleted message in #{channel.name}", description = snipe_message_content[channel.id])
        em.set_footer(text = f"This message was sent by {snipe_message_author[channel.id]}")
        await ctx.send(embed = em)
    except: #This piece of code is run if the bot doesn't find anything in the dictionary
        await ctx.send(f"There are no recently deleted messages in #{channel.name}")

#000000000000000000000000000000000000000000000000000000000000000000

@client.event
async def on_message(message):
    #
    if (not message.author.bot):

    
      if("chad" in str(message.content).lower()):
       
        await message.channel.send("if you are looking for chad, it is <@738685698206597171>")
        

    
      if("pride" in str(message.content).lower()):
        await message.channel.send("https://tenor.com/view/pes-pesuniversity-pesu-may-the-pride-of-pes-may-the-pride-of-pes-be-with-you-gif-21274060")
    await client.process_commands(message)

#00000000000000000000000000000000000000000000000000000000000000000

@client.command()
async def mute(ctx, member : discord.Member = None):

    if member is None:
        await ctx.send('Please pass in a valid user')
        return

    await member.add_roles('mooted')

    await ctx.send(f'{str(member)} was muted!')
@client.event
async def on_command_error(ctx, error):
    await ctx.send(error)
    await (ctx.send("{} made this error".format(ctx.author.mention)))
#000000000000000000000000000000000000000000000000000000000000000000
@client.event  # check if bot is ready
async def on_ready():
    print('Bot online')
keep_alive()


# command for bot to join the channel of the user, if the bot has already joined and is in a different channel, it will move to the channel the user is in


##00000000000000000000000000000000000000000000000000000000000000000

my_secret = os.environ['token2']
client.run(my_secret)