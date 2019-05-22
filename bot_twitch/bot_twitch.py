from twitchio.ext import commands
import inspect
from bot_twitch import bindings
from bot_twitch.config import tokens, config

class bot_twitch(commands.Bot):

    def __init__(self):
        print('Ogma Bot initiating')
        self.parsers = []
        super().__init__(
            irc_token=tokens.OAUTH,
            client_id=tokens.CLIENT_ID,
            nick=config.TWITCH_BOT_NICKNAME,
            prefix=config.PREFIX,
            initial_channels=[config.TWITCH_CHANNEL_NAME]
        )

    async def event_ready(self):
        self.load_orders()
        self.load_parsers()
        print('Ogma Bot initialized')

    async def event_usernotice_subscription(self, metadata):
        print(metadata)

    async def handle_commands(self, message, ctx=None):
        if not message.content.startswith(config.PREFIX):
            return

        command = message.content.split()[0][1:]

        if command == 'poweroff':
            pass
        elif command in self.commands:
            await super().handle_commands(message, ctx)
        else:
            cmd = self.commands['custom']
            if ctx is None:
                try:
                    ctx = await self.get_context(message)
                except Exception as e:
                    return await self.event_error(e, message.raw_data)

            await cmd._callback(self.modules[config.CATCH_ALL_COMMAND], ctx)

    def load_orders(self):
        from os.path import dirname, basename, isfile
        import glob
        modules = glob.glob(dirname(__file__)+"/bindings/*.py")
        commands = [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py') and not basename(f).startswith('_')]
        for cmd in commands:
            self.load_module(name=f'bot_twitch.bindings.{cmd}')

    def load_parsers(self):
        imported = __import__('bot_twitch.variable_parsers', globals(), locals(), ['*'], 0)

        for name, obj in inspect.getmembers(imported, inspect.ismodule):
            for cname, cobj in inspect.getmembers(obj, inspect.isclass):
                self.parsers.append(cobj())
