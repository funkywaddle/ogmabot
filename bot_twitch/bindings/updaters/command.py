from bot_twitch.libs.updater import updater
from data.models.command import Command

class command(updater):

    def __init__(self):
        print('Command Updater initiated')

    async def run_command(self, ctx):
        """ Allows streamer/mods to update custom commands """

        msg_parts = ctx.message.content.split()

        #msg_parts[0] == !update
        #msg_parts[1] == command
        #msg_parts[2] == {{command}}
        #msg_parts[3:] == {{command_message}}

        if len(msg_parts) <= 3:
            await ctx.send(self.get_wrong_format_message())
            return

        cmd = msg_parts[2]
        print(f'cmd: {cmd}')

        if cmd.startswith('!'):
            cmd = cmd[1:]
        print(f'cmd: {cmd}')

        response = msg_parts[3:]
        response = ' '.join(response)
        print(f'response: {response}')

        try:
            cmd = Command.get(Command.command == cmd)
            cmd.response = response
            cmd.save()
            print('command updated')
            await ctx.send(self.get_success_message())
        except Command.DoesNotExist as e:
            print('cmd doesn\'t exist')
            await ctx.send(self.get_run_add_not_update_message())

    def get_wrong_format_message(self):
        return "The format for this method is: !update command {{command}} {{command response}}"

    def get_run_add_not_update_message(self):
        return "This command does not exist. Please use !add command {{command}} {{command response}}"

    def get_success_message(self):
        return "Command updated successfully"
