import os
import discord
from discord.ext import commands

token = ""

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


# coroutine to load all cogs
async def load_cogs():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py") and filename != "__init__.py":
            await bot.load_extension(f"cogs.{filename[:-3]}")
            print(f"Loaded {filename[:-3]}")


@bot.event
async def on_ready():
    print("Bot is ready!")
    await load_cogs()


bot.run(token)
