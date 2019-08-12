from urls.base_url import BaseUrl


class ExtensionAnalytics(BaseUrl):

    def __init__(self):
        self.url = f'{self.base}/analytics/extensions'
        self.parameters = self.get_parameters()
        self.required_scope = 'analytics:read:extensions'
        self.http_verb = 'GET'

    def get_parameters(self):
        return {
            'required': {},
            'optional': {
                'after': None,
                'ended_at': None,
                'extension_id': None,
                'first': None,
                'started_at': None,
                'type': None
            }
        }
