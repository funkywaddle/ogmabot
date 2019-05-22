class author_name:
    def __init__(self):
        print('Author Name Variable Parser Engaged')
        self.variable = '{{author_name}}'

    def parse(self, text, ctx):
        msg = text.replace(self.variable, '{}'.format(ctx.author.name))
        return msg
