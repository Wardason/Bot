import time
from discord.ext import commands
import discord


class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, ex):
        print(ex)
        await ctx.send("Please check with $help the usage of this command")

    @commands.command(brief="The bot developer")
    async def developer(self, ctx):
        embed = discord.Embed()
        embed.add_field(name="", value="")
        await ctx.send("This bot is developed by Leonard Warda. Find me on:\nTwitter: Wardason_\nInstagram: "
                       "leonardwarda\nGithub: Wardason")

    @commands.command(brief="F for lasse")
    async def lucylover(self, ctx):
        await ctx.channel.send("https://imgur.com/ndrIfTz")

    @commands.command(name="knecht")
    async def bene(self, ctx):
        await ctx.channel.send("https://imgur.com/a/BobfAHs")
        time.sleep(1)
        await ctx.channel.send("spaß")



def setup(bot):
    bot.add_cog(Basic(bot))
