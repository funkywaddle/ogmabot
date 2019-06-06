import inspect
from twitchio.ext import commands
from bot_twitch.libs.remover import remover

@commands.cog(name='remove')
class remove:

    def __init__(self, bot):
        print('Remove Cog loaded')
        self.bot = bot
        self.removers = {}
        self.load_removers()

    @commands.command(name='remove')
    async def binding(self, ctx):
        msg_parts = ctx.message.content.split()
        if msg_parts[1] in self.removers:
            await self.removers[msg_parts[1]].run_command(ctx)

    def load_removers(self):
        imported = __import__('bot_twitch.bindings.removers', globals(), locals(), ['*'], 0)

        for name, obj in inspect.getmembers(imported, inspect.ismodule):
            for cname, cobj in inspect.getmembers(obj, inspect.isclass):
                rmr = cobj()
                if isinstance(rmr, remover) and not cname == remover.__name__:
                    self.removers[cname] = rmr