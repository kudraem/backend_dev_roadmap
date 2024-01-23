import scheduled_checks.scheduled_checks as s_c
import pytest


def test_check_accessibility():
    assert s_c.check_accessibility('https://api.github.com/') is True
    assert s_c.check_accessibility('https://dummyjson.com/todos') is True
    assert s_c.check_accessibility('https://dummyjson.com/todoss') is False
    assert s_c.check_accessibility('https://httpbin.org/get') is True
    assert s_c.check_accessibility('https://httpbin.org/post') is False
    print('Tests passed. Accessibility checked')


def test_read_check_results():
    url_list = s_c.get_url_list_from_file('../url_list')
    check_result = s_c.check_urls(url_list)
    assert check_result[0][1] == 'https://api.github.com/'
    assert check_result[0][2] is True
    assert check_result[2][1] == 'https://dummyjson.com/todoss'
    assert check_result[2][2] is False
    print('Tests passed. Check\'s results are collected')


def test_write_read_results():
    url_list = s_c.get_url_list_from_file('../url_list')
    check_result = s_c.check_urls(url_list)
    s_c.write_check_results_to_file(check_result)
    read_from_file = s_c.read_check_results_from_file('check_result.csv')
    assert read_from_file[1][1] == 'https://dummyjson.com/todos'
    assert read_from_file[1][2] == 'This site is OK'
    assert read_from_file[5][1] == 'https://gooogle.com/404'
    assert read_from_file[5][2] == 'Resource is unavailable'
    print('Tests passed. Check\'s results are wrote to file and read from it')


# Тест готов работать, когда будет получен адрес сервера с редиректами
"""
def test_max_redirects():
    with pytest.raises(s_c.ScheduledCheckerException) as err:
        s_c.check_accessibility(
            'https://2866-79-101-225-134.ngrok-free.app/redirect_error')
    assert str(err.value) == 'Sorry, too many redirects'
"""

# Timeout тест не работает, поскольку сервер возвращает 404
"""
def test_timeout():
    with pytest.raises(ScheduledCheckerException) as err:
        s_c.check_accessibility(
        'https://2866-79-101-225-134.ngrok-free.app/timeout_error')
    assert str(err.value) == 'Timeout error. Try again later.'
"""


def test_connection():
    with pytest.raises(s_c.ScheduledCheckerException) as err:
        s_c.check_accessibility('https://gooogle.com/404')
    assert str(err.value) == 'Connection is lost, try again later.'
    print('Tests passed. Connection exception is caught')
