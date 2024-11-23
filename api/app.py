"""
This module defines the main FastAPI application for Money Manager.
"""

from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI, Request, Header, Response, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from typing import Optional

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

@app.get("/logout", response_class=HTMLResponse)
async def logout(request: Request, response: Response):
    result = await users.logout(response, request)

    if result.get("message") == "Logout successful":
        redirect_response = RedirectResponse(url="/login", status_code=302)
        if "set-cookie" in response.headers:
            redirect_response.headers["set-cookie"] = response.headers["set-cookie"] # the fix to the cookie not invalidating after 2 hours of debugging
        return redirect_response

    raise HTTPException(status_code=400, detail="Logout failed")

@app.get("/landing", response_class=HTMLResponse)
async def landing_page(request: Request, token: Optional[str] = Header(None)):
    token = request.cookies.get("access_token")  # retrieve token from cookies
    if not token:
        return RedirectResponse(url="/login", status_code=302)

    try:
        username = await users.get_username(token)
        return templates.TemplateResponse("landing.html", {"request": request, "username": username})
    except HTTPException as e:
        return RedirectResponse(url="/login", status_code=302)
    except Exception as e:
        print(f"Error in landing page: {e}")
        return RedirectResponse(url="/login", status_code=302)

@app.get("/categories", response_class=HTMLResponse)
async def landing_page(request: Request, token: Optional[str] = Header(None)):
    token = request.cookies.get("access_token")  # retrieve token from cookies
    if not token:
        return RedirectResponse(url="/login", status_code=302)

    try:
        username = await users.get_username(token)
        return templates.TemplateResponse("categories.html", {"request": request, "username": username})
    except HTTPException as e:
        return RedirectResponse(url="/landing", status_code=302)
    except Exception as e:
        print(f"Error in landing page: {e}")
        return RedirectResponse(url="/landing", status_code=302)

@app.get("/expenses", response_class=HTMLResponse)
async def landing_page(request: Request, token: Optional[str] = Header(None)):
    token = request.cookies.get("access_token")  # retrieve token from cookies
    if not token:
        return RedirectResponse(url="/login", status_code=302)

    try:
        username = await users.get_username(token)
        return templates.TemplateResponse("expenses.html", {"request": request, "username": username})
    except HTTPException as e:
        return RedirectResponse(url="/landing", status_code=302)
    except Exception as e:
        print(f"Error in landing page: {e}")
        return RedirectResponse(url="/landing", status_code=302)

@app.get("/barchart", response_class=HTMLResponse)
async def landing_page(request: Request, token: Optional[str] = Header(None)):
    token = request.cookies.get("access_token")  # retrieve token from cookies
    if not token:
        return RedirectResponse(url="/login", status_code=302)

    try:
        username = await users.get_username(token)
        return templates.TemplateResponse("barchart.html", {"request": request, "username": username})
    except HTTPException as e:
        return RedirectResponse(url="/landing", status_code=302)
    except Exception as e:
        print(f"Error in landing page: {e}")
        return RedirectResponse(url="/landing", status_code=302)


if __name__ == "__main__":
    uvicorn.run("app:app", host=API_BIND_HOST, port=API_BIND_PORT, reload=True)
