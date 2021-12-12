from database import Base
from sqlalchemy import Column, String, Integer


class Human(Base):
    __tablename__ = 'humans'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)