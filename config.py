import os
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())


# URLs
# "postgresql://root:root@localhost:5433/HEADMAN_DB"
DATABASE_URL=os.getenv('PG_DATABASE_URL')


