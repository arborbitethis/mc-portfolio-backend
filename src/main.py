from fastapi import FastAPI
from .routes import portfolio_routes, timelapse_routes, recipe_routes


app = FastAPI(
    title="Matthew Courter's Portfolio",
    description="",
    version="0.0.1"
)

wrapper = FastAPI()

app.include_router(portfolio_routes.router)
app.include_router(timelapse_routes.router)
app.include_router(recipe_routes.router)
