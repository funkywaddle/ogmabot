from data.models.command import Command
from twitchio.ext import commands
import distance

@commands.cog(name='custom')
class custom:

    @commands.command(name='custom')
    async def binding(self, ctx):
        word_list = ctx.message.content.split()
        keyword = word_list[0][1:]
        test = ctx.command

        try:
            msg = Command.get(Command.command == keyword).response
        except Command.DoesNotExist as e:
            cmds = [cmd for cmd in Command.select()
                if distance.levenshtein(keyword, cmd.command) <= 2]

            if len(cmds) is 1:
                msg = cmds[0].response

            else:
                msg = f'@{ctx.author.name}, I do not know which command you are trying to run. Please check your spelling and try again'
                msg = f'@{ctx.author.name}, I do not know which command you are trying to run. Please check your spelling and try again'
        finally:
            await ctx.send(msg)
