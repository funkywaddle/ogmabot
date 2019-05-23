class user_name:
    def __init__(self):
        print('User Name Variable Parser Engaged')
        self.variable = '{{user.name}}'

    def parse(self, text, ctx):
        msg = ctx.message.content
        parameters = msg.split()[1:]

        return text.replace(self.variable, parameters[0])
