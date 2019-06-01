from twitchio.ext import commands

@commands.cog(name='bug')
class bug:

    def __init__(self, bot):
        print('Bug Cog loaded')
        self.bot = bot

    @commands.command(name='bug')
    async def binding(self, ctx):
        pass