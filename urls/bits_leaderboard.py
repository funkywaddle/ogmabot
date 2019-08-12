from urls.base_url import BaseUrl


class BitsLeaderboard(BaseUrl):

    def __init__(self):
        self.url = f'{self.base}/bits/leaderboard'
        self.parameters = self.get_parameters()
        self.required_scope = 'bits:read'
        self.http_verb = 'GET'

    def get_parameters(self):
        return {
            'required': {},
            'optional': {
                'count': None,
                'period': None,
                'started_at': None,
                'user_id': None
            }
        }
