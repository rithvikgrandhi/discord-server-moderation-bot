import os
import discord
import asyncio
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
     channellogs=client.get_channel(891551602509488128)
     embed=discord.Embed(title=str(message.author)+"deleted the message in "+str(message.channel),color=discord.Color.random())
     embed.add_field(name="Message:",value=message.content,inline=False)
     await channellogs.send(embed=embed)
    
     await asyncio.sleep(120)
    
     del snipe_message_author[message.channel.id]
     del snipe_message_content[message.channel.id]
        

@client.command(name = 'snipe')
async def snipe(ctx):
    channel = ctx.channel
    try: #This piece of code is run if the bot finds anything in the dictionary
        em = discord.Embed(name = f"Last deleted message in #{channel.name}", description = snipe_message_content[channel.id],color=discord.Color.random())
        em.set_footer(text = f"This message was sent by {snipe_message_author[channel.id]}")
        await ctx.send(embed = em)
    except: #This piece of code is run if the bot doesn't find anything in the dictionary
        await ctx.send(f"There are no recently deleted messages in #{channel.name}")

#000000000000000000000000000000000000000000000000000000000000000000

@client.event
async def on_message(message):
    #
    if (not message.author.bot):

    
      
        
      
    
      if("pride" in str(message.content).lower()):
        await message.channel.send("https://tenor.com/view/pes-pesuniversity-pesu-may-the-pride-of-pes-may-the-pride-of-pes-be-with-you-gif-21274060")
    await client.process_commands(message)

#00000000000000000000000000000000000000000000000000000000000000000

    @commands.command(aliases=['e', 'echo'])
    async def echo(self, ctx, dest: discord.TextChannel = None, *, message: str = ''):
        echo_embed = discord.Embed(
            title="Echo", color=0x48BF91, description=self.echo)
        if((self.admin in ctx.author.roles) or (self.mod in ctx.author.roles)):
            if(dest == None):
                await ctx.channel.send(embed=echo_embed)
                return
            attachment = ctx.message.attachments
            if(dest.id == ctx.channel.id):
                await ctx.message.delete()
            # if(message != ''):
            #     sent = await dest.send(message)
            if(len(attachment) != 0):
                await attachment[0].save(attachment[0].filename)
                sent = await dest.send(file=discord.File(attachment[0].filename))
                os.remove(attachment[0].filename)
                if(message != ''):
                    await sent.edit(content=message)
            else:
                await dest.send(content=message)
        else:
            await ctx.channel.send("Sucka you can't do that")
# @client.event

# async def on_message_edit(before,after):
#   channellogs = client.get_channel(891551602509488128)
#   await channellogs.send(str(before.author)+" in "+str(before.channel)+"\nbefore: "+before.content+"\nafter: "+after.content)

@client.event
async def on_message_edit(before,after):
    channellogs=client.get_channel(891551602509488128)
    embed=discord.Embed(title=str(before.author)+"edited the message in "+str(before.channel),color=discord.Color.random())
    embed.add_field(name="Before:",value=before.content,inline=False)
    embed.add_field(name="After:",value=after.content,inline=False)
    await channellogs.send(embed=embed)

#000000000000000000000000000000000000000000000000000000000000000000
@client.event  # check if bot is ready
async def on_ready():
    print('Bot online')
keep_alive()


# command for bot to join the channel of the user, if the bot has already joined and is in a different channel, it will move to the channel the user is in


##00000000000000000000000000000000000000000000000000000000000000000

my_secret = os.environ['token2']
client.run(my_secret)
