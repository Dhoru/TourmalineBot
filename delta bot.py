import discord
from discord.ext import commands
import time
import random
bot = commands.Bot(command_prefix='!!')
@bot.remove_command('help')

@bot.command()
async def info(ctx):
  embed = discord.Embed(title='Delta - Info')
  embed.add_field(name="This bot was made using discord.py by dhoru#7700", value="Join the server at https://discord.gg/cthA5Pv !", inline=False)

  await ctx.send(embed=embed)

@bot.command()
async def help(ctx):
  embed = discord.Embed(title='Delta - Commands')
  embed.add_field(name="!!info", value="shows bot info.", inline=True)
  embed.add_field(name="!!info", value="shows bot info.", inline=True)
  embed.add_field(name="!!say <message>", value="bot repeats what you say.", inline=True)
  embed.add_field(name="!!react <emoji>", value="""reacts to your message
        with the specified emoji.""", inline=True)
  embed.add_field(name="!!ping", value="shows bot latency.", inline=True)
  embed.add_field(name="__ASCII Art Commands:__", value="Commands which show ascii art", inline=False)
  embed.add_field(name="!!point", value="ascii finger point", inline=True)
  embed.add_field(name="!!clouds", value="ascii clouds", inline=True)
  embed.add_field(name="!!communism", value="ascii communist sign", inline=True)
  embed.set_footer(text="Delta")
  embed.colour = 0xFFFFFF  # can be set in 'discord.Embed()' too

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
async def communism(ctx):
    await ctx.send('''
```fix
        ._
         `d,
           Qb
       _   jQ
     .gP`  JP
._   ' ~&.~P
 ~JJjpjJ ~&.
 jJ        ~&.
jJ           ~'
~       MC
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

@bot.command()
async def ping(ctx):
    await ctx.send('Pong! `{0} ms`'.format(round(bot.latency, 1)))

@bot.event
async def on_ready():
    activity = discord.Game(name="Dhoru is epic | !!help", type=3)
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print("Bot is ready!")


bot.run('NzQ5OTEwOTQ0OTUxNDM1MjY0.X0y2_Q.dWq7mJQyHEpiPD5kxFchIJxQ_PM')
