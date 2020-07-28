from .context import XenditClient, QRCodesClient


def test_qrcode_class():
    xendit_client = XenditClient(api_key='apikey')
    qrcode = QRCodesClient(xendit_client)

    assert qrcode
    assert isinstance(qrcode, QRCodesClient)
    assert isinstance(qrcode.client, XenditClient)


def test_qrcode_from_xendit_client():
    xendit_client = XenditClient(api_key='apikey')

    assert hasattr(xendit_client, 'qrcode')
    assert isinstance(xendit_client.qrcode, QRCodesClient)
    assert isinstance(xendit_client.qrcode.client, XenditClient)


def test_qrcode_client():
    xendit_client = XenditClient(api_key='apikey')
    qrcode = QRCodesClient(xendit_client)

    assert hasattr(qrcode, 'get_url')
    assert hasattr(qrcode, 'create')
    assert hasattr(qrcode, 'get_payment_detail')


def test_create_wrong_qrcode_type():
    xendit_client = XenditClient(api_key='')
    try:
        xendit_client.qrcode.create('nottype', 'INV1', 'http://callbackurl', 10000)
    except Exception as e:
        err = e

    assert err.__class__.__name__ == 'InvalidQrCodeType'
