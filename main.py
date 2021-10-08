import os
import discord
import asyncio
from discord.ext import commands
from discord.ext import tasks
from discord.utils import get
from webserver import keep_alive

#000000000000000000000000000000000
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix="pes ",intents=intents)

@client.event
async def on_ready():
    print("the bot is ready")

@client.command()
async def ping(ctx):
    await ctx.send(f"Ping: {round(client.latency * 1000)} ms") 

@client.command()
async def ping(ctx):
    await ctx.send(f"Ping: {round(client.latency * 1000)} ms")

@client.command()
async def hello(ctx):
    await ctx.send(f'Hello {ctx.author.mention}')
    await ctx.author.send("hello,I hope you are doing good")

@client.command()
async def greet(ctx, name, *,greeting):
    await ctx.send(f"{greeting} {name}")

@client.command()
async def noob(ctx):
    await ctx.send("no you")
    
@client.command()
async def pride(ctx):
   await ctx.send("https://tenor.com/view/pes-pesuniversity-pesu-may-the-pride-of-pes-may-the-pride-of-pes-be-with-you-gif-21274060")

@client.command()
async def god(ctx):
    await ctx.send("that is <@676050443180179468>")
    
#clear command
@client.command(aliases=['purge','p','c'])
async def clear(ctx, amount=1):
    perms = ctx.channel.permissions_for(ctx.author)
    if perms.manage_messages:
        await ctx.channel.purge(limit=amount+1)
    else: 
        await ctx.send("Don't  have permission to delete messages here")
    

#changing nicknames command
@client.command()
async def nick(ctx, member: discord.Member, *,newname: str):
    # Gets permissions that the message sender has
    perms = ctx.channel.permissions_for(ctx.author)
    if perms.manage_nicknames:
        # If the sender can edit nicknames, edit
        await member.edit(nick=newname)
    else: 
        await ctx.send("Don't  have permissions to change nicknames")

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Required arguments not given")
        
#server information command
@client.command()
async def serverinfo(ctx):
    name=ctx.guild.name
    description=ctx.guild.description
    region=ctx.guild.region
    icon=ctx.guild.icon_url
    memberCount=ctx.guild.member_count
    owner=ctx.guild.owner

    embed=discord.Embed(title=name+"Server Information",description=description,color=discord.Color.blue())
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Description",value=description,inline=False)
    embed.add_field(name="Owner",value=owner,inline=False)
    embed.add_field(name="Region",value=region,inline=False)
    embed.add_field(name="Member count",value=memberCount,inline=False)
    await ctx.send(embed=embed)

#kick command
@client.command()
@commands.has_role(834694539142103041)
async def kick(ctx,member:discord.Member,*,reason="No reason given"):
    await member.send("You were kicked from "+ctx.guild.name+". Reason: "+reason)
    await member.kick(reason=reason)

@kick.error
async def kick_error(ctx,error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You don't have the permssion to use this command")

#ban command
@client.command()
@commands.has_role(834694539142103041)
async def ban(ctx,member:discord.Member,*,reason="No reason given"):
    await member.send("You were banned from "+ctx.guild.name+". Reason: "+reason)
    await member.ban(reason=reason)

@ban.error
async def ban_error(ctx,error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You don't have the permssion to use this command")

#unban command
@client.command()
@commands.has_role(834694539142103041)
async def unban(ctx,*,member):
    banned_members=await ctx.guild.bans()
    for person in banned_members:
        user=person.user
        if member==str(user):
            await ctx.guild.unban(user)

@unban.error
async def unban_error(ctx,error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You don't have the permssion to use this command")

#role giving command
@client.command(pass_context=True)
@commands.has_role(834694539142103041) 
async def giveRole(ctx,member:discord.Member,role:discord.Role):
    await member.add_roles(role)

@giveRole.error
async def giveRole_error(ctx,error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You don't have the permssion to use this command")


snipe_message_author = {}
snipe_message_content = {}

@client.event
async def on_message_delete(message):
     snipe_message_author[message.channel.id] = message.author
     snipe_message_content[message.channel.id] = message.content
     channellogs=client.get_channel(891551602509488128)
     embed=discord.Embed(title=str(message.author)+"deleted the message in "+str(message.channel),color=discord.Color.red())
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
    embed=discord.Embed(title=str(before.author)+"edited the message in "+str(before.channel),color=discord.Color.blue())
    embed.add_field(name="Before:",value=before.content,inline=False)
    embed.add_field(name="After:",value=after.content,inline=False)
    await channellogs.send(embed=embed)

#000000000000000000000000000000000000000000000000000000000000000000

@client.event
async def on_voice_state_update(member, before, after):
	channellogs=client.get_channel(891551602509488128)
	if(not before.channel and after.channel):
		embed=discord.Embed(title="someone has joined vc",color=discord.Color.green())
		embed.add_field(name="Username:",value=member)
		await channellogs.send(embed=embed)


@client.event  # check if bot is ready
async def on_ready():
    print('Bot online')
keep_alive()


# command for bot to join the channel of the user, if the bot has already joined and is in a different channel, it will move to the channel the user is in


##00000000000000000000000000000000000000000000000000000000000000000

my_secret = os.environ['token2']
client.run(my_secret)
