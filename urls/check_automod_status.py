from urls.base_url import BaseUrl


class CheckAutoModStatus(BaseUrl):

    def __init__(self):
        self.url = f'{self.base}/moderation/enforcements/status'
        self.parameters = self.get_parameters()
        self.required_scope = 'moderation:read'
        self.http_verb = 'POST'

    def get_parameters(self):
        return {
            'required': {
                'broadcaster_id': None
            },
            'optional': {
                'has_delay': None
            }
        }
