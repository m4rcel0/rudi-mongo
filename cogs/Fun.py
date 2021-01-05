import discord
from discord.ext import commands
import requests
import random
from TextToOwO import owo
import re

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["echo"])
    @commands.is_owner()
    async def say(self, ctx, *, words: commands.clean_content):
        """Makes the bot say something"""
        try:
            await ctx.message.delete()
        except:
            pass
        await ctx.send(words)

    @commands.command()
    async def owo(self, ctx, *, msg: commands.clean_content = None):
        """Converts normal text to OwO
        
        Usage: !owo 'text'
        If no text is provided, it uses the previous message's contents"""
        if not msg:
            msg = ctx.bot._connection._messages[len(ctx.bot._connection._messages)-2].content
        owo_msg = owo.text_to_owo(msg)
        await ctx.send(owo_msg)

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
            "sapa",
            "kurbağa"
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

def doesnt_know(message):

    idk = re.search(r'\b(idk|dunno)|(i\s(dont|do\snot|don\'t)\s((even|really)\s)?(know|understand|get))|(i\slack\s(critical|important)\sinformation)|(i((\'m)|(\sam))\snot\sof\sunderstandment)\b', message)
    if idk: return True
    
    return False

def react_dogehouse(message):

    if message.guild.id == 575312937611427860 and message.author.id == 313290158969454593:
        return True

    return False

def setup(bot):
    bot.add_cog(Fun(bot))