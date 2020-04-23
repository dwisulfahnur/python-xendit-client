import json

import requests

from .balance import BalanceClient
from .ewallets import EwalletClient
from .exeptions import APIErrorException, JSONDecodeError, InvalidArgumentException


class XenditClient(object):
    BASE_URL = 'https://api.xendit.co'

    def __init__(self, api_key, api_version=None):
        self.http_client = requests
        self.api_key = api_key
        self.api_version = api_version

    def set_api_key(self, api_key):
        self.api_key = api_key

    def set_api_version(self, api_version):
        self.api_version = api_version

    def get_api_version(self, api_version):
        return self.api_version

    def send_request(self, method, request_url, parameters=None):
        if isinstance(parameters, str):
            try:
                parameters = json.loads(parameters)
            except Exception as e:
                raise JSONDecodeError(
                    'fail to parse `parameters` string as JSON. '
                    'Use JSON string or Dict as `parameters`. with message: `{0}`'.format(
                        repr(e)))

        payload = json.dumps(parameters) if method != 'get' else parameters
        headers = {
            'content-type': 'application/json',
            'accept': 'application/json',
            'user-agent': 'xenditclient-python/0.0.1'
        }
        if self.api_version:
            headers['x-api-version'] = self.api_version

        response_object = self.http_client.request(
            method,
            self.BASE_URL + request_url,
            auth=requests.auth.HTTPBasicAuth(self.api_key, ''),
            data=payload if method != 'get' else None,
            params=payload if method == 'get' else None,
            headers=headers,
            allow_redirects=True
        )
        # catch response if the response body is not jsonable
        try:
            response_dict = response_object.json()
        except json.decoder.JSONDecodeError as e:
            raise JSONDecodeError(
                'Fail to decode API response as JSON, API response is not JSON: `{0}`. with message: `{1}`'.format(
                    response_object.text, repr(e)))

        # raise API error exception
        if response_object.status_code >= 300:
            raise APIErrorException(
                message='Xendit API is returning API error. Error code: {0}. HTTP status code: `{1}`. '
                        'API response: `{2}`'.format(response_dict['error_code'],
                                                     response_object.status_code,
                                                     response_object.text),
                code=response_object.status_code,
                error_code=response_dict['error_code'],
                response_dict=response_dict
            )

        return response_dict

    def validate_params(self, params, required_params):
        for key in required_params:
            if key not in params.keys():
                raise InvalidArgumentException('the params must be include \'{0}\' key'.format(key))

        if len([i for i in required_params if i not in required_params]) > 0:
            raise InvalidArgumentException('You must pass required parameters on your params.')

    @property
    def ewallet(self):
        return EwalletClient(client=self)

    @property
    def balance(self):
        return BalanceClient(client=self)
