import discord
from discord.ext import commands
import random
import asyncio
import os

bot = commands.Bot(command_prefix="!")
TOKEN = open("token.txt", "r").read()

async def chng_pr():
    await bot.wait_until_ready()
    statuses = [
        "!help",
        "with mongs",
        "!pepe",
        "with nsfw api's",
        "with my pp",
        "mong playlist @spotify",
        "REEEEEEEEEEEEEEEEEEEEEE",
        "innocent",
        "with your feelings",
        "Grand Dead Game V",
        "Forza can't connect 4",
        "@someone",
        "the waiting game while you don't give Cow more ideas for commands :pepega:"
    ]

    while not bot.is_closed():
        status = random.choice(statuses)
        await bot.change_presence(activity=discord.Game(status))
        await asyncio.sleep(60)

for cog in os.listdir("./cogs"):
    if cog.endswith(".py") and not cog.startswith("_"):
        try:
            cog = f"cogs.{cog.replace('.py', '')}"
            bot.load_extension(cog)
            print(f"{cog[5:]} loaded successfully!")
        except Exception as e:
            print(f"{cog} cannot be loaded:")
            raise e

bot.loop.create_task(chng_pr())

bot.run(TOKEN)
