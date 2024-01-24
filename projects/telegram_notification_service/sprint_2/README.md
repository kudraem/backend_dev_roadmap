# Sprint 2
Получив базовое представление о HTTP, попробовав выполнять реальные
HTTP запросы с помощью Python, перейдем к этапу реализации нашего проекта.

В этом спринте мы заложим основу ключевого сервиса - логику отправки сообщений в Telegram (в схеме архитектуры системы - Telegram Bot), а в
качестве дополнительной задачи попробуем реализовать удобную CLI утилиту
для отправки сообщений в Telegram.

## Этап 1. Telegram Bot API и отправка сообщений в Telegram
Задаче данного этапа - реализовать Python пакет 
([Python Import Package](https://packaging.python.org/en/latest/discussions/distribution-package-vs-import-package/#distribution-package-vs-import-package))
для отправки в Telegram сообщений
(содержание сообщения - UTF-8 текст) с помощью 
[Telegram Bot API](https://core.telegram.org/bots/api).

В результате должен получиться пакет, который можно имортировать в 
код любого Python проекта и использовать его для отправки сообщений в Telegram.

При работе необходимо учитывать следующие ключевые моменты:
1. отправлять сообщений пользователю Telegram с помощью Telegram Bot API
можно только после того, как пользователь сам инициирует диалог с данным
ботом, запустив команду `/start`
1. при отправке сообщения пользователю Telegram, используется системный 
идентификатор чата, который, в частности, можно получить при обработке
команды `/start`
1. никаких сторонних библиотек, кроме `requests` для реализации
взаимодействия с Python Bot API использовать нельзя
1. в случае необходимости, [updates получать](https://core.telegram.org/bots/api#getting-updates)
с помощью [getUpdates()](https://core.telegram.org/bots/api#getupdates)

В качестве репозитория для проекта используем [этот репозиторий](https://github.com/kudraem/telegram_msg_sender)
и работаем через Pull Requests.

### Источники
#### Основные
1. [Telegram Bot API Reference](https://core.telegram.org/bots/api)
1. [Tutorial. From BotFather to 'Hello World'](https://core.telegram.org/bots/tutorial) [аналогичный пример на Python](https://gitlab.com/Athamaxy/telegram-bot-tutorial/-/blob/main/TutorialBot.py)
#### Дополнительные
1. [Telegram Bot Features](https://core.telegram.org/bots/features)
1. [Bot API Library Examples](https://core.telegram.org/bots/samples)

## Этап 2. CLI утилита для отправки сообщений в Telegram
На базе пакета, полученного в рамках выполнения предыдущего этапа, необходимо реализовать
удобный CLI инструмент для отправки сообщений в Telegram с использованием
командной строки. Технически такая реализация может быть частью исходного пакета или
вынесена в отдельный пакет - на усмотрение автора.

Интерфейс такой программы необходимо спроектировать самостоятельно с учетом удобства
пользователей и общепринятой практики использования инструментов командной строки.
Программа должна предоставлять документацию по ключу `-h` или `--help`.

Для работы с аргументами командной строки необходимо использовать пакет стандартной
библиотеки Python - [argparse](https://docs.python.org/3/library/argparse.html).

## * Этап 3. Публикация своего пакета в PyPI
Это дополнительная задача, которую можно реализовать по желанию.
Собрать и опубликовать реализованный(-е) пакет(-ы) в PyPI.