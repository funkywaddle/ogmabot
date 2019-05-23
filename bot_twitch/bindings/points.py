from twitchio.ext import commands
from data.models.points import Points
from data.models.config import Config

@commands.cog(name='points')
class points:

	def __init__(self, bot):
		print('Points Cog loaded')
		self.bot = bot

	@commands.command(name='points')
	async def binding(self, ctx):
		point_name = Config.get(Config.key=='point_name').value
		person, have, points = self.get_points(ctx)

		if points == 1:
			point_name = point_name[0:-1]

		msg = f'{person} {have} {points} {point_name}'
		await ctx.send(msg)

	def get_points(self, ctx):
		msg_parts = ctx.message.content.split()

		if len(msg_parts) == 1:
			person = 'You'
			have = 'have'

			try:
				points = Points.get(Points.user==ctx.message.author.name).points
			except Points.DoesNotExist as e:
				points = 0
		elif len(msg_parts) == 2:
			user = msg_parts[1]
			user = user[1:] if user.startswith('@') else user
			person = f'@{user}'
			have = 'has'

			try:
				points = Points.get(Points.user==user).points
			except Points.DoesNotExist as e:
				points = 0
		return (person, have, points)