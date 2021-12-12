from pydantic import BaseModel
from database import Base


class HumansShortInfo(Base):
    first_name: str
    last_name: str
