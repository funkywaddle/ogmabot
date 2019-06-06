import inspect
from twitchio.ext import commands
from bot_twitch.libs.updater import updater

@commands.cog(name='update')
class update:

    def __init__(self, bot):
        print('Update Cog loaded')
        self.bot = bot
        self.updaters = {}
        self.load_updaters()

    @commands.command(name='update')
    async def binding(self, ctx):
        msg_parts = ctx.message.content.split()
        if msg_parts[1] in self.updaters:
            await self.updaters[msg_parts[1]].run_command(ctx)

    def load_updaters(self):
        imported = __import__('bot_twitch.bindings.updaters', globals(), locals(), ['*'], 0)

        for name, obj in inspect.getmembers(imported, inspect.ismodule):
            for cname, cobj in inspect.getmembers(obj, inspect.isclass):
                updr = cobj()
                if isinstance(updr, updater) and not cname == updater.__name__:
                    self.updaters[cname] = updr