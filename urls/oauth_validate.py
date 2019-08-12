from urls.base_url import BaseUrl


class OauthValidate(BaseUrl):

    def __init__(self):
        self.url = 'https://id.twitch.tv/oauth2/validate'
        self.parameters = self.get_parameters()
        self.required_scope = ''
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
