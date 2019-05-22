from data.models.command import Command
from twitchio.ext import commands

@commands.cog(name='tsundere')
class tsundere:

    @commands.command(name='tsundere')
    async def binding(self, ctx):
        print('TsundereTubeWorm was here')
