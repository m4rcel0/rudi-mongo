import discord
from discord.ext import commands

class Mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx, cog):
        try:
            self.bot.unload_extension(f"cogs.{cog}")
            self.bot.load_extension(f"cogs.{cog}")
            await ctx.send(f"{cog} module was reloaded successfully!")
        except Exception as e:
            await ctx.send(f"The {cog} module could not be loaded, I'm now broken.")
            print(f"{cog} cannot be loaded:")
            raise e

    @commands.command(aliases=[
        "die",
        "begone",
        "fuckoff"
    ])
    @commands.is_owner()
    async def logout(self, ctx):
        await ctx.send("<:really:697676884510507018>")
        await ctx.send("ok bi")
        await self.bot.logout()

    # @commands.command()
    # @commands.has_permissions(kick_members=True)
    # async def kick(self, ctx, member: discord.Member, *, reason=""):
    #     await member.kick(reason=reason)
    #     await ctx.send(f"{member.mention} was kicked by {ctx.author.mention}, {reason}")

    # @commands.command()
    # @commands.has_permissions(ban_members=True)
    # async def ban(self, ctx, member: discord.Member, *, reason="No reason"):
    #     await member.ban(reason=reason)
    #     await ctx.send(f"{member.mention} was banned by {ctx.author.mention}, {reason}")

    # @commands.command()
    # @commands.has_permissions(manage_messages=True)
    # async def purge(self, ctx, amount: int):
    #     """Deletes a number of messages"""
    #     await ctx.channel.purge(limit=amount+1)
    #     await ctx.send(f"{amount} messages  got deleted")

    # @purge.error
    # async def purge_error(self, ctx, error):
    #     if isinstance(error, commands.CheckFailure):
    #         await ctx.send("You can't do that!")
    #     if isinstance(error, commands.MissingRequiredArgument):
    #         await ctx.send("You need to specify an amount")
    #     if isinstance(error, commands.BadArgument):
    #         await ctx.send("Argument needs to be an integer")
    #     raise error
    

def setup(bot):
    bot.add_cog(Mod(bot))