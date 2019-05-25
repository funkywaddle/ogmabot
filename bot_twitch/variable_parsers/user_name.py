import re
from bot_twitch.variable_parsers.parser import parser

class user_name(parser):
    def __init__(self):
        super().__init__()
        print('User Name Variable Parser Engaged')
        self.variable = 'user.name'

    def parse(self, text, ctx):
        parameters = ctx.message.content.split()
        pattern = f'{self.var_open}{self.variable}\|(\d+){self.var_close}'
        match = re.search(pattern, text)

        if match is not None:
            parameter_num = int(match.group(1))
            found = f'{self.var_open}{self.variable}|{parameter_num}{self.var_close}'

            if len(parameters) >= parameter_num:
                user = parameters[parameter_num]
                if user.startswith('@'):
                    user = user[1:]
                text = text.replace(found, user)

        return text
