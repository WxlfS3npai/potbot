import discord
from discord.ext import commands
import asyncio
import os
client = commands.Bot(command_prefix= ',')

@client.event
async def on_ready():
    print(client.user.name)
    
@client.command(pass_context=True)
async def addrole(ctx, member: discord.Member, roles):
    """Adds a role to user"""
    if ctx.message.author.server_permissions.manage_roles:
        role = discord.utils.get(member.server.roles, name=roles)
        await client.add_roles(member, role)
        await client.say("User Has Been Assigned With Selected Role")
        await client.say(":white_check_mark: {} Now Has".format(member.mention) + " The Role: " + roles)
    else:
        await client.say(":octagonal_sign: Permisson Too Low.")

@client.command(pass_context=True)
async def removerole(ctx, member: discord.Member, roles):
    """Adds a role to user"""
    if ctx.message.author.server_permissions.manage_roles:
        role = discord.utils.get(member.server.roles, name=roles)
        await client.remove_roles(member, role)
        await client.say("User Has Been Assigned With Selected Role")
        await client.say(":octagonal_sign: {} Now doesnt has".format(member.mention) + " The Role: " + roles)
    else:
        await client.say(":octagonal_sign: Permisson Too Low.")
        
        
@client.command(pass_context=True)
async def report(ctx, user: discord.Member, reason, *msg):
    author = ctx.message.author
    if ctx.message.author.id == user.id:
        await client.send_message(user,"Don't try to report yourself! I see this as trolling and abuse or maybe you are just an idiot reporting yourself.")
    if ctx.message.author.id != user.id:
        embed = discord.Embed(title="you have been repoted by {} ID {} In {}".format(
            ctx.message.author.name, ctx.message.author.id, ctx.message.server.name))
        embed.add_field(name="reason", value="{}".format(reason), inline=False)
        embed.add_field(name="report", value="requested by {}".format(
            ctx.message.author.name), inline=False)
        await client.send_message(user, embed=embed)
        await client.say('report has been sent')
      

@client.command(pass_context=True)
async def help(ctx):
    print('test')

    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.blue()
    )

    embed.add_field(name="my mod commands", value="warn@someone <reason> - will warn user\naddrole@someone <rolename>\nmute@someone - mutes the user\nunmute - unmute the user\nkick@someone - kicks the user\nreport@someone <reason> - reports the user" , inline=False)
    await client.send_message(embed=embed)
    
@client.command(pass_context=True)
async def mute(ctx, member: discord.Member):
     if ctx.message.author.id == '380094320507748362':
        role = discord.utils.get(member.server.roles, name='Muted')
        await client.add_roles(member, role)
        embed=discord.Embed(title="User Muted!", description="**{0}** was muted by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
        await client.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff00f6)
        await client.say(embed=embed)

@client.command(pass_context=True)
async def unmute(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.manage_messages:
        role = discord.utils.get(member.server.roles, name='UnMuted')
        await client.remove_roles(member, role)
        embed=discord.Embed(title="User Unmuted!", description="{0} was unmuted by {1}!".format(member, ctx.message.author), color=0xff00f6)
        await client.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff00f6)
        await client.say(embed=embed)
        
client.run(os.environ['BOT_TOKEN'])
