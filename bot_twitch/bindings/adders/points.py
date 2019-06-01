from bot_twitch.libs.adder import adder
from data.models.points import Points
from data.models.config import Config

class points(adder):

    def __init__(self):
        print('Points Adder initiated')

    async def run_command(self, ctx):
        """ Allows streamer/mods to give points to users. Does not remove from anyone """

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

        recipient = msg_parts[3]

        if recipient.startswith('@'):
            recipient = recipient[1:]

        try:
            points_record = Points.get(Points.user == recipient)
        except Points.DoesNotExist as e:
            points_record = Points(user=recipient, points=0)

        points_record.points += amount
        points_record.save()

        point_name = self.get_points_name()
        if amount == 1:
            point_name = point_name[:-1]

        await ctx.send(f'@{ctx.message.author.name} has given {amount} {point_name} to @{recipient}')

    def get_wrong_format_message(self):
        return "The format for this method is: !add points {{amount}} {{recipient}}"

    def get_remove_points_message(self):
        return "Please use !remove points {{amount}} {{recipient}} to remove points. This command is strictly for adding points."

    def get_points_name(self):
        return Config.get(Config.key == 'point_name').value