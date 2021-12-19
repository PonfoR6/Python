from fastapi import FastAPI
from database import engine
from blog_router import blog_router
import model

app = FastAPI()
app.include_router(blog_router.router)

model.Base.metadata.create_all(engine)
