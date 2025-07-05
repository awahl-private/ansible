import discord
from discord.ext import commands

# Create a bot instance with a command prefix
bot = commands.Bot(command_prefix='!')

# Dictionary to store user floats
user_floats = {}

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def store(ctx, value: float):
    user_floats[ctx.author.id] = value
    await ctx.send(f"Stored {value} for {ctx.author.name}.")

@bot.command()
async def get(ctx):
    value = user_floats.get(ctx.author.id, None)
    if value is not None:
        await ctx.send(f"{ctx.author.name}, your stored value is {value}.")
    else:
        await ctx.send("You haven't stored a value yet.")

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot.run('YOUR_BOT_TOKEN')
