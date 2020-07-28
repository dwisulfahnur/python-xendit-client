# Python Xendit Client API

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

### QR Codes (QRIS)
Get QRCode client
```python
qrcode = client.qrcodes
# or
from xenditclient.qrcodes import QRCodesClient

qrcode = QRCodesClient(client)
```

Create QRCode for payment
```python
data = qrcode.create("DYNAMIC", "DS-INV-01", "https://dwisulfahnur.com/api/xendit/callback", 10200)
print(data)
# {
#   "id": "qr_a706814a-d18b-4109-9b71-7a76f9855e123",
#   "external_id": "DS-INV-01",
#   "amount": 10200,
#   "qr_string": "00022312321226660014ID.LINKAJA.WWW0118912312300241148000215200423041141230303UME51450015ID.OR.GPNQR.WWW0215000111111111110303UME520454995802ID5920Placeholder merchant6007Jakarta6106123456623801152QiFZi5qT12307152QiFZi5qThdA4M753033605405102006304D9CM",
#   "callback_url": "https://dwisulfahnur.com/api/xendit/callback",
#   "type": "DYNAMIC",
#   "status": "ACTIVE",
#   "created": "2020-07-27T07:44:31.420Z",
#   "updated": "2020-07-27T07:44:31.420Z"
# }
```

Get QRCode detail payment
```python
data = qrcode.get_payment_detail("DS-INV-01")
print(data)
# {
#   "id": "qr_a706814a-d18b-4109-9b71-7a76f9855e123",
#   "external_id": "DS-INV-01",
#   "amount": 10200,
#   "qr_string": "00022312321226660014ID.LINKAJA.WWW0118912312300241148000215200423041141230303UME51450015ID.OR.GPNQR.WWW0215000111111111110303UME520454995802ID5920Placeholder merchant6007Jakarta6106123456623801152QiFZi5qT12307152QiFZi5qThdA4M753033605405102006304D9CM",
#   "callback_url": "https://dwisulfahnur.com/api/xendit/callback",
#   "type": "DYNAMIC",
#   "status": "ACTIVE",
#   "created": "2020-07-27T07:44:31.420Z",
#   "updated": "2020-07-27T07:44:31.420Z"
# }
```
## Legal 
Disclaimer: This library is not affliated with Xendit. This is an independent and unofficial Library.
