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

        server = MinecraftServer("51.89.244.124", 25609)

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
        try:
            players = status.raw["players"]["sample"]
            names = "\n".join([player["name"] for player in players])
            #name_list = "\n".join(names)
        except:
            names = "Nobody is playing"
        if status.players.online == 1:
            players_online = "1 player online:"
        else:
            players_online = str(status.players.online) + " players online:"
        version = "Version: " + status.raw["version"]["name"]
        
        embed = discord.Embed(colour=discord.Colour.green(), title=title)
        embed.set_thumbnail(url="https://i.imgur.com/aYOBOrS.png")
        embed.add_field(name=players_online, value=names)
        embed.add_field(name="Latency:", value=str(status.latency) + "ms", inline=False)
        embed.set_footer(text=version)

        await ctx.send(embed=embed)
        await response.delete()
    

def setup(bot):
    bot.add_cog(Minecraft(bot))