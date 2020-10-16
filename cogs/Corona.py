import requests
import json

import discord
from discord.ext import commands

from datetime import datetime

class Corona(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
   

    @commands.command(aliases=[
        "coronga",
        "covid",
        "coronavirus",
        "covid19"
    ])
    async def corona(self, ctx, *, target_country = None):
        """Display COVID19 data from countries or the world
            Usage:
            !corona
            !corona country
        """

        if not target_country:
            country_flag = "https://cdn.discordapp.com/attachments/587051836050112512/696495396628988014/W31X.gif"
            url_td = "http://corona.lmao.ninja/v2/all?yesterday=false"
            url_yt = "http://corona.lmao.ninja/v2/all?yesterday=true"
        else:
            url_td = "http://corona.lmao.ninja/v2/countries/" + target_country.lower() + "?yesterday=false&strict=false"
            url_yt = "http://corona.lmao.ninja/v2/countries/" + target_country.lower() + "?yesterday=true&strict=false"
            country_flag = None

        try:
            d_td = requests.get(url_td)
            d_yt = requests.get(url_yt)
            
            stats_td = d_td.json()
            stats_yt = d_yt.json()

        except:
            ctx.send("Unable to get information right now. Try again later or contact Cow... idk")
            return


        try:
            if not country_flag:
                country_flag = stats_td['countryInfo']['flag']

            td_cases_total = "{:,}".format(stats_td['cases'])
            td_cases_new = "{:,}".format(stats_td['todayCases'])
            td_cases_active = "{:,}".format(stats_td['active'])
            td_deaths_total = "{:,}".format(stats_td['deaths'])
            td_deaths_new = "{:,}".format(stats_td['todayDeaths'])
            td_recovered = "{:,}".format(stats_td['recovered'])

            yt_cases_total = "{:,}".format(stats_yt['cases'])
            yt_cases_new = "{:,}".format(stats_yt['todayCases'])
            yt_cases_active = "{:,}".format(stats_yt['active'])
            yt_deaths_total = "{:,}".format(stats_yt['deaths'])
            yt_deaths_new = "{:,}".format(stats_yt['todayDeaths'])
            yt_recovered = "{:,}".format(stats_yt['recovered'])
            
            updated = datetime.utcfromtimestamp(stats_td['updated']/1000).strftime('%H:%M(UTC) %A %d-%m-%Y')
        except:
            await ctx.send("Country not found, maybe it has no cases, or you need to type better idk <:peeposhrug:596749393575804937>")
            return

        try:
            title = stats_td['country']
        except:
            title = "World"

        embed = discord.Embed(colour=discord.Colour.purple(), title=title + " Coronavirus Status", url="https://www.worldometers.info/coronavirus/")
        
        embed.set_thumbnail(url=country_flag)
        embed.set_footer(text="Last updated: " + updated)

        embed.add_field(name="TODAY", value="---------------" , inline=False)
        embed.add_field(name="<:totalcases:696506315131846717> Total", value=td_cases_total)
        embed.add_field(name="<:casesarrow:696516134962462771> New Cases", value=td_cases_new)
        embed.add_field(name="<a:coronacases:696408215675732078> Active", value=td_cases_active)
        embed.add_field(name="<:coronadeaths:696408166988120124> Deaths", value=td_deaths_total)
        embed.add_field(name="<:deathsarrow:696493553697947690> New Deaths", value=td_deaths_new)
        embed.add_field(name="<:coronarecovered:696408101078827049> Recovered", value=td_recovered)
        
        embed.add_field(name="YESTERDAY", value="---------------", inline=False)
        embed.add_field(name="<:totalcases:696506315131846717> Total", value=yt_cases_total)
        embed.add_field(name="<:casesarrow:696516134962462771> New Cases", value=yt_cases_new)
        embed.add_field(name="<a:coronacases:696408215675732078> Active", value=yt_cases_active)
        embed.add_field(name="<:coronadeaths:696408166988120124> Deaths", value=yt_deaths_total)
        embed.add_field(name="<:deathsarrow:696493553697947690> New Deaths", value=yt_deaths_new)
        embed.add_field(name="<:coronarecovered:696408101078827049> Recovered", value=yt_recovered) 


        await ctx.send(embed=embed) 


def setup(bot):
    bot.add_cog(Corona(bot))