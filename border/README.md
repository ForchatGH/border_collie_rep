# Как поднять songs-site локально на своём ПК?
> Вообще-то здесь должно быть описание сайта, но гайд будет полезнее. ;)

## Шаг первый: подготовка
1. Необходимо скачать архив [mysite.zip](https://github.com/clawingcode/songs-site/archive/refs/heads/main.zip).
2. В PyCharm создаём проект с виртуальным окружением и подключаем интерпретатор Python.
3. Ищем в меню Пуск папку Postgre 17, в ней SQL Shell (psql). Запускаем.
4. Добавляем пользователя songs с паролем '1111':
```commandline
CREATE USER songs WITH PASSWORD '1111';
```
5. Вводим команду: 
```commandline
CREATE DATABASE songs OWNER songs ENCODING 'UTF8';
```
5. Просим у меня файл border_collie_data.json.
6. Распаковываем архив из шага 1, копируем  **только** его содержимое, без корневой папки, и вставляем в проект.
7. border_collie_data.json кидаем в корень проекта.
## Шаг второй: установка и настройка
1. Качаем Django:
```commandline
pip install django
```
2. Качаем Pillow:
```commandline
pip install pillow
```
3. Качаем psycopg:
```commandline
pip install "psycopg[binary]"
```
4. Открываем **терминал (не python shell!)** в Pycharm (Alt+F12).
5. Вводим:
```commandline
python manage.py migrate
```
6. Если всё успешно, то вводим:
```commandline
python -Xutf8 manage.py loaddata border_collie_data.json

```
7. Если нет ошибок, запускаем сервер:
```commandline
python manage.py runserver
```
8. Там появится адрес 127.0.0.1:8000. Переходим по нему и знакомимся с сайтом.

>Если возникают ошибки, то отправляем их мне скрином.
