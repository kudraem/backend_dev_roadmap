from todo.dummy_todo import Todo, DummyJsonException, DummyJsonApi
import pytest


def test_todo():
    new = Todo('https://dummyjson.com/todos')
    response = new.enlist({'limit': 10, 'skip': 0})
    assert response[1]['id'] == 2
    response = new.enlist({'limit': 10, 'skip': 5})
    assert response[6]['id'] == 12
    response = new.id(5)
    assert response['todo'] == "Solve a Rubik's cube"
    response = new.random()
    assert response['id'] > 0
    response = new.user(5, {'limit': 10, 'skip': 0})
    assert response[0]['userId'] == 5
    response = new.add('Send another request to dummyjson.com', 31, False)
    assert response['id'] == 151
    response = new.update(1, False)
    assert response['completed'] is False
    response = new.remove(1)
    assert response['isDeleted'] is True
    print('Tests for Todo passed')


def test_raise_http_exception():
    with pytest.raises(DummyJsonException) as err:
        new = Todo('https://www.google.com/images/branding/googlelogo/1x/')
        new.id(1000)
    assert str(err.value) == ('HTTPError is occured, '
                              'and it is 404 Client Error: '
                              'Not Found for url: https://www.google.com/images/branding/googlelogo/1x/1000')
    print('Test passed, HTTP error is occured')


'''
def test_max_redirects():
    with pytest.raises(DummyJsonException) as err:
        new = DummyJsonApi('https://2866-79-101-225-134.ngrok-free.app/redirect_error')
        new.get()
    assert str(err.value) == 'Sorry, too many redirects'


def test_timeout():
    with pytest.raises(DummyJsonException) as err:
        new = DummyJsonApi('https://2866-79-101-225-134.ngrok-free.app/timeout_error')
        new.get()
    assert str(err.value) == 'Timeout error. Try again later.'
'''


def test_json_parse():
    with pytest.raises(DummyJsonException) as err:
        new = DummyJsonApi('https://google.com')
        new.get()
    print(err.value)


def test_connection():
    with pytest.raises(DummyJsonException) as err:
        new = Todo('https://gooogle.com/404')
        new.enlist({})
    assert str(err.value) == 'Connection is lost, try again later.'
    print('Tests passed. Connection exception is caught')
