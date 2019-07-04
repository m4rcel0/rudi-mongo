import discord
from discord.ext import commands
from wordcloud import WordCloud
import random
import os

def make_cloud(text, font, hues):
    global currenthues
    currenthues = hues
    words = clean_words(text)
    wordcloud = WordCloud(font_path=get_random_font(font), background_color=bgc, mode='RGBA', width=640, height=360, scale=1, color_func=generate_color)
    wordcloud.generate(' '.join(words))
    wordcloud.to_file('wordcloud.png')


def generate_color(word=None, font_size=None, position=None, orientation=None, font_path=None, random_state=None):
    return 'hsl(%s, %s%%, %s%%)' % (random.choice(currenthues), 100, random.randint(20, 80))


def get_random_font(category):
    return 'assets/fonts/' + category + '/' + random.choice(os.listdir('assets/fonts/' + category))

boringwords = ['the', 'a', 'an', 'of']

def clean_words(text):
    clean = to_words(text)
    for boring in boringwords:
        clean[:] = [word for word in clean if word != boring]
        clean = [x for x in clean if ':' not in x]
        clean = [x for x in clean if '@' not in x]
    return clean


def to_words(text):
    return text.lower().split()


class Wordcloud(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['wc', 'cloud'])
    async def wordcloud(self, ctx, *args):
        font = ''
        hues = []
        global bgc
        bgc = 'black'
        # global mode = 'RGB'
        for arg in args:
            if is_color(arg):
                hues.append(from_name(arg).hue)
            elif arg in os.listdir('assets/fonts/'):
                font = arg
            elif arg == 'transparent':
                bgc=None
                # mode='RGBA'


        if not font:
            font = random.choice(os.listdir('assets/fonts/'))

        if len(hues) < 1:
            hues.append(random.choice(allColors).hue)

        status = await ctx.send("Reading messages...")

        generatefrom = ''
        async for message in ctx.channel.history(limit=1000):
            if not message.author.bot:
                generatefrom = (generatefrom + ' ' + message.content)
        
        await status.edit(content="Creating cloud...")
        
        make_cloud(generatefrom, font, hues)

        await message.channel.send(file=discord.File('wordcloud.png'))
        
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