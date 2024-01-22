import requests


class SizeCheckerException(BaseException):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


def size_converter(num):
    prefixes = ['B', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']
    recursive_counter = 0

    def calculate_size(content_length):
        nonlocal recursive_counter
        bytes = content_length
        if bytes < 1024:
            return bytes
        else:
            recursive_counter += 1
            return calculate_size(bytes / 1024)

    size = round(calculate_size(num), 1)
    if recursive_counter == 0:
        size = int(size)
    return f'{size} {prefixes[recursive_counter]}'


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
        response_size = float(response.headers.get('Content-Length'))
        return size_converter(response_size)


print(check_size('https://46af-79-101-225-134.ngrok-free.app/timeout_error'))