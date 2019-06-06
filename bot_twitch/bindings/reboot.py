from twitchio.ext import commands

@commands.cog(name='reboot')
class reboot:

    def __init__(self, bot):
        print('Reboot loaded')
        self.bot = bot

    @commands.command(name='reboot')
    async def binding(self, ctx):
        pass