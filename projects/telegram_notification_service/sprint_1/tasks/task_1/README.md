# Задача 1. Todo

Поработаем со знакомым нам уже [DummyJSON](https://dummyjson.com/). Нам необходимо 
сделать обертку вокруг [Todo сервиса](https://dummyjson.com/docs/todos), в частности:
1. Получение списка задач (обрати внимание на пагинацию)
1. Получение отдельной задачи
1. Получение случайной задачи
1. Получение задач отдельного пользователя
1. Добавление новой задачи
1. Обновление существующей задачи
1. Удаление существующей задачи

В качестве `User-Agent` неободимо сообщать `Python-Study-App/1.0.0`.

А `Content-Type` и, соответственно, тело запроса должно быть `application/json`.

Реализация должна быть выполнена с использованием классов.

Обращаю внимание на необходимость обработки:
- сетевых ошибок (DNS и т.п.)
- HTTP ошибок
- ошибок JSON десериализации 
- timeouts ошибок
- ошибок большого кол-ва редиректов