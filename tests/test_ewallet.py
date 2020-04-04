from .context import XenditClient, EwalletClient


def test_ewallet_class():
    xendit_client = XenditClient(api_key='apikey')
    ewallet = EwalletClient(xendit_client)

    assert ewallet
    assert isinstance(ewallet, EwalletClient)
    assert isinstance(ewallet.client, XenditClient)


def test_ewallet_from_xendit_client():
    xendit_client = XenditClient(api_key='apikey')

    assert hasattr(xendit_client, 'ewallet')
    assert isinstance(xendit_client.ewallet, EwalletClient)
    assert isinstance(xendit_client.ewallet.client, XenditClient)


def test_ewallet_client():
    xendit_client = XenditClient(api_key='apikey')
    ewallet = EwalletClient(xendit_client)

    assert hasattr(ewallet, 'get_url')
    assert hasattr(ewallet, 'create')
    assert hasattr(ewallet, 'get_payment_status')


def test_create_wrong_ewallet_type():
    xendit_client = XenditClient(api_key='')
    try:
        xendit_client.ewallet.create(params={
            'ewallet_type': 'gopay'
        })
    except Exception as e:
        err = e

    assert err.__class__.__name__ == 'InvalidArgumentException'
