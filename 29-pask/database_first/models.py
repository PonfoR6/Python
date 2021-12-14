from database import Base
from sqlalchemy import Column, String, Integer


class Cars(Base):
    __tablename__ = 'cars'

    id = Column(Integer, primary_key=True, index=True)
    model = Column(String)
    make = Column(String)
    type = Column(String)