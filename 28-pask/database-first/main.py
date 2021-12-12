from fastapi import FastAPI
from database import engine
from routers import human_routers
import modelis

app = FastAPI()
app.include_router(human_routers.router)

modelis.Base.metadata.create_all(engine)
