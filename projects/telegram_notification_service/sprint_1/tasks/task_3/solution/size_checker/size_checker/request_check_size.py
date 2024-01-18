import requests


class SizeCheckerException(BaseException):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


def check_size(url):
    def size_converter(num):
        if num >= 1048576:
            size = round((num / 1048576), 1)
            if size % 10 == 0:
                return f'{int(size)} MiB'
            return f'{size} MiB'
        elif num >= 1024:
            size = round((num / 1024), 1)
            if size % 10 == 0:
                return f'{int(size)} KiB'
            return f'{size} KiB'
        else:
            return f'{int(num)} B'

    try:
        response = requests.head(url, timeout=5.0)
    except requests.TooManyRedirects:
        raise SizeCheckerException('Sorry, too many redirects')
    except requests.Timeout:
        raise SizeCheckerException('Timeout error. Try again later.')
    except requests.ConnectionError:
        raise SizeCheckerException('Connection is lost, try again later.')
    else:
        response_size = float(response.headers.get('Content-Length'))
        return size_converter(response_size)
