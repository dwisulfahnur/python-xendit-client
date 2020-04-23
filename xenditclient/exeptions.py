class JSONDecodeError(Exception):
    pass


class APIErrorException(Exception):
    error_code = 0

    def get_error_code(self):
        return self.error_code

    def __init__(self, message, code, error_code, response_dict):
        self.message = message
        self.code = code
        self.error_code = error_code
        self.response_dict = response_dict

    def __str__(self):
        return self.message


class InvalidArgumentException(Exception):
    pass


class InvalidAccountType(Exception):
    pass
