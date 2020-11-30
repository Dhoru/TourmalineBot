import praw
import discord
from discord.ext import commands
import time
import random
import os
from catfacts import catfacts
import platform
import datetime
import json
bot = commands.Bot(command_prefix='!!')
bot.remove_command('help')

reddit = praw.Reddit(client_id='Client id',
                     client_secret='Client Secret',
                     user_agent='user agent')  

@bot.command()
async def info(ctx):
    serverCount = len(bot.guilds)
    memberCount = len(set(bot.get_all_members()))

    embed = discord.Embed(title=f'{self.bot.user.name} Stats', description='\uFEFF', colour=ctx.author.colour, timestamp=ctx.message.created_at)

    embed.add_field(name='Bot Version:', value=self.bot.version)
    embed.add_field(name='Python Version:', value=pythonVersion)
    embed.add_field(name='Discord.Py Version', value=dpyVersion)
    embed.add_field(name='Total Guilds:', value=serverCount)
    embed.add_field(name='Total Users:', value=memberCount)
    embed.add_field(name='Made By:', value="dhoru#7700")

    embed.set_footer(text=f"Carpe Noctem | {self.bot.user.name}")
    embed.set_author(name=bot.user.name, icon_url=self.bot.user.avatar_url)

    await ctx.send(embed=embed) 
  
@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Tourmaline - Commands", description="""
    **Main commands:**
    `!!info` - Shows bot info (under development)
    `!!say <message>` - Bot repeats what you say.
    `!!react <emoji>` - Reacts to your message with the specified emoji.
    `!!ping` - Shows bot latency.
    `!!invite` - Link to invite the bot.

    **Fun commands:**
    `!!coinflip` - Flips a coin.
    `!!meme` - Memes fresh from r/dankmemes.
    `!!catfact` Random cat fact.

    **Utility/Moderation commands:**
    `!!setnick <@user>` - Changes the specified user's nickname.
    `!!roll <number of dice> <number of sides in each dice>` - Simulates rolling dice.
    """)
    embed.set_footer(text="TourmalineBot - Made by dhoru#7700")
    embed.colour = 0xFFFFFF  # can be set in 'discord.Embed()' too

    await ctx.send(embed=embed)
  # or: await destination.send(embed=embed)

#឵឵឵឵឵឵
@bot.command()
async def react(ctx, arg):
    await ctx.message.add_reaction(arg)

@bot.command()
async def say(ctx, *, arg):
    message_components = arg.split()
    if "@everyone" in message_components or "@here" in message_components:
        await ctx.send("You cannot have ``@everyone`` or ``@here`` in your message!")
        await ctx.message.delete()
    else:
        await ctx.send(arg)
        await ctx.message.delete()

@bot.command(pass_context=True)
async def coinflip(ctx):
    coin = [
        "heads",
        "tails",]
    await ctx.send(random.choice(coin))

@bot.command()
async def ping(ctx):
    await ctx.send('Pong! `{0} ms`'.format(round(bot.latency, 1)))

@bot.command()
async def invite(ctx):
	embed=discord.Embed(title="Invite Link", url="https://discord.com/api/oauth2/authorize?client_id=749910944951435264&permissions=8&scope=bot")
	embed.colour = 0xFFFFFF 
	
	await ctx.send(embed=embed)


@bot.command()
async def ohnoanyway(ctx):
  await ctx.send("https://i.kym-cdn.com/photos/images/original/001/883/586/63f.jpg")

@bot.command()
async def catfact(ctx):
    await ctx.send(random.choice(catfacts))

@commands.is_owner()
@bot.command()
async def tr(ctx):
  await ctx.send("https://discord.com/developers/applications/749910944951435264/bot")

@bot.command(pass_context=True)
async def setnick(ctx, member: discord.Member, nick):
    await member.edit(nick=nick)
    await ctx.send(f'Nickname was changed for {member.mention} ')

@bot.command()
async def tourmaline_rules(ctx):
    embed=discord.Embed(title="Rules:", description="<a:ruby:763440863027396628> Use common sense pls \n \n<a:ruby:763440863027396628> No mass mentioning of any form or spamming of any sort\n\n<a:ruby:763440863027396628> Do not annoy, dissolve, digest, or threaten anyone.\n \n <a:ruby:763440863027396628> No NSFW content.\n \n <a:ruby:763440863027396628> Don't abuse loopholes. \n \n<a:ruby:763440863027396628> ***Either*** your username *or* nickname should be pingable.\n \n <a:ruby:763440863027396628> No advertising servers (includes DM advertising). In case it does happen anyway, Report it to a staff member. (apply for partnership #┃partners)\n\n<a:ruby:763440863027396628> Do not DM staff about mutes/ warns.\n\n<a:ruby:763440863027396628> Alt accounts are **NOT** allowed.\n\n<a:ruby:763440863027396628> No begging for roles.\n\n<a:ruby:763440863027396628> No being an imbecile.")
    embed.colour = 0x00FF00
    await ctx.send(embed=embed)
    await ctx.message.delete()

@bot.command()
async def meme(ctx):
    memes_submissions = reddit.subreddit('dankmemes').hot()
    post_to_pick = random.randint(1, 50)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)

    embed=discord.Embed(title=submission.title, url=submission.url, color=0x0af0d5)
    embed.set_image(url=submission.url)
    await ctx.send(embed=embed)

@bot.command()
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))
    
@bot.event
async def on_ready():
    activity = discord.Game(name="Dhoru is Epic | !!help", type=3)
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print("------")
    print("Bot is ready!")
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.run(token)
