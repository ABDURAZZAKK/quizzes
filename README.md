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
GET /api/questions/?limit=100&skip=0
POST /api/questions/  {"questions_num": 100}
```
