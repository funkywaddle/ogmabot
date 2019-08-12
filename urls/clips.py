from urls.base_url import BaseUrl


class Clips(BaseUrl):

    def __init__(self):
        self.url = f'{self.base}/clips'
        self.parameters = self.get_parameters()
        self.http_verb = 'GET'

    def get_parameters(self):
        return {
            'required': {
                'broadcaster_id': None,
                'game_id': None,
                'id': None
            },
            'optional': {
                'after': None,
                'before': None,
                'ended_at': None,
                'first': None,
                'started_at': None
            }
        }
