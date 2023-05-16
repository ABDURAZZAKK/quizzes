from fastapi import APIRouter, Depends
from repositories.questionRepo import QuestionRepository
from dto_models.question import QuestionDTO
from depends import get_question_repository
from service import save_questions_from_API
from fastapi import BackgroundTasks


question_router = APIRouter()


@question_router.post("/", response_model=QuestionDTO|None)
async def create_question(
    questions_num: int,
    background: BackgroundTasks,
    questionRepo: QuestionRepository = Depends(get_question_repository)
):
    last_question = await questionRepo.get_last_question()
    background.add_task(save_questions_from_API,questions_num, questionRepo)

    return last_question

@question_router.get("/", response_model=list[QuestionDTO])
async def get_all(
    questionRepo: QuestionRepository = Depends(get_question_repository),
    limit: int = 100,
    skip: int = 0,
):
    return await questionRepo.get_all(limit, skip)