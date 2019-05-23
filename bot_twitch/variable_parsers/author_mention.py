class author_mention:
    def __init__(self):
        print('Author Mention Variable Parser Engaged')
        self.variable = '{{author.mention}}'

    def parse(self, text, ctx):
        return text.replace(self.variable, f'@{ctx.author.name}')
