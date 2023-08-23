from fastapi import FastAPI
from .routes import portfolio_routes


app = FastAPI(
    title="Matthew Courter's Portfolio",
    description="",
    version="0.0.1"
)

wrapper = FastAPI()

app.include_router(portfolio_routes.router)
