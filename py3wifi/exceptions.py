# -*- coding: utf-8 -*-
class ApiError(Exception):
    pass


class ClientError(Exception):
    pass


class AuthError(ApiError, ClientError):
    pass


class AccountBlocked(AuthError, ClientError):
    pass


class LoginRequired(AuthError, ClientError):
    pass


class PasswordRequired(AuthError, ClientError):
    pass


class NoKeysReceived(AuthError):
    pass


class LowLevelError(ClientError):
    pass
