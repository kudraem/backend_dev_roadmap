import pytest
from size_checker.request_check_size import check_size, SizeCheckerException


def test_size_checker():
    assert check_size('https://api.github.com/') == '510 B'
    assert check_size('https://dummyjson.com/todos') == '2.4 KiB'
    assert check_size('https://httpbin.org/get') == '308 B'
    print('It\'s ok, boss')


def test_timeout():
    with pytest.raises(SizeCheckerException) as err:
        check_size('https://46af-79-101-225-134.ngrok-free.app/timeout_error')
    assert str(err.value) == 'Timeout error. Try again later.'


def test_connection():
    with pytest.raises(SizeCheckerException) as err:
        check_size('https://gooogle.com/404')
    assert str(err.value) == 'Connection is lost, try again later.'


def test_empty_response():
    with pytest.raises(SizeCheckerException) as err:
        check_size('https://46af-79-101-225-134.ngrok-free.app/timeout_error')
    assert str(err.value) == 'Request is successful, but response is empty'
