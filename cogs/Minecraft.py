import discord
from discord.ext import commands
from mcstatus import MinecraftServer
import asyncio

class Minecraft(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=[
        "players",
        "playerlist",
        "pl",
        "server"
    ])
    async def status(self, ctx):
        """Checks minecraft server status"""

        server = MinecraftServer("152.89.245.40", 40247)

        response = await ctx.send("Fetching server information...")

        for i in range(5):
            try:
                status = server.status()
                break
            except:
                if i == 4:
                    await response.edit(content="Could not reach the server.")
                    return
                await response.edit(content="Failed to get info, trying again, attempt {}/5".format(i+2))
            await asyncio.sleep(1)
            
        
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

        await response.delete()
        await ctx.send(embed=embed)
    

def setup(bot):
    bot.add_cog(Minecraft(bot))