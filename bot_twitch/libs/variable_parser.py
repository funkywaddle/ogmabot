import inspect

class variable_parser:

    def __init__(self):
        self.parsers = []
        self.get_parsers()

    def parse(self, text, ctx):
        """
            The method that the child parsers will use
            to parse their particular variables
        """
        pass

    def run_parsers(self, text, ctx):
        for parser in self.parsers:
            text = parser.parse(text, ctx)
        return text

    def get_parsers(self):
        imported = __import__('bot_twitch.variable_parsers', globals(), locals(), ['*'], 0)

        for name, obj in inspect.getmembers(imported, inspect.ismodule):
            for cname, cobj in inspect.getmembers(obj, inspect.isclass):
                self.parsers.append(cobj())