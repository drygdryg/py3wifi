# -*- coding: utf-8 -*-
class ApiError(Exception):
    pass

class AuthError(ApiError):
    pass

class AccountBlocked(AuthError):
    pass

class LoginRequired(AuthError):
    pass

class PasswordRequired(AuthError):
    pass

class NoKeysReceived(AuthError):
    pass
