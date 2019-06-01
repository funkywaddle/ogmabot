from bot_twitch.libs.adder import adder
from data.models.quotes import Quotes

class quote(adder):

    def __init__(self):
        print('Quote Adder initiated')

    async def run_command(self, ctx):
        """ Allows anyone to add quotes """

        msg_parts = ctx.message.content.split()

        if len(msg_parts) <= 2:
            await ctx.send(self.get_wrong_format_message())
            return

        quote = msg_parts[2:]

        added_quote = Quotes(quote=' '.join(quote))
        added_quote.save()

        await ctx.send(f'@{ctx.message.author.name} has added quote with id: {added_quote.id}')

    def get_wrong_format_message(self):
        return "The format for this method is: !add quote {{quote}}"
