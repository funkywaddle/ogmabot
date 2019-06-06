from twitchio.ext import commands

@commands.cog(name='poweroff')
class poweroff:

    def __init__(self, bot):
        print('Poweroff loaded')
        self.bot = bot

    @commands.command(name='poweroff')
    async def binding(self, ctx):
        pass