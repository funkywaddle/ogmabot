from bot_twitch.libs.remover import remover
from data.models.points import Points
from data.models.config import Config

class points(remover):

    def __init__(self):
        print('Points Remover initiated')

    async def run_command(self, ctx):
        """ Allows streamer/mods to give points to users. Does not remove from anyone """

        # msg_parts[0] = !remove
        # msg_parts[1] = points
        # msg_parts[2] = {{amount}}
        # msg_parts[3] = {{user}}

        msg_parts = ctx.message.content.split()

        if len(msg_parts) != 4:
            await ctx.send(self.get_wrong_format_message())
            return

        try:
            amount = int(msg_parts[2])
        except ValueError as e:
            await ctx.send(self.get_wrong_format_message())
            return

        if amount < 0:
            await ctx.send(self.get_remove_points_message())
            return

        user = msg_parts[3]

        if user.startswith('@'):
            user = user[1:]

        try:
            points_record = Points.get(Points.user == user)
        except Points.DoesNotExist as e:
            await ctx.send(self.get_user_does_not_have_points_message())
            return

        points_record.points -= amount

        if points_record.points < 0:
            points_record.points = 0

        points_record.save()

        point_name = self.get_points_name()
        if amount == 1:
            point_name = point_name[:-1]

        await ctx.send(f'@{ctx.message.author.name} has removed {amount} {point_name} from @{recipient}')

    def get_wrong_format_message(self):
        return "The format for this method is: !remove points {{amount}} {{user}}"

    def get_remove_points_message(self):
        return "You cannot remove negative points from a user"

    def get_user_does_not_have_points_message(self):
        return "User has not accumulated any points yet. You cannot remove points from them."

    def get_points_name(self):
        return Config.get(Config.key == 'point_name').value