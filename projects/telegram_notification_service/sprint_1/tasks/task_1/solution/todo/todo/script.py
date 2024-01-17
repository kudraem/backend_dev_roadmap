import requests


class DummyJsonException(BaseException):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return self.message


def catch_exception(method, path, **kwargs):
    try:
        response = requests.request(method, path, **kwargs)
        response.raise_for_status()
    except requests.TooManyRedirects:
        raise DummyJsonException('Sorry, too many redirects')
    except requests.HTTPError as err:
        raise DummyJsonException(f'HTTPError is occured, and it is {err}')
    except requests.Timeout:
        raise DummyJsonException('Timeout error. Try again later.')
    except requests.ConnectionError:
        raise DummyJsonException('Connection is lost, try again later.')
    else:
        try:
            return response.json()
        except requests.JSONDecodeError:
            raise DummyJsonException('Incoming JSON is invalid')


class DummyJsonApi(requests.Session):
    def __init__(self, domain):
        super().__init__()
        self.max_redirects = 5
        self.domain = domain
        self.headers = {'User-Agent': 'Python-Study-App/1.0.0',
                        'Content-Type': 'application/json'}

    def get(self, path='/', delimiter=None, skip=None):
        params = {'limit': delimiter, 'skip': skip}
        return catch_exception('get', (self.domain + path),
                               params=params,
                               headers=self.headers)

    def post(self, request_body, path='/'):
        return catch_exception('post', (self.domain + path),
                               json=request_body,
                               headers=self.headers)

    def patch(self, request_body, path='/'):
        return catch_exception('patch', (self.domain + path),
                               json=request_body,
                               headers=self.headers)

    def delete(self, path='/'):
        return catch_exception('delete', (self.domain + path),
                               headers=self.headers)


class Todo:
    def __init__(self):
        self.dummyjson = DummyJsonApi('https://dummyjson.com/todos')

    def enlist(self, delimiter=5, skip=0):
        """
        list(self, delimiter=5, skip=0)

        Метод позволяет пропустить skip элементов в списке дел
        и получить следующие delimiter дел.
        Значение skip по-умолчанию - 0.
        Значение delimiter по-умолчанию - 5.
        """
        todoes_dict = self.dummyjson.get(delimiter=delimiter, skip=skip)
        return todoes_dict.get('todos')

    def id(self, event_id):
        """
        id(self, event_id)

        Метод позволяет получить из списка конкретное дело
        с заданным пользователем event_id.
        """
        path = f'/{event_id}'
        return self.dummyjson.get(path=path)

    def random(self):
        """
        random(self)

        Метод позволяет получить произвольное дело из списка
        """
        path = '/random'
        return self.dummyjson.get(path=path)

    def user(self, user_id, delimiter=0, skip=0):
        """
        user(self, user_id, delimiter=0, skip=0)

        Метод позволяет получить список дел конкретного пользователя
        по его user_id.
        Метод позволяет также выводить ограниченное количество дел
        (параметр delimiter), а также пропускать первые skip дел
        пользователя
        """
        path = f'/user/{user_id}'
        todoes_dict = self.dummyjson.get(path=path,
                                         delimiter=delimiter, skip=skip)
        return todoes_dict.get('todos')

    def add(self, event, user_id, status=False):
        """
        add(self, event, user_id, status=False)

        Метод позволяет добавить свое дело в общий список.
        В качестве входных параметров требует:
        1) event - текстовое описание самого дела;
        2) status - статус завершенности:
                    (True - завершено, False - не завершено);
        3) user_id - ID пользователя
        Значение status по умолчанию: False
        """
        path = '/add'
        request_body = {
            'todo': event,
            'completed': status,
            'userId': user_id
        }
        return self.dummyjson.post(path=path, request_body=request_body)

    def update(self, task_id, status=True):
        """
        update(self, task_id, status=True)

        Метод позволяет обновить статус дела по его id.
        В качестве входных параметров требует:
        1) task_id - id дела
        2) status - статус завершенности дела (по-умолчанию - True)
        """
        path = f'/{task_id}'
        request_body = {
            'completed': status,
        }
        return self.dummyjson.patch(path=path, request_body=request_body)

    def remove(self, task_id):
        """
        remove(self, task_id)

        Метод позволяет удалить дело по его task_id
        """
        path = f'/{task_id}'
        return self.dummyjson.delete(path=path)
