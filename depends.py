from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from db.base import get_async_session
from db.tables import questions
from dto_models.question import QuestionDTO
from repositories.questionRepo import QuestionRepository



async def get_question_repository(
    session: AsyncSession = Depends(get_async_session),
) -> QuestionRepository:
    return QuestionRepository(session, questions, QuestionDTO)
