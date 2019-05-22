from twitchio.ext import commands
from data.models.suggestion import Suggestion
from data.models.upvote import Upvote
from data.models.points import Points
from data.models.config import Config

@commands.cog(name='suggest')
class suggest:

    def __init__(self, bot):
        print('Suggest Cog loaded')
        self.bot = bot

    @commands.command(name='suggest')
    async def binding(self, ctx):
        self.get_point_config()

        do_it = False

        try:
            user_points = Points.get(Points.user == ctx.author.name)
            do_it = True
        except Points.DoesNotExist as e:
            msg = self.not_enough_points(ctx)
            if self.point_cost == 0:
                do_it = True
            else:
                do_it = False
        else:
            point_ttl = int(user_points.points)
            if point_ttl < self.point_cost:
                msg = self.not_enough_points(ctx)
                do_it = False
            else:
                new_point_ttl = point_ttl - self.point_cost
                user_points.points = new_point_ttl
                user_points.save()
                do_it = True
        finally:
            if do_it:
                message = ctx.message.content.split()[1:]

                suggestion = Suggestion(suggestion=' '.join(message), user=ctx.author.name)
                suggestion.save()

                upvote = Upvote(suggestion=suggestion, user=ctx.author.name)
                upvote.save()

                msg = f'@{ctx.author.name}, your suggestion has been saved. Thank you for taking the time to make the stream a better place.'
        await ctx.send(msg)

    def not_enough_points(self, ctx):
        return f'@{ctx.author.name} you need {self.point_cost} {self.point_name} to run this command.'

    def get_point_config(self):
        self.point_cost = Config.get(Config.key == 'suggestion_cost').value
        self.point_name = Config.get(Config.key == 'point_name').value
        self.point_cost = int(self.point_cost)