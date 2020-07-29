from .context import XenditClient, VirtualAccountClient


def test_virtual_account_class():
    xendit_client = XenditClient(api_key='apikey')
    va = VirtualAccountClient(xendit_client)

    assert va
    assert isinstance(va, VirtualAccountClient)
    assert isinstance(va.client, XenditClient)


def test_va_from_xendit_client():
    xendit_client = XenditClient(api_key='apikey')

    assert hasattr(xendit_client, 'virtual_account')
    assert isinstance(xendit_client.virtual_account, VirtualAccountClient)
    assert isinstance(xendit_client.virtual_account.client, XenditClient)


def test_xendit_client():
    xendit_client = XenditClient(api_key='apikey')
    va = VirtualAccountClient(xendit_client)

    assert hasattr(va, 'get_url')
    assert hasattr(va, 'create')
    assert hasattr(va, 'get_payment_detail')
    assert hasattr(va, 'update_payment_detail')
    assert hasattr(va, 'get_va_banks')


def test_create_va_wrong_bank_code():
    xendit_client = XenditClient(api_key='')
    try:
        xendit_client.virtual_account.create(
            '1234',
            'wrongbankcode',
            'Dwi Sulfahnur'
        )
    except Exception as  e:
        err = e

    assert err.__class__.__name__ == 'InvalidArgumentException'
