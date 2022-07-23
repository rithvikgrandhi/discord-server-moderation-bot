import os
import discord
import asyncio
from discord.ext import commands
from discord.ext import tasks
from discord.utils import get
from webserver import keep_alive

######################################################################

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix=".", intents=intents)

######################################################################
@client.event  # check if bot is ready
async def on_ready():
    print('Bot online')

######################################################################

@client.command()
async def ping(ctx):
    await ctx.send(f"Ping: {round(client.latency * 1000)} ms")

######################################################################

@client.command(name='topper')
async def topper(ctx):
    await ctx.send("that is <@708719821226901534>")

######################################################################

@client.command()
async def hello(ctx):
    await ctx.send(f'Hello {ctx.author.mention}')
    await ctx.author.send("hello,I hope you are doing good")

######################################################################

@client.command()
async def greet(ctx, name, *, greeting):
    await ctx.send(f"{greeting} {name}")

######################################################################

@client.command()
async def noob(ctx):
    await ctx.send("no you")

######################################################################

@client.command()
async def pride(ctx):
    await ctx.send(
        "https://tenor.com/view/pes-pesuniversity-pesu-may-the-pride-of-pes-may-the-pride-of-pes-be-with-you-gif-21274060"
    )

######################################################################

@client.command()
async def god(ctx):
    await ctx.send("that is <@676050443180179468>")

######################################################################

#clear command
@client.command(aliases=['purge', 'p'])
async def clear(ctx, amount=1):
    perms = ctx.channel.permissions_for(ctx.author)
    if perms.manage_messages:
        await ctx.channel.purge(limit=amount + 1)
    else:
        await ctx.send("Don't have permission to delete messages here")

######################################################################

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Required arguments not given")

######################################################################

@client.command(aliases=["mc"])
async def message_count(ctx, channel: discord.TextChannel = None):
    channel = channel or ctx.channel
    await ctx.send("counting")
    count = 0
    async for _ in channel.history(limit=None):
        count += 1
    await ctx.send(f"There were {count} messages in {channel.mention}")

######################################################################

@client.event
async def on_message(message):
    if message.channel.id == 889139570304757780 and (message.content != ":hmmlurk:" and message.content!='<a:hmmlurk:869808170804068362>') and message.author!=client.user:
        await message.channel.purge(limit=1)

    await client.process_commands(message)

######################################################################

#server information command
@client.command()
async def serverinfo(ctx):
    name = ctx.guild.name
    description = ctx.guild.description
    region = ctx.guild.region
    icon = ctx.guild.icon_url
    memberCount = ctx.guild.member_count
    owner = ctx.guild.owner

    embed = discord.Embed(title=name + "Server Information",
                          description=description,
                          color=discord.Color.random())
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Description", value=description, inline=False)
    embed.add_field(name="Owner", value=owner, inline=False)
    embed.add_field(name="Region", value=region, inline=False)
    embed.add_field(name="Member count", value=memberCount, inline=False)
    await ctx.send(embed=embed)

######################################################################

#kick command
@client.command()
@commands.has_role(834694539142103041)
async def kick(ctx, member: discord.Member, *, reason="No reason given"):
    await member.send("You were kicked from " + ctx.guild.name + ". Reason: " +
                      reason)
    await member.kick(reason=reason)


@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You don't have the permssion to use this command")

######################################################################

#ban command
@client.command()
@commands.has_role(834694539142103041)
async def ban(ctx, member: discord.Member, *, reason="No reason given"):
    await member.send("You were banned from " + ctx.guild.name + ". Reason: " +
                      reason)
    await member.ban(reason=reason)


@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You don't have the permssion to use this command")

######################################################################

#unban command
@client.command()
@commands.has_role(834694539142103041)
async def unban(ctx, *, member):
    banned_members = await ctx.guild.bans()
    for person in banned_members:
        user = person.user
        if member == str(user):
            await ctx.guild.unban(user)


@unban.error
async def unban_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You don't have the permssion to use this command")

######################################################################

#role giving command
@client.command(pass_context=True)
@commands.has_role(834694539142103041)
async def giveRole(ctx, member: discord.Member, role: discord.Role):
    await member.add_roles(role)


@giveRole.error
async def giveRole_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You don't have the permssion to use this command")

######################################################################
snipe_message_author = {}
snipe_message_content = {}


@client.event
async def on_message_delete(message):
    snipe_message_author[message.channel.id] = message.author
    snipe_message_content[message.channel.id] = message.content
    channellogs = client.get_channel(891551602509488128)
    embed = discord.Embed(title=str(message.author) +
                          " deleted the message in " + str(message.channel),
                          color=discord.Color.red())
    embed.add_field(name="Message:", value=message.content, inline=False)
    await channellogs.send(embed=embed)

    await asyncio.sleep(120)

    del snipe_message_author[message.channel.id]
    del snipe_message_content[message.channel.id]

