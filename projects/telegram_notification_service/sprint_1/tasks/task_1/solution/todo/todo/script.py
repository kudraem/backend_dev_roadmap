import requests


def catch_exception(request):
    try:
        response = request
        response.raise_for_status()
    except requests.TooManyRedirects:
        raise Exception('Sorry, too many redirects')
    except requests.HTTPError as err:
        raise Exception(f'HTTPError is occured, and it is {err}')
    except requests.Timeout:
        raise Exception('Timeout error. Try again later.')
    except requests.ConnectionError:
        raise Exception('Connection is lost, try again later.')
    else:
        try:
            return response.json()
        except requests.JSONDecodeError:
            raise Exception('Incoming JSON is invalid')


class DummyJsonApi(requests.Session):
    def __init__(self, domain):
        super().__init__()
        self.max_redirects = 5
        self.domain = domain
        self.headers = {'User-Agent': 'Python-Study-App/1.0.0',
                        'Content-Type': 'application/json'}

    def get(self, path='/', delimiter=None, step=None):
        params = {'limit': delimiter, 'skip': step}
        return catch_exception(super().get(self.domain + path,
                                           params=params,
                                           headers=self.headers))

    def post(self, request_body, path='/'):
        return catch_exception(super().post(self.domain + path,
                                            json=request_body,
                                            headers=self.headers))

    def patch(self, request_body, path='/'):
        return catch_exception(super().patch(self.domain + path,
                                             json=request_body,
                                             headers=self.headers))

    def delete(self, path='/'):
        return catch_exception(super().delete(self.domain + path,
                                              headers=self.headers))


class Todo:
    def __init__(self):
        self.dummyjson = DummyJsonApi('https://dummyjson.com/todos')

    def enlist(self, delimiter=5, step=0):
        """
        list(self, delimiter=5, step=0)

        Метод позволяет пропустить step элементов в списке дел
        и получить следующие delimiter дел.
        Значение step по-умолчанию - 0.
        Значение delimiter по-умолчанию - 5.
        """
        todoes_dict = self.dummyjson.get(delimiter=delimiter, step=step)
        return todoes_dict.get('todos')

    def id(self, event_id):
        """
        id(self, event_id)

        Метод позволяет получить из списка конкретное дело
        с заданным пользователем event_id.
        """
        path = f'/{event_id}'
        return self.dummyjson.get(path=path)


new = Todo()
response = new.enlist(10)
assert response[1]['id'] == 2
response = new.enlist(10, 5)
assert response[6]['id'] == 12
response = new.id(5)
assert response['todo'] == "Solve a Rubik's cube"
print('Tests passed')
