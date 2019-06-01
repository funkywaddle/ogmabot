from twitchio.ext import commands
from data.models.points import Points
from data.models.config import Config

@commands.cog(name='give')
class give:

    def __init__(self, bot):
        print('Give loaded')
        self.bot = bot

    @commands.command(name='give')
    async def binding(self, ctx):
        msg_parts = ctx.message.content.split()

        if len(msg_parts) != 3:
            await ctx.send(self.get_wrong_format_message())
            return

        try:
            amount = int(msg_parts[1])
        except ValueError as e:
            await ctx.send(self.get_wrong_format_message())
            return

        if amount < 0:
            await ctx.send(self.get_remove_points_message())
            return

        recipient = msg_parts[2]
        giver = ctx.message.author.name

        if recipient.startswith('@'):
            recipient = recipient[1:]

        try:
            giver_points = Points.get(Points.user == giver)
        except Points.DoesNotExist as e:
            await ctx.send(self.get_not_enough_points_message())
            return

        if(giver_points.points < amount):
            await ctx.send(self.get_not_enough_points_message())
            return

        try:
            points_record = Points.get(Points.user == recipient)
        except Points.DoesNotExist as e:
            points_record = Points(user=recipient, points=0)

        points_record.points += amount
        points_record.save()

        giver_points.points -= amount
        giver_points.save()

        point_name = self.get_points_name()
        if amount == 1:
            point_name = point_name[:-1]

        await ctx.send(f'@{ctx.message.author.name} has given {amount} {point_name} to @{recipient}')

    def get_wrong_format_message(self):
        return "The format for this method is: !give {{amount}} {{recipient}}"

    def get_remove_points_message(self):
        return "You CANNOT give a fellow viewer negative points. Nice try!"

    def get_points_name(self):
        return Config.get(Config.key == 'point_name').value

    def get_not_enough_points_message(self):
        return "You do not have enough points to give"
#!give 1000 @defr3n