from bot_twitch.variable_parsers.parser import parser

class author_mention(parser):
    def __init__(self):
        print('Author Mention Variable Parser Engaged')
        self.variable = '{{author.mention}}'

    def parse(self, text, ctx):
        return text.replace(self.variable, f'@{ctx.author.name}')
