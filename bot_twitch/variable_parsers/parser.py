from data.models.config import Config

class parser:

    def __init__(self):
        self.var_open = self.get_var_open()
        self.var_close = self.get_var_close()

    def parse(self, text, ctx):
        pass

    def get_var_open(self):
        return self.get_config('custom_command_variable_open')

    def get_var_close(self):
        return self.get_config('custom_command_variable_close')

    def get_config(self, key):
        config = None
        try:
            config = Config.get(Config.key == key).value
        except Config.DoesNotExist as e:
            config = None
        finally:
            return config