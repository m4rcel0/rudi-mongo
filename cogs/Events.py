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
            guild_members = message.guild.members
            while True:
                someone = random.choice(guild_members)
                if not someone.bot:
                    await message.channel.send(f"{someone.mention}")
                    break

        if Fun.doesnt_know(message.content.lower()):
           await message.add_reaction(":HeDoesntKnow:578466405649874944")

        if Fun.react_dogehouse(message):
            await message.add_reaction(":pempocute:682304790948085887")

        # print(f"@{message.author} in {message.guild} #{message.channel} said:\n\t{message.content}")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("You can't do that!")
        if isinstance(error, commands.CommandNotFound):
            pass
            #await ctx.send("This is not a command...")
            #await ctx.send("This is not a command...\nHere, have a pepe instead:", embed=Fun.get_pepe(ctx))

        raise error



def setup(bot):
    bot.add_cog(Events(bot))
