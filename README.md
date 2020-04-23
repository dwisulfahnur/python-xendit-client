# Python Xendit Clinet API

[![Build Status](https://travis-ci.com/dwisulfahnur/python-xendit-client.svg?branch=master)](https://travis-ci.com/dwisulfahnur/python-xendit-client)
[![PyPI version](https://badge.fury.io/py/xenditclient.svg)](https://badge.fury.io/py/xenditclient)
[![Downloads](https://pepy.tech/badge/xenditclient/month)](https://pepy.tech/project/xenditclient)
[![Downloads](https://pepy.tech/badge/xenditclient)](https://pepy.tech/project/xenditclient)

Xendit REST API Client for Python

## Documentation


## Install
Install xenditclient with pip by the following command:
```sh
pip install xenditclient
```

## Usage
Configure the XenditClient with the secret key that you can obtained on your Xendit Dashboard Account.
```python
from xenditclient import XenditClient

client = XenditClient(api_key='<your-secret-key>')
```
### Get Balance
```python
res_dict = client.balance.get_balance('CASH')
print(res_dict)
# {
#   'balance': 1000137690
# }
```

### EWallets
#### Create Payment

```python
params = {
  'ewallet_type':'OVO',
  'external_id':'21345',
  'amount':10000,
  'phone':'081234567890'
}

res_dict = client.ewallet.create(params)
print(res_dict)
# {
#   "business_id": "12345678",
#   "external_id": "21345",
#   "amount": "10000",
#   "phone": "081234567890",
#   "ewallet_type": "OVO",
#   "status": "PENDING",
#   "created": "2020-04-04T00:00:00.000Z",
# }
```
#### Get Payment Status

```python
res_dict = client.ewallet.get_payment_status(external_id='21345', payment_method='OVO')
print(res_dict)
# {
#   "amount": "10000",
#   "business_id": "12345678",
#   "ewallet_type": "OVO",
#   "external_id": "21345",
#   "status": "COMPLETED",
#   "transaction_date": "2020-04-04T11:48:47.903Z"
# }
```

## Legal 
Disclaimer: This library is not affliated with Xendit. This is an independent and unofficial Library.
