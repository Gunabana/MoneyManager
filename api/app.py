"""
This module defines the main FastAPI application for Money Manager.
"""

from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from api.routers import accounts, analytics, categories, expenses, users
from config import API_BIND_HOST, API_BIND_PORT

@asynccontextmanager
async def lifespan(_app: FastAPI):
    """Lifespan function that handles app startup and shutdown"""
    yield
    # Handles the shutdown event to close the MongoDB client
    await users.shutdown_db_client()


app = FastAPI(lifespan=lifespan)
app.mount("/static", StaticFiles(directory="api/static"), name="static")

templates = Jinja2Templates(directory="api/templates")

# Include routers for different functionalities
app.include_router(users.router)
app.include_router(accounts.router)
app.include_router(categories.router)
app.include_router(expenses.router)
app.include_router(analytics.router)

# Add a default web app route
@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/signup", response_class=HTMLResponse)
async def signup_page(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})

@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

if __name__ == "__main__":
    uvicorn.run("app:app", host=API_BIND_HOST, port=API_BIND_PORT, reload=True)
