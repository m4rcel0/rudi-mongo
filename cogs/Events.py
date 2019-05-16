import discord
from discord.ext import commands
import random

from cogs import Fun

unaware = [
    "idk",
    "dunno",
    "i don't know",
    "i dont know"
]

questions = [
    "what",
    "why",
    "where"
]

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
        
        if message.content.endswith("?"):
            await message.add_reaction(":FeelsFunnyMan:578366776681955348")

        for question in questions:
            if message.content.startswith(question):
                await message.add_reaction(":FeelsFunnyMan:578366776681955348")
                break
        
        for idk in unaware:
            if idk in message.content:
                await message.add_reaction(":FeelsFunnyMan:578366776681955348")
                break
        #if "idk" in message.content:
            #await message.channel.send(f"{message.author.mention} doesn't know <:FeelsFunnyMan:578366776681955348>")


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