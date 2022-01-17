from fastapi import FastAPI
from database import engine
from router import user_router, brand_router, model_router, settings_router, car_router, mileage_router
import model

app = FastAPI()
app.include_router(brand_router.router)
app.include_router(settings_router.router)
app.include_router(mileage_router.router)
app.include_router(model_router.router)
app.include_router(user_router.router)
app.include_router(car_router.router)


model.Base.metadata.create_all(engine)
