from pydantic import BaseModel
from datetime import datetime



class QuestionDTO(BaseModel):
    id: int
    question_id: int
    question: str
    answer: str
    created_at: datetime
    
    class Config:
        orm_mode = True
