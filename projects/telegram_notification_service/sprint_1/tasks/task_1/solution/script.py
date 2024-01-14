import requests


class Todo(requests.Session):
    def __init__(self):
        super().__init__()
        self.todo_list = None
        self.max_redirects = 5
        self.url = 'https://dummyjson.com/todos'
        self.limit = None
        self.skip = 0
        self.params = {'limit': self.limit, 'skip': self.skip}
        self.headers = {'User-Agent': 'Python-Study-App/1.0.0', 'Content-Type': 'application/json'}

    def get(self, delimiter = 5):
        """
        Метод возвращает указанное в качестве аргумента количество дел
        (значение по умолчанию - 5)
        """
        self.params.update(limit=delimiter)
        try:
            response = super().get(self.url, params=self.params, headers=self.headers)
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
                self.todo_list = response.json()
                return self.todo_list
            except requests.JSONDecodeError:
                return 'Incoming JSON is invalid'

    def next(self, skip=5, delimiter=5):
        """
        Метод позволяет пропустить skip элементов в списке дел
        и получить следующие delimiter дел.
        Значение skip по-умолчанию равно 5.
        Значение delimiter по-умолчанию - 5.
        """
        self.skip += skip
        self.params.update(skip=self.skip)
        return self.get(delimiter)

    def id(self, event_id):
        """Метод позволяет получить из списка конкретное дело
        с заданным пользователем id.
        """
        url = f'{self.url}/{event_id}'
        try:
            response = super().get(url, headers=self.headers)
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

new = Todo()
#print(new.get(10))
#print(new.next(5, 10))
print(new.id(5))