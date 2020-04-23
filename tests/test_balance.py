from .context import XenditClient, BalanceClient


def test_balance_class():
    xendit_client = XenditClient(api_key='apikey')
    balance = BalanceClient(xendit_client)

    assert balance
    assert isinstance(balance, BalanceClient)
    assert isinstance(balance.client, XenditClient)


def test_balance_from_xendit_client():
    xendit_client = XenditClient(api_key='apikey')

    assert hasattr(xendit_client, 'balance')
    assert isinstance(xendit_client.balance, BalanceClient)
    assert isinstance(xendit_client.balance.client, XenditClient)


def test_balance_client():
    xendit_client = XenditClient(api_key='apikey')
    balance = BalanceClient(xendit_client)

    assert hasattr(balance, 'account_types')
    assert hasattr(balance, 'validate_account_type')
    assert hasattr(balance, 'get_balance')


def test_create_wrong_account_type():
    xendit_client = XenditClient(api_key='')
    try:
        xendit_client.balance.get_balance('wrong_account_type')
    except Exception as e:
        err = e

    assert err.__class__.__name__ == 'InvalidAccountType'
