from xenditclient.exceptions import InvalidQrCodeType


class QRCodesClient(object):
    STATIC = 'STATIC'
    DYNAMIC = 'DYNAMIC'

    def __init__(self, client):
        """
        QRCodes Client
        :param client:
        """
        self.client = client

    def get_url(self):
        return '/qr_codes'

    def create(self, type, external_id, callback_url, amount):
        """
        Create QRIS QR Code for payment
        :param type:
        :param external_id:
        :param callback_url:
        :param amount:
        :return:
        """
        type = type if type.isupper() else type.upper()
        if type not in [QRCodesClient.STATIC, QRCodesClient.DYNAMIC]:
            raise InvalidQrCodeType('The QR Code type must be one of'
                                    ' DYNAMIC or STATIC')

        url = self.get_url()
        params = {
            'type': type,
            'external_id': external_id,
            'callback_url': callback_url,
            'amount': amount,
        }
        return self.client.send_request('post', url, params)

    def get_payment_detail(self, external_id):
        """
        Get QRCodes Object by External ID

        :param external_id:
        :return:
        """
        url = '{base_url}/{external_id}'.format(
            base_url=self.get_url(),
            external_id=external_id
        )
        return self.client.send_request('get', url)

