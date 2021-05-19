'''
                 ========
                 imports:
                 ========
'''
asyncpraw                       # reddit api
import discord                         # discord
from discord.ext import commands       # commands
import time                            # time
import random                          # random
import os                              # idk why this is even here lol
from catfacts import catfacts          # catfacts.py list
import platform                        # w h a t i forgot
import datetime                        # same for this
import json                            # json stuff coming soon
import pyquran as q                    # pyquran
bot = commands.Bot(command_prefix='t.', intents=discord.Intents.all())
bot.remove_command('help')

#        '''
#reddit = asyncpraw.Reddit(client_id='MRtY6ttHixEa0A',
#                     client_secret='D6sKN7YJ84ZcBRBFjM1Up-dQLlk',
#                     user_agent='tourmalinebot by u/Dhoru_',
#                     password='A_legend#7700',
#                     username='Dhoru_')  
#        '''

#        '''
#with open("C:/Users/Admin/Desktop/Random Stuff/thing stuf/TourmalineBot/datas.json", "w") as file:
#    data = json.load(file)
#        '''
@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Tourmaline - Commands", description="""
    **Main commands:**
    `t.info` - Shows bot info (under development)
    `t.say <message>` - Bot repeats what you say.
    `t.react <emoji>` - Reacts to your message with the specified emoji.
    `t.ping` - Shows bot latency.
    `t.invite` - Link to invite the bot.

    **Fun commands:**
    `t.coinflip` - Flips a coin.
    `t.meme` - Memes fresh from r/dankmemes. (removed for a while because of problems)
    `t.catfact` Random cat fact.

    **Utility/Moderation commands:**
    `t.setnick <@user>` - Changes the specified user's nickname.
    `t.roll <number of dice> <number of sides in each dice>` - Simulates rolling dice.
    """)
    embed.set_footer(text="TourmalineBot - Made by dhoru#7700")
    embed.colour = 0xFFFFFF  # can be set in 'discord.Embed()' too

    await ctx.send(embed=embed)
  # or: await destination.send(embed=embed)

@bot.command()
async def info(ctx):
    embed=discord.Embed(title="Info")
    embed.add_field(name="Version:", value=discord.version_info, inline=False)
    embed.set_footer(text="TourmalineBot - Made by dhoru#7700")
    await ctx.send(embed=embed)

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
	embed=discord.Embed(title="Invite Link", url="https://discord.com/oauth2/authorize?client_id=749910944951435264&permissions=4294967295&scope=bot")
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

@bot.command()
async def setnick(ctx, member: discord.Member, nick):
    await member.edit(nick=nick)
    await ctx.send(f'Nickname was changed for {member.mention} ')

@bot.command()
async def test(ctx):
    embed=discord.Embed(title="Rules:", description="<a:ruby:763440863027396628> Use common sense pls \n \n<a:ruby:763440863027396628> No mass mentioning of any form or spamming of any sort\n\n<a:ruby:763440863027396628> Do not annoy, dissolve, digest, or threaten anyone.\n \n <a:ruby:763440863027396628> No NSFW content.\n \n <a:ruby:763440863027396628> Don't abuse loopholes. \n \n<a:ruby:763440863027396628> ***Either*** your username *or* nickname should be pingable.\n \n <a:ruby:763440863027396628> No advertising servers (includes DM advertising). In case it does happen anyway, Report it to a staff member. (apply for partnership #┃partners)\n\n<a:ruby:763440863027396628> Do not DM staff about mutes/ warns.\n\n<a:ruby:763440863027396628> Alt accounts are **NOT** allowed.\n\n<a:ruby:763440863027396628> No begging for roles.\n\n<a:ruby:763440863027396628> No being an imbecile.")
    embed.colour = 0x00FF00
    await ctx.send(embed=embed)
    await ctx.message.delete()

        '''
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
async def subreddit(ctx, arg):
    postthings = await reddit.subreddit(arg).hot()
    post_to_pick = random.randint(1, 50)
    for i in range(0, post_to_pick):
        submission = next(x for x in postthings if not x.stickied)

    embed=discord.Embed(title=submission.title, url=submission.url, color=0x0af0d5)
    embed.set_image(url=submission.url)
    await ctx.send(embed=embed)
        '''

@bot.command()
async def ayat(ctx, sn: int, an: int):
    embed=discord.Embed(title=q.quran.get_sura_name(sn), description=q.quran.get_verse(sura_number=sn, verse_number=an))
    embed.color = 0xFFFFFF
    await ctx.send(embed=embed)

@bot.command
@commands.is_owner()                     
async def status(ctx, *, text: str):
    await bot.change_presence(activity=discord.Game(name=text))

@bot.command()
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))
        
@bot.event
async def on_ready():
    activity = discord.Game(name="Dhoru is Epic | t.help", type=3)
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print("------")
    print("Bot is ready!")
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.run('TOKEN')
