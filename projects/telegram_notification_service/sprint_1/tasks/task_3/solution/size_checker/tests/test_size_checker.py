import pytest
from size_checker.request_check_size import check_size, SizeCheckerException, size_converter


def test_size_checker():
    assert check_size('https://api.github.com/') == 510
    assert check_size('https://dummyjson.com/todos') == 2471
    assert check_size('https://httpbin.org/get') == 308
    print('It\'s ok, boss')


def test_size_converter():
    assert size_converter(1048576) == '1.0 MiB'
    assert size_converter(1024) == '1.0 KiB'
    assert size_converter(512) == '512 B'
    assert size_converter(1208925819614629174706176) == '1.0 YiB'
    assert size_converter(0) == '0 B'
    response_size = check_size('https://api.github.com/')
    assert size_converter(response_size) == '510 B'
    response_size = check_size('https://dummyjson.com/todos')
    assert size_converter(response_size) == '2.4 KiB'
    response_size = check_size('https://httpbin.org/get')
    assert size_converter(response_size) == '308 B'
    print('Sizes converted')


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


def test_max_redirects():
    with pytest.raises(SizeCheckerException) as err:
        check_size('https://2866-79-101-225-134.ngrok-free.app/redirect_error')
    assert str(err.value) == 'Sorry, too many redirects'
