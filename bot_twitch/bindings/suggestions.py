from twitchio.ext import commands
from peewee import fn
from data.models.suggestion import Suggestion
from data.models.upvote import Upvote

@commands.cog(name='suggestions')
class suggestions:

    def __init__(self, bot):
        print('Suggestions Cog loaded')
        self.bot = bot

    @commands.command(name='suggestions')
    async def binding(self, ctx):

        output = []

        suggestions = (Suggestion
                        .select(Suggestion, fn.COUNT(Upvote.id).alias('upvote_count'))
                        .join(Upvote)
                        .group_by(Suggestion)
                        .order_by(fn.COUNT(Upvote.id).desc())
                    )

        for sug in suggestions:
            times = 'time'
            if int(sug.upvote_count) > 1:
                times += 's'
            output.append(f'{sug.suggestion} | ID: {sug.id} | {sug.upvote_count} votes')

        await ctx.send("""
            """.join(output))
