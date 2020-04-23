from .exeptions import InvalidAccountType


class BalanceClient(object):
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

    @classmethod
    def account_types(cls):
        return ["CASH", "HOLDING", "TAX"]

    def validate_account_type(self, account_type):
        if account_type not in self.account_types():
            raise InvalidAccountType("Invalid Account type. Available types: CASH, TAX, HOLDING")

    def get_balance(self, account_type):
        self.validate_account_type(account_type)
        url = '/balance?account_type={0}'.format(account_type)
        return self.client.send_request('get', url)
