import discord
from discord.ext import commands
import random

from cogs import Fun

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Logged in as " + self.bot.user.name)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        
        if message.content == "@someone":
           await message.channel.send(f"{random.choice(message.guild.members).mention}")

        if Fun.doesnt_know(message.content):
            await message.add_reaction(":HeDoesntKnow:578466405649874944")

        # print(f"@{message.author} in {message.guild} #{message.channel} said:\n\t{message.content}")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("You can't do that!")
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("This is not a command...")
            #await ctx.send("This is not a command...\nHere, have a pepe instead:", embed=Fun.get_pepe(ctx))

        raise error



def setup(bot):
    bot.add_cog(Events(bot))