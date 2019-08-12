class BaseUrl:

    def __init(self):
        self.base = 'https://api.twitch.tv/helix'
        self.required_scope = ''
        self.requires_oauth = False
        self.http_verb = 'GET'

    def get_url_parameters(self):
        return {
            'required': {},
            'either_or_required': {},
            'optional': {}
        }

    def get_body_parameters(self):
        return {
            'required': {},
            'either_or_required': {},
            'optional': {}
        }

    def get_headers(self):
        pass
