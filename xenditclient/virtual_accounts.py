from .exceptions import InvalidArgumentException

SAHABAT_SAMPOERNA = 'SAHABAT_SAMPOERNA'
MANDIRI = 'MANDIRI'
PERMATA = 'PERMATA'
BNI = 'BNI'
BRI = 'BRI'
BCA = 'BCA'


class VirtualAccountClient(object):
    def __init__(self, client):
        """
        Virtual Account Client
        :param client:
        """
        self.client = client

    def get_url(self):
        return '/callback_virtual_accounts'

    def create(self, external_id, bank_code, name, **kwargs):
        """
        :required params:
            external_id: str
            bank_code: str
            name: str

        :optional params:
            virtual_account_number: str // Optional
            suggested_amount: int // Optional
            is_closed: bool // Optional
            expected_amount: int // Optional
            expiration_date: UTC datetime // Optional
            is_single_use: bool // Optional
            description: str // Optional

        :return:
        """
        virtual_account_number = kwargs.get('virtual_account_number')
        suggested_amount = kwargs.get('suggested_amount')
        is_closed = kwargs.get('is_closed')
        expected_amount = kwargs.get('expected_amount')
        expiration_date = kwargs.get('expiration_date')
        is_single_use = kwargs.get('is_single_use')
        description = kwargs.get('description')

        bank_codes = [BCA, BNI, BRI, PERMATA, MANDIRI, SAHABAT_SAMPOERNA]

        if bank_code not in bank_codes:
            raise InvalidArgumentException(f'bank_code is not valid. '
                                           f'It must be one of {", ".join(bank_codes)}')

        url = self.get_url()
        data = dict(
            name=name,
            bank_code=bank_code,
            external_id=external_id
        )

        if is_closed: data.update({'is_closed': is_closed})
        if virtual_account_number: data.update({'virtual_account_number': virtual_account_number})
        if suggested_amount: data.update({'suggested_amount': suggested_amount})
        if expected_amount: data.update({'expected_amount': expected_amount})
        if expiration_date: data.update({'expiration_date': expiration_date.isoformat()})
        if is_single_use: data.update({'is_single_use': is_single_use})
        if description: data.update({'description': description})

        return self.client.send_request('post', url, data)

    def get_va_banks(self):
        url = '/available_virtual_account_banks'
        return self.client.send_request('get', url)

    def get_payment_detail(self, payment_id):
        """
        Get Virtual Account Payment
        :return:
        """
        url = f'/callback_virtual_accounts/{payment_id}'
        return self.client.send_request('get', url)

    def update_payment_detail(self, payment_id, suggested_amount=None, expected_amount=None,
                              expiration_date=None, is_single_use=None, description=None):
        """
        Update FVA Payment

        :param payment_id: required
        :param suggested_amount:
        :param expected_amount:
        :param expiration_date:
        :param is_single_use:
        :param description:
        :return:
        """
        url, data = (f'/callback_virtual_accounts/{payment_id}', dict())
        data = dict()
        if suggested_amount: data.update({'suggested_amount': suggested_amount})
        if expected_amount: data.update({'expected_amount': expected_amount})
        if expiration_date: data.update({'expiration_date': expiration_date.isoformat()})
        if is_single_use: data.update({'is_single_use': is_single_use})
        if description: data.update({'description': description})
        return self.client.send_request('patch', url, data)
