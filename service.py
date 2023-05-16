from httpx import AsyncClient, ReadError, ReadTimeout
from dto_models.question import QuestionIn
from repositories.questionRepo import QuestionRepository
from datetime import datetime

def get_datetime(s):
    return datetime.strptime(s, '%Y-%m-%dT%H:%M:%S.%fZ')

async def _get_questions_from_API(count: int, questionRepo:QuestionRepository) -> list[dict]:
    url = f'https://jservice.io/api/random?count={count}'
    count = 0
    questions = []
    async with AsyncClient() as ac:
        try:
            response = await ac.get(url)
            json = response.json()
            for q in json:
                question = await questionRepo.get_by_quetion_id(q['id'])
                if question:
                    count+=1
                else:
                    questions.append(
                        dict(QuestionIn(
                        question_id=q['id'],
                        question=q['question'],
                        answer=q['answer'],
                        created_at= get_datetime(q['created_at'])
                        ))
                    )
            if count:
                try:
                    additional = await _get_questions_from_API(count, questionRepo)
                    print("рекурсия работает")
                    questions = questions + additional
                except RecursionError:
                    pass
        except ReadError:
            pass
        except ReadTimeout:
            pass
        return questions


async def save_questions_from_API(count: int, questionRepo:QuestionRepository) -> int:
    questions = await _get_questions_from_API(count, questionRepo)
    if questions:
        await questionRepo.create_many(questions)
        return len(questions)
    return 0

