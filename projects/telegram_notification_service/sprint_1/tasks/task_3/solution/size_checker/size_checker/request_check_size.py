import requests


class SizeCheckerException(BaseException):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


def size_converter(num):
    suffixes = ['B', 'KiB', 'MiB', 'GiB', 'TiB',
                'PiB', 'EiB', 'ZiB', 'YiB']
    # recursive_counter = 0
    # В варианте функции без рекурсии этой переменной,
    # пожалуй, здесь не место

    """
    Оставим это для потомков
    ~~~~~~~~~~~~~~~~~~~~~~~~
    
    def calculate_size(content_length):
        nonlocal recursive_counter
        bytes = content_length
        if bytes < 1024:
            return bytes
        else:
            recursive_counter += 1
            return calculate_size(bytes / 1024)
            
    size = round(calculate_size(num), 1)
    return f'{size} {suffixes[recursive_counter]}'
    """

    def calculate_size(content_length):
        suffix_index = 0
        result_size = content_length
        while result_size >= 1024:
            result_size /= 1024
            suffix_index += 1
        return result_size, suffix_index

    calculation_results = calculate_size(num)
    size = round(calculation_results[0], 1)
    return f'{size} {suffixes[calculation_results[1]]}'


def check_size(url):
    try:
        response = requests.head(url, timeout=5.0, allow_redirects=True)
    except requests.TooManyRedirects:
        raise SizeCheckerException('Sorry, too many redirects')
    except requests.Timeout:
        raise SizeCheckerException('Timeout error. Try again later.')
    except requests.ConnectionError:
        raise SizeCheckerException('Connection is lost, try again later.')
    else:
        try:
            return int(response.headers['Content-Length'])
        except KeyError:
            raise SizeCheckerException('Request is successful, '
                                       'but response is empty')
