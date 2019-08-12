from urls.base_url import BaseUrl


class TopGames(BaseUrl):

    def __init__(self):
        self.url = f'{self.base}/games/top'
        self.parameters = self.get_parameters()
        self.http_verb = 'GET'

    def get_parameters(self):
        return {
            'required': {},
            'optional': {
                'after': None,
                'before': None,
                'first': None
            }
        }
