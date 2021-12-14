from fastapi import FastAPI
from database import engine
from routers import human_routers
import models

app = FastAPI()
app.include_router(human_routers.router)

models.Base.metadata.create_all(engine)
