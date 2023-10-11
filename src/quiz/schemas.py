from pydantic import BaseModel, ConfigDict
from datetime import datetime


class QuizModel(BaseModel):
    """Validation"""
    model_config = ConfigDict(arbitrary_types_allowed=True)
    id: int
    id_question: id
    question: str
    answer: str
    create_data: datetime

    # class Config:
    #     orm_mode = True
