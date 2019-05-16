import discord
from discord.ext import commands
import asyncio

import logging
from bot_discord import config
from bot_discord import tokens

class bot_discord(discord.Client):

    def __init__(self):
        print('Discord bot initiated')
        self.startup_extensions = []
        self.bot = self.get_bot()
        self.setup_logging()
        self.load_extensions()

    def load_extensions(self):
        for ext in self.startup_extensions:
            try:
                self.bot.load_extensions(ext)
            except Exception as e:
                exc = '{}: {}'.format(type(e).__name__, e)
                msg = f'[ERR] Can\'t load extension {ext}\n{exc}'
                self.bot.logger.error(msg)
                print(msg)

    def run(self):
        print('Discord bot: RUN!!!')
        asyncio.run(self.bot.start(tokens.PROD, bot=True, reconnect=True))


    def get_prefix(bot, message):
        prefixes = [config.PREFIX]
        return commands.when_mentioned_or(*prefixes)(bot, message)

    def get_bot(self):
        return commands.Bot(command_prefix=self.get_prefix, description=config.DESCRIPTION)

    def setup_logging(self):
        # Setup logger.
        logger = logging.getLogger('Ogma')
        logger.setLevel(logging.DEBUG)
        handler = logging.FileHandler(filename='ogma.log',
                                      encoding='utf-8',
                                      mode='a')
        form = '%(asctime)s:%(levelname)s:%(name)s:%(message)s'
        handler.setFormatter(logging.Formatter())
        logger.addHandler(handler)
        self.bot.logger = logger

    async def on_ready(self):
        self.bot.logger.info(f'Logged in as: {self.bot.user.name}')
        await self.bot.change_presence(activity=discord.Game(name=config.PRESENCE))


    async def on_message(self, message):

        #No bot, you cannot send your own commands!!
        if message.author == self.bot.user:
            return

        if message.content.startswith(config.PREFIX):
            pass


