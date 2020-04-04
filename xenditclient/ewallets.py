from .exeptions import InvalidArgumentException


class EwalletClient(object):
    def __init__(self, client):
        """
        Ewallet Client
        :param client:
        """
        if not getattr(client, 'validate_params', False):
            raise TypeError('client must be contains a \'validate_params\' method')

        if not getattr(client, 'send_request', False):
            raise TypeError('client must be contains a \'send_request\' method')

        self.client = client
        self.client.set_api_version('2020-02-01')

    def get_url(self):
        return '/ewallets'

    def create(self, params: dict):
        ewallet_type = params.get('ewallet_type')
        if not ewallet_type:
            raise InvalidArgumentException('Please specify ewallet_type inside your parameters')
        self.validate_ewallet_type(ewallet_type)

        required_params = []
        if ewallet_type == 'OVO':
            required_params = ['external_id', 'amount', 'phone']
        if ewallet_type == 'DANA':
            required_params = ['external_id', 'amount', 'callback_url', 'redirect_url']

        if ewallet_type == 'LINKAJA':
            required_params = ['external_id', 'amount', 'phone', 'items', 'callback_url',
                               'redirect_url']

        self.client.validate_params(params, required_params)
        url = self.get_url()
        return self.client.send_request('post', url, params)

    def get_payment_status(self, external_id, ewallet_type):
        self.validate_ewallet_type(ewallet_type)
        url = '{base_url}?external_id={external_id}&ewallet_type={ewallet_type}'.format(
            base_url=self.get_url(),
            external_id=external_id,
            ewallet_type=ewallet_type
        )

        return self.client.send_request('get', url)

    def validate_ewallet_type(self, ewallet_type):
        if ewallet_type not in ['OVO', 'DANA', 'LINKAJA']:
            raise InvalidArgumentException('ewallet_type is not valid. '
                                           'it should be one of \'OVO\', \'DANA\', or \'LINKAJA\'')
