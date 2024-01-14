# Задача 2. Мониторинг доступности сайтов

У заказчика есть N сайтов доступность которых необходимо систематически
автоматически мониторить. Для упрощения задачи, представим, что один сайт 
представлен одним URL. 

Необходимо каждую минуту проверять доступность каждого
сайта и сохранять об этом отчет в отдельный файл, где каждая новая строка -
результат очередной провеки отдельного сайта:

`{дата_время} {URL} {результат_проверки}`

Формат `{дата_время}` и `{результат_проверки}` необходимо определить самостоятельно,
но учесть, что формат и содержание должны быть достаточными, чтобы локализовать проблему,
удобными для чтения человеком, удобным для работы автоматических систем, например, для 
парсинга другими программами.

Способ реализации автоматического запуска сервиса необходимо определить
самостоятельно и описать в README файле.