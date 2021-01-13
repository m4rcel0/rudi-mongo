import requests
import json

import discord
from discord.ext import commands

from datetime import datetime

class Corona(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
   

    @commands.command(aliases=[
        "c",
        "covid",
        "coronavirus",
        "covid19"
    ])
    async def corona(self, ctx, *, target_country = None):
        """Display COVID-19 data from countries or the world
            Usage:
            !c
            !c br
            !c brazil
        """

        if not target_country:
            url_td = "https://disease.sh/v3/covid-19/all"
            url_yt = "https://disease.sh/v3/covid-19/all?yesterday=true"
            url_2d = "https://disease.sh/v3/covid-19/all?twoDaysAgo=true"
            country_flag = "https://cdn.discordapp.com/attachments/587051836050112512/696495396628988014/W31X.gif"
        else:
            url_td = "https://disease.sh/v3/covid-19/countries/" + target_country.lower()
            url_yt = "https://disease.sh/v3/covid-19/countries/" + target_country.lower() + "?yesterday=true"
            url_2d = "https://disease.sh/v3/covid-19/countries/" + target_country.lower() + "?twoDaysAgo=true"
            country_flag = None
            
        try:
            data_today = requests.get(url_td).json()
            data_yesterday = requests.get(url_yt).json()
            data_twoDaysAgo = requests.get(url_2d).json()
            country_flag = country_flag if country_flag else data_today['countryInfo']['flag']
        except:
            ctx.send("Unable to get information right now. Try again later or contact Cow... idk")
            return
        
        try:
            title = data_today['country']
        except:
            title = "World"
            
        time = int((datetime.utcnow() - datetime.utcfromtimestamp(data_today['updated']/1000)).total_seconds()/60)

        def create_embed(data, flag, title, day, time):
            embed = discord.Embed(
                colour=discord.Colour.purple(),
                title=title + " Covid-19 " + day,
                url="https://www.worldometers.info/coronavirus/")
            embed.set_thumbnail(url=flag)
            if time < 1:
                embed.set_footer(text="Updated less than a min. ago")
            else:
                embed.set_footer(text="Updated " + str(time) + "min ago")
            
            embed.add_field(name="<:totalcases:696506315131846717> Total", value="{:,}".format(data['cases']))
            embed.add_field(name="<:casesarrow:696516134962462771> New Cases", value="{:,}".format(data['todayCases']))
            embed.add_field(name="<a:coronacases:696408215675732078> Active", value="{:,}".format(data['active']))
            embed.add_field(name="<:coronadeaths:696408166988120124> Deaths", value="{:,}".format(data['deaths']))
            embed.add_field(name="<:deathsarrow:696493553697947690> New Deaths", value="{:,}".format(data['todayDeaths']))
            embed.add_field(name="<:coronarecovered:696408101078827049> Recovered", value="{:,}".format(data['recovered']))
            
            return embed
        
        await ctx.send(embed=create_embed(data_today, country_flag, title, "today", time))
        await ctx.send(embed=create_embed(data_yesterday, country_flag, title, "yesterday", time))
        await ctx.send(embed=create_embed(data_twoDaysAgo, country_flag, title, "two days ago", time))


def setup(bot):
    bot.add_cog(Corona(bot))