######################################################################

@client.command(name='snipe')
async def snipe(ctx):
    channel = ctx.channel
    try:  #This piece of code is run if the bot finds anything in the dictionary
        em = discord.Embed(name=f"Last deleted message in #{channel.name}",
                           description=snipe_message_content[channel.id],
                           color=discord.Color.random())
        em.set_footer(
            text=f"This message was sent by {snipe_message_author[channel.id]}"
        )
        await ctx.send(embed=em)
    except:  #This piece of code is run if the bot doesn't find anything in the dictionary
        await ctx.send(
            f"There are no recently deleted messages in #{channel.name}")


#00000000000000000000000000000000000000000000000000000000000000000

@client.event
async def on_message_edit(before, after):
    channellogs = client.get_channel(891551602509488128)
    embed = discord.Embed(title=str(before.author) +
                          " edited the message in " + str(before.channel),
                          color=discord.Color.blue())
    embed.add_field(name="Before:", value=before.content, inline=False)
    embed.add_field(name="After:", value=after.content, inline=False)
    await channellogs.send(embed=embed)

######################################################################

#changing nicknames command
@client.command()
async def nick(ctx, member: discord.Member, *, newname: str):
    # Gets permissions that the message sender has
    perms = ctx.channel.permissions_for(ctx.author)
    if perms.manage_nicknames:
        # If the sender can edit nicknames, edit
        await member.edit(nick=newname)
    else:
        await ctx.send("Don't  have permissions to change nicknames")

######################################################################

@client.event
async def on_voice_state_update(member, before, after):
    channellogs = client.get_channel(891551602509488128)
    if (not before.channel and after.channel):
        embed = discord.Embed(title="someone has joined vc",
                              color=discord.Color.green())
        embed.add_field(name="Username:", value=member)
        await channellogs.send(embed=embed)

######################################################################

@client.command()
# @commands.has_role()
async def spam(ctx):
    if (ctx.author.id == 760161883336081408
            or ctx.author.id == 764118123330273330 or ctx.author.id==793111567184297985):
      emoji = discord.utils.get(client.emojis, name = 'hypersweat')
      for i in range(0,5):
        msg1=(str(emoji)+str(emoji)+str(emoji)+str(emoji)+str(emoji)+str(emoji)+str(emoji)+str(emoji)+str(emoji)+str(emoji)+str(emoji)+str(emoji)+str(emoji)+str(emoji)+str(emoji)+str(emoji)+str(emoji))
        await ctx.send(msg1)

 ######################################################################

@client.event
async def on_member_join(member):

    await member.send(f" Hi {member.mention}, welcome to PES media server. Select your cycle in #🗝️get-roles and you'll get access to the important docs of your courses. You get the role by selecting the appropriate emoji as reaction. \n Please note that we do not promote plagiarism on this server (aka you can't ask assignment answers). ||mainly cuz we don't want to be held responsible for it || \n If you find something missing in the docs or your teacher sent you some other reference material, you can ping any of the mods or admins.")
    
    channellogs2 = client.get_channel(891551602509488128)
    embed = discord.Embed(title="someone has joined the server", description=member,color=discord.Color.gold())
    embed.add_field(name="Username: ", value=member.mention)
    
    await channellogs2.send(embed=embed)

######################################################################

@client.command()
async def assemble(ctx):
    if (ctx.author.id == 760161883336081408
            or ctx.author.id == 764118123330273330):
        await ctx.send("***Avengers, ASSEMBLE!***")
        await ctx.send(
            "<@699646699177639936> <@764118123330273330>  <@760161883336081408> <@738685698206597171> <@793111567184297985>"
        )

######################################################################

@client.command(aliases=['C','c'])
async def count(ctx,*, role:str=""):
    if(role == ""):
        await ctx.channel.send(f"We have **{ctx.guild.member_count}** people in this server")
    else:
        try:
            ROLE=ctx.guild.get_role(int(role))
            await ctx.channel.send(f"**{len(ROLE.members)}** people have the role **{ROLE.name}**")
            
        except:
            guild=ctx.guild
            thisRole = []
            thisRole.append(get(ctx.guild.roles, name=role))
            count = 0
            for member in guild.members:
                boolean = True
                for roles in thisRole:
                    if roles not in member.roles:
                        boolean = False
                    if boolean:
                        count += 1
            await ctx.channel.send(f"**{count}** people have the role **{role}**")


keep_alive()

my_secret = os.environ['TOKEN']

client.run(my_secret)
