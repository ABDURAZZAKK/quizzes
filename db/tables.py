from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as sa

Base = declarative_base()


class Question(Base):
    __tablename__ = 'some_table'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    question_id = sa.Column(sa.Integer, unique=True)
    question =  sa.Column(sa.Text)
    answer = sa.Column(sa.String(255))
    created_at = sa.Column(sa.DateTime())
