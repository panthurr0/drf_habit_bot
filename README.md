# Трекер полезных привычек

В 2018 году Джеймс Клир написал книгу «Атомные привычки», которая посвящена приобретению новых полезных привычек и
искоренению старых плохих привычек. В проекте, вдохновленном этой книгой, была реализована бэкенд-часть SPA
веб-приложения.

## Стэк:

<div>
     <img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original-wordmark.svg" alt="python" width="40" height="40"/>&nbsp;
   <img src="https://github.com/devicons/devicon/blob/master/icons/django/django-plain.svg" alt="django" width="40" height="40"/>&nbsp;
   <img src="https://github.com/devicons/devicon/blob/master/icons/postgresql/postgresql-original-wordmark.svg" alt="psql" width="40" height="40"/>&nbsp;
   <img src="https://github.com/devicons/devicon/blob/master/icons/djangorest/djangorest-original-wordmark.svg" alt="djangorest" width="40" height="40"/>&nbsp;
   <img src="https://github.com/devicons/devicon/blob/master/icons/redis/redis-original-wordmark.svg" alt="redis" width="40" height="40"/>&nbsp;
   <img src="https://github.com/devicons/devicon/blob/master/icons/swagger/swagger-original-wordmark.svg" alt="swagger" width="40" height="40"/>&nbsp;
   <img src="https://github.com/devicons/devicon/blob/master/icons/pytest/pytest-original-wordmark.svg" alt="pytest" width="40" height="40"/>
</div>
В проекте, при создании привычки от авторизированного пользователя HabitCreateApiView создаётся таска в Celery-beat, 
которая отправляет запрос телеграму, а он уведомляет пользователя о привычке

[Посмотреть настройки Celery-beat](config/settings.py)\
[HabitCreateApiView](habit/views.py)\
[Тесты](habit/tests.py)\
[URL-запросы для CRUD привычек](habit/urls.py)\
[Валидация при создании привычки](habit/validators.py)

## Getting started:

1. Установка зависимостей(команда применит зависимости, а также установит миграции):\
   `docker compose up --build -d`
2. Адрес для доступа: \
http://localhost:8000/

Пример запроса создания привычки
`{
"place": "Дома",
"habit_time": "16:46:00",
"action": "Позаниматься на тренажере",
"is_nice_habit": "false",
"periodicity": 2,
"reward": "",
"complete_time": "16:47:00",
"is_public": true,
"is_active": true,
}`