import requests
from datetime import datetime
import csv


class ScheduledCheckerException(BaseException):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


def check_accessibility(url):
    try:
        response = requests.head(url, timeout=5.0, allow_redirects=True)

        """
        except requests.TooManyRedirects:
            raise ScheduledCheckerException('Sorry, too many redirects')
    
        # На момент написания кода я пока не до конца понимаю,
        # должна ли функция идти по редиректам, или же,
        # получив первый код 3**, она должна сообщать, что ресурс недоступен.
        # Поэтому возможность обработки такого исключения предусмотрена, 
        # но не реализована.
        # Еще интерпретатор ругается, что он ожидал блок except или finally,
        # а не вот это все, поэтому после раскомментирования нужно подвинуть
        # первый блок except на четыре пробела влево
        """
    except requests.Timeout:
        raise ScheduledCheckerException('Timeout error. Try again later.')
    except requests.ConnectionError:
        raise ScheduledCheckerException('Connection is lost, try again later.')
    else:
        return response.status_code == 200


def write_check_results(url_list):
    headers_template = ['Date and time', 'URL', 'Check result']
    url_status = {True: 'This site is OK', False: 'Resource is unavailable'}
    with open(r'check_result.txt', 'a') as result:
        wrighter = csv.writer(result, delimiter=';')
        wrighter.writerow(headers_template)
        for url in url_list:
            string_template = [datetime.now(), url,
                               url_status[check_accessibility(url)]]
            wrighter.writerow(string_template)
