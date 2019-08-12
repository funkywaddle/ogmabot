from urls.base_url import BaseUrl


class GameAnalytics(BaseUrl):

    def __init__(self):
        self.url = f'{self.base}/analytics/games'
        self.parameters = self.get_parameters()
        self.required_scope = 'analytics:read:games'
        self.http_verb = 'GET'

    def get_parameters(self):
        return {
            'required': {},
            'optional': {
                'after': None,
                'ended_at': None,
                'first': None,
                'game_id': None,
                'started_at': None,
                'type': None
            }
        }
