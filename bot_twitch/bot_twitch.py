import twitch
import inspect
from bot_twitch import tokens, config

class bot_twitch():

    def __init__(self):
        print('Twitch bot initiating')
        self.helix = twitch.Helix(tokens.PROD)
        self.commands = {}
        self.load_commands()


    def run(self):
        try:
            twitch.Chat(
                channel=f'#{config.TWITCH_CHANNEL_NAME}',
                nickname=f'{config.TWITCH_BOT_NICKNAME}',
                oauth=f'{tokens.OAUTH}',
                helix=self.helix).subscribe(
                    lambda message: self.message_handler(message)
            )
        except KeyboardInterrupt as e:
            print('Shutting down bot.....')


    def message_handler(self, message):
        if not message.text.startswith('!'):
            return

        command = message.text.split()[0][1:]
        if command in self.commands:
            self.commands[command].run_command(message.text)

    def load_commands(self):
        commands = __import__('bot_twitch.commands', globals(), locals(), ['*'], 0)
        for name, obj in inspect.getmembers(commands, inspect.ismodule):
            for cname, cobj in inspect.getmembers(obj, inspect.isclass):
                self.commands[cname] = cobj()