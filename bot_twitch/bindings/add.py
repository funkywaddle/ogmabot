import inspect
from twitchio.ext import commands
from bot_twitch.libs.adder import adder

@commands.cog(name='add')
class add:

    def __init__(self, bot):
        print('Add Cog loaded')
        self.bot = bot
        self.adders = {}
        self.load_adders()

    @commands.command(name='add')
    async def binding(self, ctx):
        msg_parts = ctx.message.content.split()
        if msg_parts[1] in self.adders:
            await self.adders[msg_parts[1]].run_command(ctx)

    def load_adders(self):
        imported = __import__('bot_twitch.bindings.adders', globals(), locals(), ['*'], 0)

        for name, obj in inspect.getmembers(imported, inspect.ismodule):
            for cname, cobj in inspect.getmembers(obj, inspect.isclass):
                adr = cobj()
                if isinstance(adr, adder) and not cname == adder.__name__:
                    self.adders[cname] = adr