import requests

from typing import List

from fastapi import FastAPI, Depends

from database import session
from quiz.models import Quiz
from quiz.schemas import QuizModel
from sqlalchemy.orm import Session

app = FastAPI()

""" create a database session and close it after finishing """


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


@app.get("/", response_model=List[QuizModel])
def get_quiz(db: Session = Depends(get_db)):
    """
    Get function
    Returns all objects from database (all quiz question)
    """
    results = db.query(Quiz).all()
    return results


@app.post('/', response_model=QuizModel)
def add_quiz(count: int, db: Session = Depends(get_db)) -> None:
    """
    :param count: int
    :param db: Session = Depends(get_db)
    :return: None

    Post function
    Add {count} new question(s) to quiz database. If question is already in database ->
    make requests while found question which is not in database
    """
    url = f'https://jservice.io/api/random?count={count}'
    response = requests.get(url)
    data = response.json()
    for res in data:
        while db.query(Quiz).filter(Quiz.id_question == res["id"]).first() is not None:
            url = 'https://jservice.io/api/random?count=1'
            response = requests.get(url)
            res = response.json()[0]

        new_quiz = Quiz(
            id_question=res["id"],
            question=res["question"],
            answer=res["answer"],
            create_data=res["created_at"]
        )
        db.add(new_quiz)
        db.commit()
        db.refresh(new_quiz)
