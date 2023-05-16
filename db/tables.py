import sqlalchemy as sa

metadata = sa.MetaData()


# class Question(Base):
#     __tablename__ = 'some_table'
#     id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
#     question_id = sa.Column(sa.Integer, unique=True)
#     question =  sa.Column(sa.Text)
#     answer = sa.Column(sa.String(255))
#     created_at = sa.Column(sa.DateTime())

questions = sa.Table(
    "questions",
    metadata,
    sa.Column('id',sa.Integer, primary_key=True, autoincrement=True),
    sa.Column('question_id',sa.Integer, unique=True),
    sa.Column('question',sa.Text),
    sa.Column('answer',sa.String(255)),
    sa.Column('created_at',sa.DateTime())
)