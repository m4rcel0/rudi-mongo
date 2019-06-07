import discord
from discord.ext import commands
import random
import asyncio
import os
import json

CONFIG = json.load(open("config.json", "r"))
TOKEN = CONFIG["token"]
bot = commands.Bot(command_prefix=CONFIG["prefix"])

async def chng_pr():
    await bot.wait_until_ready()
    game_status = [
        "!pepe",
        "with my pp",
        "innocent",
        "with your feelings",
        "Grand Dead Game V",
        "Forza can't connect 4",
        "IRON MINING SIMULATOR"
    ]

    listen_status = [
        "mong playlist @spotify",
        "10 Hours of Soft Loli Breathing"
    ]

    watch_status = [
        "ayymd memes",
        "dead chat",
        "you do @someone in chat",
        "your lack of critical information",
        "the great mongolian empire rise again"
    ]

    statuses = {
        0 : game_status,
        2 : listen_status,
        3 : watch_status
    }


    while not bot.is_closed():
        status_type = random.choice([0,2,3])
        status = random.choice(statuses[status_type])
        await bot.change_presence(activity=discord.Activity(name=status, type=status_type))
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
