import discord
from discord.ext import commands
import time
import random
import os
bot = commands.Bot(command_prefix='!!')
@bot.remove_command('help')

@bot.command()
async def info(ctx):
  embed = discord.Embed(title='TourmalineBot - Info')
  embed.add_field(name="This bot was made using discord.py by dhoru#7700", value="Join the server at https://discord.gg/cthA5Pv !", inline=False)

  await ctx.send(embed=embed)

@bot.command()
async def help(ctx):
    embed = discord.Embed(title='TourmalineBot - Main Commands')
    embed.add_field(name="!!info", value="shows bot info.", inline=True)
    embed.add_field(name="!!info", value="shows bot info.", inline=True)
    embed.add_field(name="!!say <message>", value="bot repeats what you say.", inline=True)
    embed.add_field(name="!!react <emoji>", value="""reacts to your message
          with the specified emoji.""", inline=True)
    embed.add_field(name="!!ping", value="shows bot latency.", inline=True)
    embed.set_footer(text="Hello World")
    embed.colour = 0xFFFFFF  # can be set in 'discord.Embed()' too

    await ctx.send(embed=embed)

    embed = discord.Embed(title='TourmalineBot - Fun commands:')
    embed.add_field(name="!!coinflip", value="flips a coin.", inline=True)
    embed.add_field(name="!!point", value="ascii finger point", inline=True)
    embed.add_field(name="!!clouds", value="ascii clouds", inline=True)
    embed.colour = 0xFFFFFF 

    await ctx.send(embed=embed)

  # or: await destination.send(embed=embed)

#឵឵឵឵឵឵
@bot.command()
async def point(ctx):
  embed = discord.Embed(title='឵឵')
  embed.add_field(name="ASCII hand sign", value="""
  ```fix
      mmm_
       YMMmm._
         "MMMMMm.
           '"YMMMbm.
       _,mmmm._mMMMMMm.
    ,mMMMMYMMMMMMMMMPMMMm.
   dMMMMP   '"YMMMMMUMMMLM.
  dMMMP'        `YMMPYMPM8Mb_
mdMMM_             MM8mMMmM_Yb.
YMMMMMMm___     ,mMPdMMMMMMMMmYM.
   YPM8MMMM8mmmmmmmMMMMMMMMMMMMbM.
      '`Y8MMMMMMMMMMMMMMMMMMMMMMMM._
           `YM8PMMMMMMMMMMMMMMMMMMMMm__
              `"MbYMMMMMMMMMMMMMMMMMMMMbL_
                 'YYMPPMMMMMMMMMMMMMMMMMMMMm_
                     `"PM"YMMMMMMMMMMMMMMmMMb.
                         `"YMMMMMMMMMMMMMMMbMMM_
                             YMMMMMMMMMMMMMMMMMM
                               YMMMMMMMMMMMMMMMM
  -Dhoru#7700-                  YMMMMMMMMMMMMMMM
                                  `YMMMMMMMMMMMP
                                    `YMMMMMMMMMM
                                      `MMMMMMMMM
                                       `MMMMMdMM
```""", inline=False)
  await ctx.send(embed=embed)


@bot.command()
async def clouds(ctx):
    await ctx.send('''
```fix
                     _________
     ___            (         )
    (   )__       _(           )___
   (_______)...  (_________________)

```
     ''')

@bot.command()
async def react(ctx, arg):
    await ctx.message.add_reaction(arg)

@bot.command()
async def say(ctx, *, arg):
    if arg == "@everyone":
        await ctx.send("no mass mentioning.")
    elif arg == "@here":
        await ctx.send("no mass mentioning.")
    else:
        await ctx.send(arg)
        await ctx.message.delete()

@bot.command(pass_context=True)
async def coinflip(ctx):
    coin = [
        "heads",
        "tails",]
    await ctx.send(random.choice(coin))

@bot.command(pass_context=True)
async def kill(ctx, arg):
    murder_message = [
    "dies of covid-19"
    ]
    await ctx.send("{}".format(arg, random.choice(murder_message)))

@bot.command()
async def ping(ctx):
    await ctx.send('Pong! `{0} ms`'.format(round(bot.latency, 1)))

@commands.is_owner()
@bot.command()
async def tr(ctx):
  await ctx.send("https://discord.com/developers/applications/749910944951435264/bot")

@bot.event
async def on_ready():
    activity = discord.Game(name="add status here", type=3)
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print("Bot is ready!")
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command(name='roll_dice', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))



bot.run('insert your token here')
