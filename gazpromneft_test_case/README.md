Текст тестового задания - `test-data\Тестовое задание`  

Тестовые данные - `test-data\testing_data`  


Для запуска необходимо в корне проекта создать файл .env и написать туда следующие переменные:

`DJANGO_SECRET_KEY`=Ключ безопасности django.  

`POSTGRES_DB`=Имя БД.  

`POSTGRES_USER`=Пользователь привязанный к БД.  

`PAYMENT_PASSWORD`=Пароль пользователя привязанного к БД.  

`POSTGRES_HOST`=localhost  

`PAYMENT_PORT`=5432  


Далее выполняем по порядку следующие команды:

`docker-compose build`  

`docker-compose up` 

После переходим по адресу `http://localhost:8000/` и можно тестировать приложение.  
