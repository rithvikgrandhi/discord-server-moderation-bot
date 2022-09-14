import os
import discord
import asyncio
from discord.ext import commands
from discord.utils import get
from webserver import keep_alive

######################################################################
#data
mods = [ ] #roleids

admin_role_id= #roleid


######################################################################

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix=".", intents=intents) #bot prefix


######################################################################
@client.event  # check if bot is ready
async def on_ready():
    print('Bot online')
    await client.change_presence(activity=discord.Game(
        name=""))
    #msg1.start()


channellogs = client.get_channel(#channel_id)

######################################################################

@client.command()
async def ping(ctx):
    await ctx.send(f"Ping: {round(client.latency * 1000)} ms")


######################################################################

@client.command()
@commands.has_any_role("Admin")
async def leaveg(ctx, ):
    guild_name = 'stuff'
    guild = discord.utils.get(client.guilds,
                              name=guild_name)  # Get the guild by name
    if guild is None:
        print("No guild with that name found.")  # No guild found
        return
    await guild.leave()  # Guild found
    await ctx.send(f"I left: {guild.name}!")


###################################################################


@client.command()
@commands.has_any_role("Admin")
async def dm(ctx, i):
    guild = client.get_guild(i)
    guildchannel = guild.system_channel
    invitelink = await guildchannel.create_invite(max_uses=1, unique=True)
    await ctx.send(invitelink)


####################################################################
    
@client.command(aliases=['servers', 'guilds'])
async def guilds_command(ctx):
    if ((ctx.author.id == #mod_ids)):
        await ctx.channel.trigger_typing()

        number = 0
        guilds_details = await client.fetch_guilds(limit=150).flatten()
        await ctx.send("```You have clearance```")
        list1 = []
        for guild_deets in guilds_details:
            number += 1
            list1.append(guild_deets.name)
        await ctx.send(list1)

    else:
        await ctx.send("You are not authorised for this")


######################################################################


#clear command
@client.command(aliases=['purge', 'p'])
@commands.has_any_role("Admin")
async def clear(ctx, amount=1):
    await ctx.channel.purge(limit=amount + 1)

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("Don't have permission to delete messages here")


######################################################################


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Required arguments not given")


######################################################################


@client.command(aliases=["mc"])
@commands.has_any_role("Admin")
async def message_count(ctx, channel: discord.TextChannel = None):
    channel = channel or ctx.channel
    await ctx.send("counting")
    count = 0
    async for _ in channel.history(limit=None):
        count += 1
    await ctx.send(f"There were {count} messages in {channel.mention}")

@message_count.error
async def message_count_error(ctx,error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You can't use this command <:keku:869498061674668112>")
    


########################################################################


# @client.event
# async def on_message(message):
#     if message.reference is not None and message.channel.id == 889139570304757780:
#         await message.channel.purge(limit=1)

#     elif message.channel.id == 889139570304757780 and (
#             message.content != ":hmmlurk:" and message.content !=
#             'https://cdn.discordapp.com/emojis/869808170804068362.gif?size=48&quality=lossless'
#             and message.content != '<a:hmmlurk:869808170804068362>'):
#         await message.channel.purge(limit=1)

#     await client.process_commands(message)


# ######################################################################

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
@commands.has_any_role("Admin")
async def kick(ctx, member: discord.Member, *, reason=None):

    await ctx.guild.kick(member)
    await ctx.send(f'User {member.mention} has been kicked for {reason}')
    await channellogs.send(
        f'User {member.mention} has been kicked for {reason}')


@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You don't have the permssion to use this command")


######################################################################
        
@client.command()
@commands.has_any_role("Admin")
async def ban(ctx, member: discord.User = None, reason=None):
    if member == None or member == ctx.message.author:
        await ctx.channel.send("You cannot ban yourself")
        return
    if reason == None:
        reason = "For being a jerk!"
    message = f"You have been banned from {ctx.guild.name} for {reason}"
    await member.send(message)
    await ctx.guild.ban(member, reason=reason)
    await ctx.channel.send(f"{member} is banned!")


######################################################################


#unban command
@client.command(pass_context=True)
@commands.has_any_role("Admin")
async def unban(ctx, *, member):
    banned_members = await ctx.guild.bans()
    for person in banned_members:
        user = person.user
        if member == str(user):
            await ctx.guild.unban(user)
            ctx.send(member, "is unbanned")
            channellogs.send(member, "is unbanned")


@unban.error
async def unban_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You don't have the permssion to use this command")


######################################################################


#role giving command
@client.command(pass_context=True)
@commands.has_any_role("Admin")
async def giveRole(ctx, member: discord.Member,*, role: discord.Role):
    await member.add_roles(role)
    await ctx.send(f"Gave role **{role}** to **{member.mention}**")


@giveRole.error
async def giveRole_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You don't have the permssion to use this command")


######################################################################
snipe_message_author = {}
snipe_message_content = {}


@client.event
async def on_message_delete(message):
    # if message.contains
    snipe_message_author[message.channel.id] = message.author
    snipe_message_content[message.channel.id] = message.content
    channellogs = client.get_channel(#logs_channel_id)
    embed = discord.Embed(title="someone deleted a message ",
                          color=discord.Color.red())
    embed.add_field(name="Sender:", value=message.author)
    embed.add_field(name='Channel:', value=message.channel.mention)
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

    if before.channel.id == #channel_id:
        before.delete
    channellogs = client.get_channel(#logs_channel_id)
    embed = discord.Embed(title=str(before.author) + " edited a message",
                          color=discord.Color.blue())

    embed.add_field(name="channel", value=before.channel.mention)
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
    channellogs = client.get_channel(#logs_channel_id)
    if (not before.channel and after.channel):
        embed = discord.Embed(title="someone has joined vc",
                              color=discord.Color.green())
        embed.add_field(name="Username:", value=member)
        await channellogs.send(embed=embed)


######################################################################


@client.command()
@commands.has_any_role("Admin")
async def echo(ctx,
               destination: discord.TextChannel = None,
               *,
               message: str = ""):
    if (message == ""):
        await ctx.send("Enter some message to echo")
    else:
        if (destination == None):
            await ctx.send(message)
            await ctx.message.delete()
        else:
            await destination.send(message)
            await ctx.message.delete()


@echo.error
async def echo_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You can't use this command <:keku:869498061674668112>")


##########################################################################################


@client.command()
# @commands.has_role()
async def stress(ctx):
    if (ctx.author.id == #mod1
            or ctx.author.id == #mod_2
            or ctx.author.id == #Mod_3):
        emoji = discord.utils.get(client.emojis, name='hypersweat')
        for i in range(0, 5):
            msg1 = (str(emoji) + str(emoji) + str(emoji) + str(emoji) +
                    str(emoji) + str(emoji) + str(emoji) + str(emoji) +
                    str(emoji) + str(emoji) + str(emoji) + str(emoji) +
                    str(emoji) + str(emoji) + str(emoji) + str(emoji) +
                    str(emoji))
            await ctx.send(msg1)

##########################################################################
@client.event
async def on_member_join(member):

    await member.send(
        f" Hi {member.mention}, welcome to PES media server. Select your cycle in <#get_roles_channel_id> and you'll get access to the important docs of your courses. You get the role by selecting the appropriate emoji as reaction. \n Please note that we do not promote plagiarism on this server (aka you can't ask assignment answers). ||mainly cuz we don't want to be held responsible for it || \n If you find something missing in the docs or your teacher sent you some other reference material, you can ping any of the mods or admins. NOTE: PLS FEEL FREE TO FUCK OFF IF YOU'RE NOT FROM PES UNIVERSITY"
    )

    channellogs2 = client.get_channel(#logs_channel_id)
    embed = discord.Embed(title="someone joined the server",
                          description=member,
                          color=discord.Color.gold())
    embed.add_field(name="Username: ", value=member.mention)
    await channellogs2.send(embed=embed)


######################################################################

@client.command()
async def assemble(ctx):
    if (ctx.author.id == #mod_1
            or ctx.author.id == #mod_2):
        await ctx.send("***Avengers, ASSEMBLE!***")
        await ctx.send(
            "#mod_id_to_ping"
        )


######################################################################


@client.command(aliases=['C', 'c'])
async def count(ctx, *, role: str = ""):
    if (role == ""):
        await ctx.channel.send(
            f"We have **{ctx.guild.member_count}** people in this server")
    else:
        try:
            ROLE = ctx.guild.get_role(int(role))
            await ctx.channel.send(
                f"**{len(ROLE.members)}** people have the role **{ROLE.name}**"
            )

        except:
            guild = ctx.guild
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
            await ctx.channel.send(
                f"**{count}** people have the role **{role}**")


##############################################################################

 
#change roles of all members with a role to another        
# @client.command(pass_context=True)
# @commands.has_any_role("Admin")
# async def addRemove(ctx,*,newRole:discord.Role):
#     x = ctx.guild.members
#     for member in x:
#         for role in member.roles:
#             if (role.name == "Sem-4 BT"):
#                 rmRole:discord.Role=role
#                 await member.add_roles(newRole)
#                 await member.remove_roles(rmRole)
#                 # await ctx.send(f"Done for **{member.name}**")
#     await ctx.channel.send("<@764118123330273330> done")

# @addRemove.error
# async def test_error(ctx, error):
#     if isinstance(error, commands.CheckFailure):
#         await ctx.send(error)


######################################################################
#useless fun commands

@client.command()
async def hello(ctx):
    await ctx.send(f'Hello {ctx.author.mention}')
    await ctx.author.send("hello,I hope you are doing good")

@client.command()
async def noob(ctx):
    await ctx.channel.send("no you")

@client.command()
async def god(ctx):
    await ctx.channel.send("I'm god, god is great <a:elmofire:869949972165050428>")

@client.command()
async def topper(ctx):
    await ctx.channel.send(f"{ctx.author.mention} that can be you too if you study, noob go study <:thu:878501339011874886> ")
    await ctx.channel.send("<:gostudy:972839521324523571>")

@client.command()
async def chad(ctx):
    await ctx.channel.send("Stop calling others chad for everything, go study <:tengue_fold:869949822709420054> , if I see chad word again,then I will kick you <:thu:878501339011874886>")

@client.command()
async def stripper(ctx):
    await ctx.channel.send("that is <@744592590749433926>")

######################################################################
            
@client.command()
async def spam(ctx, count, *user):
    if (ctx.message.author.id == #mod_1
            or ctx.message.author.id == #mod_2
            or ctx.message.author.id == #mod_3
            or ctx.message.author.id == #mod_4):
        for i in range(int(count)):

            await ctx.send(" ".join(list(user)))

    else:
        await ctx.send(ctx.author.mention, 'you cant, kekw')


######################################################################

keep_alive()

my_secret = os.environ['TOKEN']


client.run(my_secret)
