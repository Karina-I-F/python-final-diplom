
## Документация по проекту

Отправка сообщений на почту и импорт товаров магазина через Celery. Flowers для мониторинга Celery задач.

###Для запуска проекта необходимо:

Добавить виртуальные переменные локально в .env
```
SECRET_KEY=
DEBUG=
ALLOWED_HOSTS=.localhost, .127.0.0.1, .testserver, .0.0.0.0

# DATABASE SETTINGS
POSTGRES_DB=pythonfinaldiplom
POSTGRES_USER=pythonfinaldiplom
POSTGRES_PASSWORD=pythonfinaldiplom
POSTGRES_HOST=db
POSTGRES_PORT=5432

# EMAIL SETTINGS
EMAIL_HOST=smtp.mail.ru # or smtp.gmail.com
EMAIL_HOST_USER= # put your email here
EMAIL_HOST_PASSWORD= # create a password for the application and put it here

# CELERY STUFF
CELERY_RESULT_BACKEND=redis://redis:6379/0
CELERY_BROKER_URL=redis://redis:6379/1
CELERY_TIMEZONE=UTC
```

Создать образы и запустить контейнеры:

```bash
docker-compose up -d --build
```

Открыть терминал внутри контейнера:

```bash
docker-compose exec django sh
```

Создать суперпользователя для админки (там же можно изменить тип пользователя на "магазин"):

```bash
python manage.py createsuperuser
```

Прогнать тесты:

```bash
python manage.py test tests.backend
```
