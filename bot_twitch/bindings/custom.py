from data.models.command import Command
from twitchio.ext import commands

@commands.cog(name='custom')
class custom:

    @commands.command(name='custom')
    async def binding(self, ctx):
        word_list = ctx.message.content.split()
        keyword = word_list[0][1:]
        custom_cmd = None

        try:
            custom_cmd = Command.get(Command.command == keyword).response
        except Command.DoesNotExist as e:
            pass

        await ctx.send(custom_cmd)
