from .context import XenditClient


def test_xenditclient_class():
    client = XenditClient(api_key='myapikey')
    assert client.api_key == 'myapikey'


def test_validate_params_method():
    client = XenditClient(api_key='myapikey')
    assert getattr(client, 'validate_params')


def test_send_request_method():
    client = XenditClient(api_key='myapikey')
    assert getattr(client, 'send_request', False)
