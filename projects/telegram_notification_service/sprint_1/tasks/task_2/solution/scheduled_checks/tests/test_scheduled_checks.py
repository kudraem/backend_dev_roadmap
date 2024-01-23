from scheduled_checks.scheduled_checks import (
    check_accessibility, ScheduledCheckerException, write_check_results)
import pytest
import csv


def test_check_accessibility():
    assert check_accessibility('https://api.github.com/') is True
    assert check_accessibility('https://dummyjson.com/todos') is True
    assert check_accessibility('https://dummyjson.com/todoss') is False
    assert check_accessibility('https://httpbin.org/get') is True
    assert check_accessibility('https://httpbin.org/post') is False
    print('Tests passed. Accessibility checked')


test_list = ['https://api.github.com/', 'https://dummyjson.com/todos',
             'https://dummyjson.com/todoss', 'https://httpbin.org/get',
             'https://httpbin.org/post']


def test_write_check_results():
    test_file_result = []
    write_check_results(test_list)
    with open(r'check_result.txt', 'r') as result:
        reader = csv.reader(result, delimiter=';')
        for row in reader:
            test_file_result.append(row)
    assert test_file_result[1][1] == 'https://api.github.com/'
    assert test_file_result[1][2] == 'This site is OK'
    assert test_file_result[3][1] == 'https://dummyjson.com/todoss'
    assert test_file_result[3][2] == 'Resource is unavailable'
    print('Tests passed. Check\'s results are wrote to file')


"""
def test_max_redirects():
    with pytest.raises(ScheduledCheckerException) as err:
        check_accessibility('https://2866-79-101-225-134.ngrok-free.app/redirect_error')
    assert str(err.value) == 'Sorry, too many redirects'

# На момент написания кода я пока не до конца понимаю,
# должна ли функция идти по редиректам, или же,
# получив первый код 3**, она должна сообщать, что ресурс недоступен.
# Поэтому тест есть, но не задействован.
"""

# Timeout тест не работает, поскольку сервер возвращает 404
"""
def test_timeout():
    with pytest.raises(ScheduledCheckerException) as err:
        check_accessibility('https://2866-79-101-225-134.ngrok-free.app/timeout_error')
    assert str(err.value) == 'Timeout error. Try again later.'
"""


def test_connection():
    with pytest.raises(ScheduledCheckerException) as err:
        check_accessibility('https://gooogle.com/404')
    assert str(err.value) == 'Connection is lost, try again later.'
    print('Tests passed. Connection exception is caught')
