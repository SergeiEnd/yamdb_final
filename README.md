# YaMDb API
![example workflow](https://github.com/SergioEnd/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

### Описание проекта:

Проект YaMDb собирает отзывы пользователей на произведения, позволяет ставить произведениям оценку и комментировать чужие отзывы.

Произведения делятся на категории, и на жанры. Список произведений, категорий и жанров может быть расширен администратором.

Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.

Доступ к БД проекта осуществляется через Api.
### Технологии
- Python 3.7 (asgiref 3.5.2, coreapi 2.3.3, coreschema 0.0.4, cryptography 38.0.4, flake8 5.0.4, importlib-metadata 1.7.0, pycodestyle 2.9.1, pycparser 2.21, pyflakes 2.5.0, PyJWT 2.1.0, pytest 6.2.4,pytest-django 4.4.0, pytest-pythonpath 0.7.3, python3-openid 3.2.0, pytz 2022.6, PyYAML 6.0, requests 2.26.0, requests-oauthlib 1.3.1, sqlparse 0.4.3, typing_extensions 4.4.0, uritemplate 4.1.1, urllib3 1.26.13, python-dotenv 0.21.0, psycopg2-binary)
- Django 3.2 (django-filter,django-import-export, django-templated-mail)
- Django REST Framework 3.12.4 (djangorestframework 3.12.4, djangorestframework-simplejwt 4.7.2 djoser 2.1.0)
- Gunicorn 20.0.4
- Nginx 1.21.3

### Полный список запросов и эндпоинтов описан в документации ReDoc, доступна после запуска проекта по адресу:
```
localhost/redoc/
```

### Как запустить проект в контейнерах:
Клонировать репозиторий, перейти в директорию с проектом.

```
git clone git@github.com:SergeiEnd/infra_sp2.git
```
Перейти в директорию с docker-compose.yaml
```
cd infra_sp2/infra/
```
Создать и заполнить .env-файл по шаблону:
```
DB_ENGINE=указываем, что работаем с postgresql
DB_NAME=имя базы данных
POSTGRES_USER=логин для подключения к базе данных
POSTGRES_PASSWORD=пароль для подключения к БД
DB_HOST=название сервиса (контейнера)
DB_PORT=порт для подключения к БД
SECRET_KEY=секретный ключ
```
Запустить docker-compose
```
docker-compose up
```
Выполнить миграции
```
docker-compose exec web python manage.py migrate
```
Создание суперпользователя
```
docker-compose exec web python manage.py createsuperuser
```
Сбор в статики контейнерах
``` 
docker-compose exec web python manage.py collectstatic --no-input
```
Наполненеие базы данных из фикстур
```
docker-compose exec web python manage.py loaddata fixtures.json
```

### Авторизация пользователей:
Для получения доступа необходимо создать пользователя отправив POST запрос на эндпоинт ```/api/v1/auth/signup/``` username и email

Запрос:
```
{
	"email": "string",
	"username": "string"
}
```
После этого на email придет код подтверждения, который вместе с username необходимо отправить POST запросом на эндпоинт```/api/v1/auth/token/```

Запрос:
```
{
	"username": "string",
	"confirmation_code": "string"
}
```
Ответ:
```
{
	"access": "string"
}
```
Полученный токен используется для авторизации

Для просмотра и изменения своих данных используйте эндпоинт ```/api/v1/users/me/```

### Примеры запросов к API:
```
IP адрес сервера : 158.160.30.110
```
Получение списка всех категорий:
```
/api/v1/categories/
```
Получение списка всех жанров:
```
/api/v1/genres/
```
Получение списка всех произведений:
```
/api/v1/titles/
```

Автор: Ендовицкий Сергей (https://github.com/SergeiEnd)