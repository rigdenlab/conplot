class SessionTimeOut(Exception):
    pass


class InvalidFormat(Exception):
    pass


class UserExists(Exception):
    pass


class UserDoesntExist(Exception):
    pass


class EmailAlreadyUsed(Exception):
    pass


class SQLInjectionAlert(Exception):
    pass


class IntegrityError(Exception):
    pass
