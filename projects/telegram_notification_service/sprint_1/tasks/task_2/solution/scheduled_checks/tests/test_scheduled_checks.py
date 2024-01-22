from scheduled_checks.scheduled_checks import (
    check_accessibility, ScheduledCheckerException)
import pytest


def test_check_accessibility():
    assert check_accessibility('https://api.github.com/') is True
    assert check_accessibility('https://dummyjson.com/todos') is True
    assert check_accessibility('https://dummyjson.com/todoss') is False
    assert check_accessibility('https://httpbin.org/get') is True
    assert check_accessibility('https://httpbin.org/post') is False
    print('Tests passed. Accessibility checked')


"""
def test_max_redirects():
    with pytest.raises(ScheduledCheckerException) as err:
        check_accessibility('https://2866-79-101-225-134.ngrok-free.app/redirect_error')
    assert str(err.value) == 'Sorry, too many redirects'

# На момент написания кода я пока не до конца понимаю,
# должна ли функция идти по редиректам, или же,
# получив первый код 4**, она должна сообщать, что ресурс недоступен.
# Поэтому тест есть, но не задействован. 
"""


def test_timeout():
    with pytest.raises(ScheduledCheckerException) as err:
        check_accessibility('https://2866-79-101-225-134.ngrok-free.app/timeout_error')
    assert str(err.value) == 'Timeout error. Try again later.'


def test_connection():
    with pytest.raises(ScheduledCheckerException) as err:
        check_accessibility('https://gooogle.com/404')
    assert str(err.value) == 'Connection is lost, try again later.'


test_check_accessibility()
test_timeout()
test_connection()
# test_max_redirects()
