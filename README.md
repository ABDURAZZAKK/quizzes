# Quizzes

# Запуск проекта 

## Создать в корне .env файл с содержимым:

``` bash
# POSTGRES
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=quizze
```

## Docker

```
docker compose up
```

# ENDPOINTS:

```
GET /docs/ автодокументация для тестирования от fastAPI
GET /api/questions/?limit=100&skip=0  получить список вопросов
POST /api/questions/  {"questions_num": 100} добавить в бд N вопросов
```
