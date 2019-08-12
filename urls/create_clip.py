from urls.base_url import BaseUrl


class CreateClip(BaseUrl):

    def __init__(self):
        self.url = f'{self.base}/clips'
        self.parameters = self.get_parameters()
        self.required_scope = 'clips:edit'
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
