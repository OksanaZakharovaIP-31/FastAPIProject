from sqlalchemy import DateTime, Text, Integer, Column
from sqlalchemy.ext.declarative import declarative_base

from database import engine, Base


class Quiz(Base):
    """Create a model"""
    __tablename__ = 'quiz'
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    id_question = Column(Integer, unique=True)
    question = Column(Text)
    answer = Column(Text)
    create_data = Column(DateTime)

    def __repr__(self):
        return 'Quiz {self.id!r},{self.question!r},{self.answer!r}'


Base.metadata.create_all(bind=engine)
