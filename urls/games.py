from urls.base_url import BaseUrl


class Games(BaseUrl):

    def __init__(self):
        self.url = f'{self.base}/games'
        self.parameters = self.get_parameters()
        self.http_verb = 'GET'

    def get_parameters(self):
        return {
            'required': {
                'id': None,
                'name': None
            },
            'optional': {
                'after': None,
                'before': None,
                'first': None
            }
        }
