from .baseRepo import BaseRepository
from db.tables import questions
from dto_models.question import QuestionDTO
import sqlalchemy as sa



class QuestionRepository(BaseRepository):

    async def create_many(self, questions_list: list[dict]):
        query = sa.insert(questions).values(questions_list)
        _ = await self.session.execute(query)
        await self.session.commit()



    async def get_by_quetion_id(self, q_id: str) -> QuestionDTO | None:
        query = sa.select(questions).where(questions.c.question_id == q_id)
        _ = await self.session.execute(query)
        _ = _.fetchone()

        if _ is None:
            return None
        return _

    async def get_last_question(self) -> QuestionDTO | None:
        query = sa.select(questions).order_by(questions.c.id.desc()).limit(1)
        _ = await self.session.execute(query)

        return _.fetchone()
    