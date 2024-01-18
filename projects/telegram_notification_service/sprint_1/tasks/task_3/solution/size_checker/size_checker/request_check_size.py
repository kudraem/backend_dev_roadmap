import requests


class SizeCheckerException(BaseException):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


def check_size(url):
    try:
        response = requests.head(url, timeout=5.0)
    except requests.TooManyRedirects:
        raise SizeCheckerException('Sorry, too many redirects')
    except requests.Timeout:
        raise SizeCheckerException('Timeout error. Try again later.')
    except requests.ConnectionError:
        raise SizeCheckerException('Connection is lost, try again later.')
    else:
        return response.headers.get('Content-Length')
