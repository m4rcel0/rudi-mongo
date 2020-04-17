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
            url = "http://corona.lmao.ninja/v2/all?yesterday=false"
        else:
            url = "http://corona.lmao.ninja/v2/countries/" + target_country.lower() + "?yesterday=false&strict=false"
            country_flag = None

        try:
            r = requests.get(url)
            corona_stats = r.json()
        except:
            ctx.send("Unable to get information right now. Try again later or contact Cow... idk")
            return


        try:
            if not country_flag:
                country_flag = corona_stats['countryInfo']['flag']
            cases_total = "{:,}".format(corona_stats['cases'])
            cases_new = "{:,}".format(corona_stats['todayCases'])
            cases_active = "{:,}".format(corona_stats['active'])
            deaths_total = "{:,}".format(corona_stats['deaths'])
            deaths_new = "{:,}".format(corona_stats['todayDeaths'])
            recovered = "{:,}".format(corona_stats['recovered'])
            updated = datetime.utcfromtimestamp(corona_stats['updated']/1000).strftime('%H:%M(UTC) %A %d-%m-%Y')
        except:
            await ctx.send("Country not found, maybe it has no cases, or you need to type better idk <:peeposhrug:596749393575804937>")
            return

        try:
            title = corona_stats['country']
        except:
            title = "World"

        embed = discord.Embed(colour=discord.Colour.purple(), title=title + " Coronavirus Status", url="https://www.worldometers.info/coronavirus/")
        
        embed.set_thumbnail(url=country_flag)
        embed.set_footer(text="Last updated: " + updated)

        embed.add_field(name="<:totalcases:696506315131846717> Total", value=cases_total)
        embed.add_field(name="<:casesarrow:696516134962462771> New Cases", value=cases_new)
        embed.add_field(name="<a:coronacases:696408215675732078> Active", value=cases_active)
        embed.add_field(name="<:coronadeaths:696408166988120124> Deaths", value=deaths_total)
        embed.add_field(name="<:deathsarrow:696493553697947690> New Deaths", value=deaths_new)
        embed.add_field(name="<:coronarecovered:696408101078827049> Recovered", value=recovered)


        await ctx.send(embed=embed) 
    

def setup(bot):
    bot.add_cog(Corona(bot))