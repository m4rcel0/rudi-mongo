import requests
import json

import discord
from discord.ext import commands

from datetime import datetime

from millify import millify
from millify import prettify

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
            await ctx.send("Unable to get information right now. Try again later or contact Cow... idk")
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
                
            
            
            todayCases = prettify(data['todayCases'])
            todayDeaths = prettify(data['todayDeaths'])
            todayRecovered = prettify(data['todayRecovered'])
            activeCases = millify(data['active'], precision=2)
            population = millify(data['population'], precision=2)
            totalCases = millify(data['cases'], precision=2)
            tests = millify(data['tests'], precision=2)
            recovered = millify(data['recovered'], precision=2)
            totalDeaths = millify(data['deaths'], precision=2)
            
            
            
            embed.add_field(name="<:casesarrow:696516134962462771> New Cases", value=todayCases)
            embed.add_field(name="<:deathsarrow:696493553697947690> New Deaths", value=todayDeaths)
            embed.add_field(name="⛑️ New Recoveries", value=todayRecovered)
            
            embed.add_field(name="<:totalcases:696506315131846717> Total Cases", value=totalCases + " **({:.2f}%)**".format(calc_percentage(data['cases'], data['population'])) )
            embed.add_field(name="<:coronadeaths:696408166988120124> Total Deaths", value=totalDeaths + " **({:.2f}%)**".format(calc_percentage(data['deaths'], data['cases'])) )
            embed.add_field(name="<:coronarecovered:696408101078827049> Total Recovered", value=recovered + " **({:.2f}%)**".format(calc_percentage(data['recovered'], data['cases'])) )
            
            embed.add_field(name="<a:coronacases:696408215675732078> Active Cases", value=activeCases + " **({:.2f}%)**".format(calc_percentage(data['active'], data['population'])) )
            embed.add_field(name="🧪 Tests", value=tests)
            embed.add_field(name="<:coronapopulation:813592002293792788> Population", value=population)
            
            
            
            return embed
        
        def calc_percentage(cases, population):
            percentage = int(cases)/int(population)*100
            return percentage
        
        await ctx.send(embed=create_embed(data_today, country_flag, title, "today", time))
        await ctx.send(embed=create_embed(data_yesterday, country_flag, title, "yesterday", time))
        await ctx.send(embed=create_embed(data_twoDaysAgo, country_flag, title, "two days ago", time))


def setup(bot):
    bot.add_cog(Corona(bot))