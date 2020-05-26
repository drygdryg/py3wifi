# -*- coding: utf-8 -*-
import requests

from .exceptions import (ApiError, AuthError, AccountBlocked,
                         LoginRequired, PasswordRequired, NoKeysReceived)


class Api():
    def __init__(self, login=None, password=None, read_key=None, server=None):
        self.login = login
        self.password = password
        self.key = read_key
        self.server = server or 'https://3wifi.stascorp.com'

        self.http = requests.Session()

    def auth(self):
        if not self.login:
            raise LoginRequired('Login is required to login')
        if not self.password:
            raise PasswordRequired('Password is required to login')

        r = self.http.post(
            f'{self.server}/api/apikeys',
            data={
                'login': self.login,
                'password': self.password,
                'genread': True
            }
        ).json()

        if r['result']:
            try:
                self.key = list(filter(lambda x: x['access'] == 'read', r['data']))[0]['key']
            except IndexError:
                raise NoKeysReceived('No read API key received')
        else:
            if r['error'] == 'loginfail':
                raise AuthError('Invalid login or password')
            elif r['error'] == 'lowlevel':
                raise AccountBlocked('The account is blocked')
            else:
                raise ApiError(r['error'])

    def method(self, method, params=None):
        if (not self.key) and (method in ('apiquery', 'apiwps', 'apiranges')):
            raise ApiError('This method requires authorization')

        params = params.copy() if params else {}

        if 'key' not in params:
            params['key'] = self.key

        response = self.http.post(
            f'{self.server}/api/' + method,
            json=params
        ).json()

        if response['result']:
            return response['data']
        elif 'error' in response:
            if response['error'] == 'form':
                raise ApiError('Some form fields are incorrect')
            else:
                raise ApiError(response['error'])
        else:
            raise ApiError()

    def get_api(self):
        return ApiMethod(self)


class ApiMethod():
    def __init__(self, api, method=None):
        self._api = api
        self._method = method

    def __getattr__(self, method):
        if '_' in method:
            m = method.split('_')
            method = m[0] + ''.join(i.title() for i in m[1:])

        return ApiMethod(
            self._api,
            (self._method + '.' if self._method else '') + method
        )

    def __call__(self, **kwargs):
        return self._api.method(self._method, kwargs)
