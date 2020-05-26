# -*- coding: utf-8 -*-
import requests

from .exceptions import (AuthError, AccountBlocked, LoginRequired,
                         PasswordRequired, LowLevelError)


class Client():
    def __init__(self, login=None, password=None, server=None):
        self.login = login
        self.password = password
        self.server = server or 'https://3wifi.stascorp.com'

        self.http = requests.Session()

    def auth(self):
        if not self.login:
            raise LoginRequired('Login is required to login')
        if not self.password:
            raise PasswordRequired('Password is required to login')

        r = self.http.post(
            f'{self.server}/user.php?a=login',
            data={
                'login': self.login,
                'password': self.password
            }
        ).json()

        if r['result']:
            return True
        else:
            if 'error' in r:
                if r['error'] == 'loginfail':
                    raise AuthError('Invalid login or password')
                elif r['error'] == 'lowlevel':
                    raise AccountBlocked('The account is blocked')
                else:
                    raise AuthError(r['error'])
            else:
                raise AuthError()

    def logout(self):
        r = self.http.get(f'{self.server}/user.php?a=token').json()
        if r['result']:
            token = r['token']
            r = self.http.get(
                f'{self.server}/user.php?a=logout&token={token}'
            ).json()
            return r['result']
        else:
            return False

    def request(self, action, data={}):
        r = self.http.post(
            f'{self.server}/3wifi.php?a={action}',
            data=data
        ).json()
        if r['result']:
            return r
        elif 'error' in r:
            error = r['error']
            if error == 'unauthorized':
                self.auth()
                return self.request(action, data)
            elif error == 'lowlevel':
                raise LowLevelError('You don\'t have access to this action')
