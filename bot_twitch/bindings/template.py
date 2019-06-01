from twitchio.ext import commands

@commands.cog(name='template')
class template:

    def __init__(self, bot):
        print('Template loaded')
        self.bot = bot

    @commands.command(name='template')
    async def binding(self, ctx):
        pass