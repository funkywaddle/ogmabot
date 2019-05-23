class author_name:
    def __init__(self):
        print('Author Name Variable Parser Engaged')
        self.variable = '{{author.name}}'

    def parse(self, text, ctx):
        return text.replace(self.variable, ctx.author.name)
