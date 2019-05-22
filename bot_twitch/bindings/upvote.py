from twitchio.ext import commands
from data.models.suggestion import Suggestion
from data.models.upvote import Upvote
from data.models.points import Points
from data.models.config import Config

@commands.cog(name='upvote')
class upvote:

    def __init__(self, bot):
        print('Upvote Cog loaded')
        self.bot = bot

    @commands.command(name='upvote')
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
                s_id = ctx.message.content.split()[1]

                suggestion = Suggestion.select().where(Suggestion.id == s_id)
                if suggestion.exists():
                    upvote, created = Upvote.get_or_create(
                        suggestion_id = s_id,
                        user = ctx.author.name
                    )

                    if created:
                        msg = f'You have upvoted the suggestion with id {s_id}.'
                    else:
                        msg = f'You have already upvoted that suggestion. You can\'t upvote it again.'
                else:
                    msg = f'Suggestion with id {s_id} does not exist.'

        await ctx.send(msg)

    def not_enough_points(self, ctx):
        return f'@{ctx.author.name} you need {self.point_cost} {self.point_name} to run this command.'

    def get_point_config(self):
        self.point_cost = Config.get(Config.key == 'upvote_cost').value
        self.point_name = Config.get(Config.key == 'point_name').value
        self.point_cost = int(self.point_cost)