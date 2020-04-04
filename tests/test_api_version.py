from .context import XenditClient


def test_set_api_version_not():
    xendit_client = XenditClient(api_key='')

    assert not xendit_client.api_version


def test_update_api_version():
    xendit_client = XenditClient(api_key='')
    api_version = '2020-02-01'
    xendit_client.set_api_version(api_version)

    assert xendit_client.api_version == api_version
