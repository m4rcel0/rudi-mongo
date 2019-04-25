import discord
from discord.ext import commands

class Util(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        """Shows bot latency to the server"""
        pong = await ctx.send("Pong!")
        delay = (pong.created_at - ctx.message.created_at).total_seconds() * 1000
        await pong.edit(content = f"Pong! `{int(delay)}ms`")
        print(f"Ping: {int(delay)}ms \t {ctx.message.author} \t {ctx.message.guild}")

    @commands.command(aliases=["uinfo", "ui"])
    async def userinfo(self, ctx, member: discord.Member = None):
        """Checks user info"""

        member = ctx.author if not member else member

        roles = [role for role in member.roles]

        embed = discord.Embed(colour=member.color)
        
        embed.set_author(name=f"User Info - {member}")
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        
        embed.add_field(name="ID:", value=member.id)
        embed.add_field(name="Nickname:", value=member.display_name)
        
        embed.add_field(name="Account created:", value=member.created_at.strftime("%#d %B %Y, %I:%M %p UTC"))
        embed.add_field(name="Joined this server:", value=member.joined_at.strftime("%#d %B %Y, %I:%M %p UTC"))

        embed.add_field(name=f"Roles ({len(roles)})", value="\n".join([role.mention for role in roles]))
        

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Util(bot))