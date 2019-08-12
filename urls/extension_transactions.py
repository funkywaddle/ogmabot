from urls.base_url import BaseUrl


class ExtensionTransactions(BaseUrl):

    def __init__(self):
        self.url = f'{self.base}/extensions/transactions'
        self.parameters = self.get_parameters()
        self.required_scope = 'analytics:read:extensions'
        self.http_verb = 'GET'
        self.requires_oauth = True

    def get_parameters(self):
        return {
            'required': {
                'extension_id': None
            },
            'optional': {
                'id': None,
                'after': None,
                'first': None
            }
        }
