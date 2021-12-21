from fastapi import FastAPI
import model
from database import engine
from routers import user_routers
from routers import blog_routers

app = FastAPI()
app.include_router(user_routers.router)
app.include_router(blog_routers.router)

model.Base.metadata.create_all(engine)
