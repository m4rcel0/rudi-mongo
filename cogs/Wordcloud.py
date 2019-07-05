import discord
from discord.ext import commands
from wordcloud import WordCloud
import random
import os
import asyncio
from concurrent.futures import ThreadPoolExecutor
import re

async def cloud_making(func, text, font, hues, res):
    executor = ThreadPoolExecutor(10)
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(executor, func, text, font, hues, res)

def make_cloud(text, font, hues, res):
    global currenthues
    currenthues = hues
    words = clean_words(text)
    wordcloud = WordCloud(font_path=get_random_font(font), background_color=bgc, mode='RGBA', width=res[0], height=res[1], scale=1, color_func=generate_color)
    wordcloud.generate(' '.join(words))
    wordcloud.to_file('wordcloud.png')


def generate_color(word=None, font_size=None, position=None, orientation=None, font_path=None, random_state=None):
    return 'hsl(%s, %s%%, %s%%)' % (random.choice(currenthues), 100, random.randint(20, 80))


def get_random_font(category):
    return 'assets/fonts/' + category + '/' + random.choice(os.listdir('assets/fonts/' + category))


def clean_words(text):
    text = text.lower()
    #clean = re.sub(r'[!*&|]\w*', '', clean)
    clean = re.findall(r'\w+', re.sub(r'[.!@#$%¨&*-=+;:/|\\]\w*', '', text))
    return clean


resolutions = {
    'default' : [640, 360],
    '720p' : [1280, 720],
    '1080p' : [1920, 1080],
    '4k' : [4096, 2160]
}


class Wordcloud(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['wc', 'cloud'])
    async def wordcloud(self, ctx, *args):
        """Creates a wordcloud from 1000 previous messages in the channel

        Usage: !wordcloud [color] [font] [resolution] [transparent] [amount_of_messages]
        
        Arguments are optional, and the order does not matter

        Colors: red, orange, yellow, green, blue, purple (can use more than one)
        Fonts: clean, fancy, handwriting
        Resolution: 720p, 1080p, 4k
        Transparent background: transparent
        Amount of messages: amount='number'

        Example: !wordcloud yellow blue clean 1080p messages=100
        """
        font = ''
        hues = []
        global bgc
        bgc = 'black'
        res = resolutions['720p']

        amount = 1000

        
        for arg in args:
            if arg.startswith('messages='):
                amount = int(arg.lstrip('messages='))
            elif is_color(arg):
                hues.append(from_name(arg).hue)
            elif arg in os.listdir('assets/fonts/'):
                font = arg
            elif arg in resolutions:
                res = resolutions[arg]
            elif arg == 'transparent':
                bgc=None        


        if not font:
            font = random.choice(os.listdir('assets/fonts/'))

        if len(hues) < 1:
            hues.append(random.choice(allColors).hue)

        status = await ctx.send(f"Reading {amount} messages...")

        generatefrom = ''
        
        try:
            async for message in ctx.channel.history(limit=amount):
                if not message.author.bot:
                    generatefrom = (generatefrom + ' ' + message.content)
            
            await status.edit(content=f"Creating cloud in {res[0]}x{res[1]}... (may take a while)")

            await cloud_making(make_cloud, generatefrom, font, hues, res)
            await ctx.send(file=discord.File('wordcloud.png'))
        except: 
            await ctx.send("❌ Could not create wordcloud ❌\nContact the owner maybe, idk <:peeposhrug:596749393575804937>")
        
        
        await status.delete()

        os.remove('wordcloud.png')


class Color:
    name = ''
    hue = -1

    def __init__(self, name, hue):
        self.name = name
        self.hue = hue
        allColors.append(self)


allColors = []

red = Color('red', 0)
orange = Color('orange', 30)
yellow = Color('yellow', 60)
green = Color('green', 120)
blue = Color('blue', 210)
purple = Color('purple', 270)


def from_name(name):
    for color in allColors:
        if color.name == name:
            return color
    return None

def is_color(name):
    for color in allColors:
        if color.name == name:
            return True
    return False

def setup(bot):
    bot.add_cog(Wordcloud(bot))