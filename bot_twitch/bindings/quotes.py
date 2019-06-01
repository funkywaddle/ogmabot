from twitchio.ext import commands
from data.models.quotes import Quotes

@commands.cog(name='quote')
class quote:

    def __init__(self, bot):
        print('Quote Cog loaded')
        self.bot = bot

    @commands.command(name='quote')
    async def binding(self, ctx):
        msg = ctx.message.content
        print('got it')
        parts = msg.split()

        if len(parts) == 1:
            response = Quotes.select_random().quote
        elif len(parts) == 2:
            id = parts[1]
            if id.isdigit():
                try:
                    quote = Quotes.select().where(Quotes.id == id).get().quote
                    response = f'"{quote}" - {ctx.message.channel}'
                except Quotes.DoesNotExist as e:
                    response = f'Sorry, no quote with id {id} found.'
            else:
                response = f'The id needs to be a number. {id} IS NOT A NUMBER!!!'
        else:
            response = f'Wow, REALLY?! You think {msg} is how you call this command?'

        print(response)
        await ctx.send(response)