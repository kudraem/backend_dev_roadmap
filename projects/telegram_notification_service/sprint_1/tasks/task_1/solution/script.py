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

    def list(self, delimiter=5, step=0):
        """
        Метод позволяет пропустить skip элементов в списке дел
        и получить следующие delimiter дел.
        Значение skip по-умолчанию равно 0.
        Значение delimiter по-умолчанию - 5.
        """
        return self.get(delimiter=delimiter, step=step)['todos']

    def id(self, event_id):
        """Метод позволяет получить из списка конкретное дело
        с заданным пользователем id.
        """
        return self.get(f'{self.url}/{event_id}')

    def random(self):
        """
        Метод позволяет получить произвольное дело из списка
        """
        return self.get(f'{self.url}/random')

    def user(self, user_id, delimiter=0, step=0):
        """
        Метод позволяет получить список дел конкретного пользователя
        по его id.
        Метод позволяет также выводить ограниченное количество дел
        (параметр delimiter), а также пропускать первые step дел
        пользователя
        """
        return self.get(f'{self.url}/user/{user_id}')['todos']

    def add(self, event='To do nothing', completion=False, user_id=1):
        """
        Метод позволяет добавить свое дело в общий список.
        В качестве входных параметров требует:
        1) Текстовое описание самого дела;
        2) Статус завершенности (True - завершено, False = не завершено;
        3) ID пользователя
        Значения по умолчанию: 'To do nothing', False, 0.
        """
        url = 'https://dummyjson.com/todos/add'
        request_body = {
            'todo': event,
            'completed': completion,
            'userId': user_id
        }
        return self.post(url, request_body)


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
print('Tests passed')