class user_mention:
    def __init__(self):
        print('User Mention Variable Parser Engaged')
        self.variable = '{{user.mention}}'

    def parse(self, text, ctx):
        msg = ctx.message.content
        parameters = msg.split()[1:]

        return text.replace(self.variable, f'@{parameters[0]}')
