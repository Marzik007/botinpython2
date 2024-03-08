"""
import discord
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send('Hello!')

bot.run('MTIwMjYwMDgxMDM0MTcyODMxNg.GIe8od.unQqReXpLoLIDjmGIJsJkRV-uwKv0ihb70BOn4')

"""

import discord
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send('Hello!')

@bot.command()
async def version(ctx):
    await ctx.send('version 0.1.3')

bot.run('MTIwMjYwMDgxMDM0MTcyODMxNg.GIe8od.unQqReXpLoLIDjmGIJsJkRV-uwKv0ihb70BOn4')
