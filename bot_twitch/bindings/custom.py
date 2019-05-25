from data.models.command import Command
from twitchio.ext import commands
from bot_twitch.libs.variable_parser import variable_parser
import distance

@commands.cog(name='custom')
class custom:

    def __init__(self, bot):
        print('Custom Command up and running')

    @commands.command(name='custom')
    async def binding(self, ctx):
        word_list = ctx.message.content.split()
        keyword = word_list[0][1:]

        try:
            msg = Command.get(Command.command == keyword).response
        except Command.DoesNotExist as e:
            cmds = [cmd for cmd in Command.select()
                if distance.levenshtein(keyword, cmd.command) <= 2]

            if len(cmds) is 1:
                msg = cmds[0].response
            else:
                msg = f'@{ctx.author.name}, I do not know which command you are trying to run. Please check your spelling and try again'
        finally:
            msg = variable_parser().run_parsers(msg, ctx)
            await ctx.send(msg)
