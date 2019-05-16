import discord
from discord.ext import commands
from mcstatus import MinecraftServer

class Minecraft(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["mcstatus", "server", "serverstatus"])
    async def status(self, ctx):
        """Checks minecraft server status"""

        server = MinecraftServer("152.89.245.40", 40247)
        status = server.status()
        title = status.raw["description"]["text"]
        players = status.raw["players"]["sample"]
        names = [player["name"] for player in players]
        name_list = "\n".join(names)
        players_online = str(status.players.online) + " players online:"
        version = "Server Version: " + status.raw["version"]["name"]
        
        embed = discord.Embed(colour=ctx.author.color, title=title)
        embed.set_thumbnail(url="https://i.imgur.com/aYOBOrS.png")
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.add_field(name=players_online, value=name_list)
        embed.set_footer(text=version)

        await ctx.send(embed=embed)
    

def setup(bot):
    bot.add_cog(Minecraft(bot))