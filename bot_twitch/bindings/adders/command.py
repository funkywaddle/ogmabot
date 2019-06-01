from bot_twitch.libs.adder import adder
from data.models.command import Command

class command(adder):

    def __init__(self):
        print('Command Adder initiated')

    async def run_command(self, ctx):
        """ Allows streamer/mods to add custom commands """

        msg_parts = ctx.message.content.split()

        #msg_parts[0] == !add
        #msg_parts[1] == command
        #msg_parts[2] == {{command}}
        #msg_parts[3:] == {{command_message}}

        if len(msg_parts) <= 4:
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
            print('cmd already exists')
            await ctx.send(self.get_run_update_not_add_message())
        except Command.DoesNotExist as e:
            cmd = Command(command=cmd, response=response)
            cmd.save()
            print('new command created')
            await ctx.send(self.get_success_message())

    def get_wrong_format_message(self):
        return "The format for this method is: !add command {{command}} {{command response}}"

    def get_run_update_not_add_message(self):
        return "This command already exists. Please use !update command {{command}} {{command response}}"

    def get_success_message(self):
        return "Command added successfully"
