import os
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())


PG_HOST=os.getenv('POSTGRES_HOST')
PG_PORT=os.getenv('POSTGRES_PORT')
PG_USER=os.getenv('POSTGRES_USER')
PG_PASSWORD=os.getenv('POSTGRES_PASSWORD')
PG_DB=os.getenv('POSTGRES_DB')
# URLs
# "postgresql+asyncpg://POSTGRES:POSTGRES@localhost:5433/quizzes"
DATABASE_URL= f"postgresql+asyncpg://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DB}"

