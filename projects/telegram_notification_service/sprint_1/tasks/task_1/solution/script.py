import requests


class Todo(requests.Session):
    def __init__(self):
        super().__init__()
        self.max_redirects = 5
        self.url = 'https://dummyjson.com/todos'
        self.headers = {'User-Agent': 'Python-Study-App/1.0.0',
                        'Content-Type': 'application/json'}

    def get(self, url='https://dummyjson.com/todos',
            delimiter=None, step=None):
        params = {'limit': delimiter, 'skip': step}
        try:
            response = super().get(url, params=params,
                                   headers=self.headers)
            response.raise_for_status()
        except requests.TooManyRedirects:
            return 'Sorry, too many redirects'
        except requests.HTTPError as err:
            return f'HTTPError is occured, and it is {err}'
        except requests.Timeout:
            return 'Timeout error. Try again later.'
        except requests.ConnectionError:
            return 'Connection is lost, try again later.'
        else:
            try:
                return response.json()
            except requests.JSONDecodeError:
                return 'Incoming JSON is invalid'

    def post(self, url='https://dummyjson.com/todos',
             request_body={}):
        try:
            response = super().post(url, json=request_body,
                                    headers=self.headers)
            response.raise_for_status()
        except requests.TooManyRedirects:
            return 'Sorry, too many redirects'
        except requests.HTTPError as err:
            return f'HTTPError is occured, and it is {err}'
        except requests.Timeout:
            return 'Timeout error. Try again later.'
        except requests.ConnectionError:
            return 'Connection is lost, try again later.'
        else:
            try:
                return response.json()
            except requests.JSONDecodeError:
                return 'Incoming JSON is invalid'

    def patch(self, url='https://dummyjson.com/todos', request_body={}):
        try:
            response = super().patch(url, json=request_body,
                                     headers=self.headers)
            response.raise_for_status()
        except requests.TooManyRedirects:
            return 'Sorry, too many redirects'
        except requests.HTTPError as err:
            return f'HTTPError is occured, and it is {err}'
        except requests.Timeout:
            return 'Timeout error. Try again later.'
        except requests.ConnectionError:
            return 'Connection is lost, try again later.'
        else:
            try:
                return response.json()
            except requests.JSONDecodeError:
                return 'Incoming JSON is invalid'

    def delete(self, url='https://dummyjson.com/todos'):
        try:
            response = super().delete(url, headers=self.headers)
            response.raise_for_status()
        except requests.TooManyRedirects:
            return 'Sorry, too many redirects'
        except requests.HTTPError as err:
            return f'HTTPError is occured, and it is {err}'
        except requests.Timeout:
            return 'Timeout error. Try again later.'
        except requests.ConnectionError:
            return 'Connection is lost, try again later.'
        else:
            try:
                return response.json()
            except requests.JSONDecodeError:
                return 'Incoming JSON is invalid'

    def list(self, delimiter=5, step=0):
        """
        list(self, delimiter=5, step=0)

        Метод позволяет пропустить step элементов в списке дел
        и получить следующие delimiter дел.
        Значение step по-умолчанию равно 0.
        Значение delimiter по-умолчанию - 5.
        """
        return self.get(delimiter=delimiter, step=step)['todos']

    def id(self, event_id):
        """
        id(self, event_id)

        Метод позволяет получить из списка конкретное дело
        с заданным пользователем event_id.
        """
        return self.get(f'{self.url}/{event_id}')

    def random(self):
        """
        random(self)

        Метод позволяет получить произвольное дело из списка
        """
        return self.get(f'{self.url}/random')

    def user(self, user_id):
        """
        user(self, user_id, delimiter=0, step=0)

        Метод позволяет получить список дел конкретного пользователя
        по его user_id.
        Метод позволяет также выводить ограниченное количество дел
        (параметр delimiter), а также пропускать первые step дел
        пользователя
        """
        return self.get(f'{self.url}/user/{user_id}')['todos']

    def add(self, event='To do nothing', status=False, user_id=1):
        """
        add(self, event='To do nothing', status=False, user_id=1)

        Метод позволяет добавить свое дело в общий список.
        В качестве входных параметров требует:
        1) event - текстовое описание самого дела;
        2) status - статус завершенности:
                    (True - завершено, False - не завершено);
        3) user_id - ID пользователя
        Значения по умолчанию: 'To do nothing', False, 1.
        """
        url = 'https://dummyjson.com/todos/add'
        request_body = {
            'todo': event,
            'completed': status,
            'userId': user_id
        }
        return self.post(url, request_body)

    def update(self, task_id, status=True):
        """
        update(self, task_id, status=True)

        Метод позволяет обновить статус дела по его id.
        В качестве входных параметров требует:
        1) task_id - id дела
        2) status - статус завершенности дела (по-умолчанию - True)
        """
        url = f'https://dummyjson.com/todos/{task_id}'
        request_body = {
            'completed': status,
        }
        return self.patch(url, request_body)

    def remove(self, task_id):
        """
        remove(self, task_id)

        Метод позволяет удалить дело по его task_id
        """
        return self.delete(f'{self.url}/{task_id}')


new = Todo()
response = new.list(10)
assert response[1]['id'] == 2
response = new.list(10, 5)
assert response[6]['id'] == 12
response = new.id(5)
assert response['todo'] == "Solve a Rubik's cube"
response = new.random()
assert response['id'] > 0
response = new.user(5)
assert response[0]['userId'] == 5
response = new.add()
assert response['id'] == 151
response = new.update(1, False)
assert response['completed'] is False
response = new.remove(1)
assert 'deletedOn' in response
print('Tests passed')
