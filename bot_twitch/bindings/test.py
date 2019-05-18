from twitchio.ext import commands

@commands.cog(name='test')
class test:

    @commands.command(name='test')
    async def binding(self, ctx):
        print('***TEST COMMAND CALLED***')
        await ctx.send('Test message response')
