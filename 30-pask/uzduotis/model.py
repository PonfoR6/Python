from database import Base
from sqlalchemy import Column, String, Integer


class Cars(Base):
    __tablename__ = 'blog'

    id = Column(Integer, primary_key=True, index=True)
    Topic = Column(String)
    Active_members = Column(Integer)
    Comments = Column(Integer)