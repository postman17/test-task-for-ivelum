# test-task-for-ivelum
## Установка
    - copy .env.example to .env
    - set preposition and main url in settings.py
    - docker-compose up

https://github.com/ivelum/job/blob/master/code_challenges/python.md

Хабрапрокси

Реализовать простой http-прокси-сервер, запускаемый локально (порт на ваше усмотрение), который показывает содержимое страниц Хабра. Прокси должен модицифировать текст на страницах следующим образом: после каждого слова из шести букв должен стоять значок «™». Пример:

Исходный текст: https://habr.com/ru/company/yandex/blog/258673/

Сейчас на фоне уязвимости Logjam все в индустрии в очередной раз обсуждают 
проблемы и особенности TLS. Я хочу воспользоваться этой возможностью, чтобы 
поговорить об одной из них, а именно — о настройке ciphersiutes.

Через ваш прокси™: http://127.0.0.1:8232/ru/company/yandex/blog/258673/

Сейчас™ на фоне уязвимости Logjam™ все в индустрии в очередной раз обсуждают 
проблемы и особенности TLS. Я хочу воспользоваться этой возможностью, чтобы 
поговорить об одной из них, а именно™ — о настройке ciphersiutes. 

Условия:

    Python™ 3.6+
    страницы должны™ отображаться и работать полностью корректно, в точности так, как и оригинальные (за исключением модифицированного текста™);
    при навигации по ссылкам, которые ведут на другие™ страницы хабра, браузер должен™ оставаться на адресе™ вашего™ прокси™;
    можно использовать любые общедоступные библиотеки, которые сочтёте нужным™;
    чем меньше™ кода, тем лучше. PEP8 — обязательно;
    если в условиях вам не хватает каких-то данных™, опирайтесь на здравый смысл.

Если задачу™ удалось сделать быстро™, и у вас еще остался энтузиазм - как насчет™ написания тестов™?

Присылайте ваше решение в виде ссылки на gist или на публичный репозиторий на Github.
