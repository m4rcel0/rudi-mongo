import discord
from discord.ext import commands
import requests
import random

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["echo"])
    async def say(self, ctx, *, words: commands.clean_content):
        """Makes the bot say something"""
        #await ctx.message.delete()
        await ctx.send(words)

    @commands.command(aliases=["kot"])
    async def cat(self, ctx):
        """A random cat pic"""
        cat = requests.get("http://aws.random.cat/meow").json()
        embed = discord.Embed(colour=ctx.author.color)

        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.set_footer(text="A random cat!  •  Powered by random.cat")
        
        embed.set_image(url=cat['file'])

        await ctx.send(embed=embed)

    @commands.command(aliases=["doggo"])
    async def dog(self, ctx):
        """A random dog pic"""
        dog = requests.get("https://dog.ceo/api/breeds/image/random").json()
        embed = discord.Embed(colour=ctx.author.color)
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.set_footer(text="A random dog!  •  Powered by dog.ceo")
        
        embed.set_image(url=dog['message'])

        await ctx.send(embed=embed)

    @commands.command(
        aliases=[
            "frog",
            "pepo",
            "kikker",
            "frosch",
            "zaba",
            "sapo",
            "лягушка",
            "grenouille",
            "béka",
            "Žába",
            "កង្កែប",
            "perereca",
            "rã",
            "forg",
            "frogge",
            "sapa"
        ]
    )
    async def pepe(self, ctx):
        """A random pepe"""
        await ctx.send(embed=get_pepe(ctx))

    
def get_pepe(ctx):
    pepes = [pepe.rstrip('\n') for pepe in open("assets/pepes.txt")]
    chosen_pepe = random.choice(pepes)
    embed = discord.Embed(colour=ctx.author.color)
    embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    embed.set_footer(text="A random pepe!  •  Maybe it's rare, idk")
    embed.set_image(url=chosen_pepe)
    return embed

def setup(bot):
    bot.add_cog(Fun(bot))