from bot_twitch.libs.updater import updater
from data.models.config import Config

class config(updater):

    def __init__(self):
        print('Config Updater initiated')

    async def run_command(self, ctx):
        """ Allows streamer/mods to update config settings """

        #msg_parts[0] == !update
        #msg_parts[1] == config
        #msg_parts[2] == {{key}}
        #msg_parts[3:] == {{value}}

        msg_parts = ctx.message.content.split()

        if len(msg_parts) <= 3:
            await ctx.send(self.get_wrong_format_message())
            return

        key = self.get_config_key(msg_parts)
        print(f'key: {key}')

        value = self.get_config_value(msg_parts)
        print(f'value: {value}')

        try:
            self.set_config_value(key, value)
            print('config updated')
            await ctx.send(self.get_success_message())
        except Config.DoesNotExist as e:
            print('config doesn\'t exist')
            await ctx.send(self.get_config_does_not_exist_message())

    def get_config_key(self, msg_parts):
        return msg_parts[2]

    def get_config_value(self, msg_parts):
        value = msg_parts[3:]
        return ' '.join(value)

    def set_config_value(self, key, value):
        config = Config.get(Config.key == key)
        config.value = value
        config.save()

    def get_wrong_format_message(self):
        return "The format for this method is: !update config {{key}} {{value}}"

    def get_config_does_not_exist_message(self):
        return "That config does not exist"

    def get_success_message(self):
        return "Config updated successfully"
