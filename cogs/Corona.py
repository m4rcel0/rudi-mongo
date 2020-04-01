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
        "coronavirus"
        "covid19"
    ])
    async def corona(self, ctx, target_country = None):
        """Fetches and displays Corona Virus current cases from the world"""

        try:
            r = requests.get("https://corona-stats.online?format=json")
        except:
            ctx.send("Unable to get information right now. Try again later or contact Cow... idk")
            return
        
        if not target_country:
            corona_stats = r.json()['worldStats']
            country_flag = "https://upload.wikimedia.org/wikipedia/commons/6/6f/Earth_Eastern_Hemisphere.jpg"
        else:
            corona_stats = None
            countries = r.json()['data']
            for country in countries:
                try:
                    if (country['country'].lower() == target_country.lower() or 
                    country['countryCode'].lower() == target_country.lower()):
                        corona_stats = country
                        country_flag = corona_stats['countryInfo']['flag']
                        break
                except:
                    pass

        if not corona_stats:
            await ctx.send("Could not find that country.")
            return


        cases_total = "{:,}".format(corona_stats['cases'])
        cases_new = "{:,}".format(corona_stats['todayCases'])
        cases_active = "{:,}".format(corona_stats['active'])
        deaths_total = "{:,}".format(corona_stats['deaths'])
        deaths_new = "{:,}".format(corona_stats['todayDeaths'])
        recovered = "{:,}".format(corona_stats['recovered'])

        embed = discord.Embed(colour=discord.Colour.purple(), title=corona_stats['country'] + " Coronavirus Status", url="https://www.worldometers.info/coronavirus/")
        
        embed.set_thumbnail(url=country_flag)
        embed.set_footer(text="🦇")

        embed.add_field(name="😷 Total Cases", value=cases_total)
        embed.add_field(name="🔼 New Cases", value=cases_new)
        embed.add_field(name="🤢 Active", value=cases_active)
        embed.add_field(name="💀 Deaths", value=deaths_total)
        embed.add_field(name="🔺 New Deaths", value=deaths_new)
        embed.add_field(name="🥳 Recovered", value=recovered)


        await ctx.send(embed=embed) 
    

def setup(bot):
    bot.add_cog(Corona(bot))