"""
ASGI config for webapp project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from fastapi import FastAPI
from api.app import app as fastapi_app  # FastAPI app is located in api/app.py
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.routing import Mount
from starlette.applications import Starlette

# Set Django settings module path
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webapp.settings")

# Get the Django ASGI application
django_app = get_asgi_application()

# Define a CombinedApp class to mount both FastAPI and Django
class CombinedApp(Starlette):
    def __init__(self, django_app, fastapi_app, **kwargs):
        # Mount Django app at the root path '/'
        # Mount FastAPI app at '/api'
        routes = [
            Mount("/", app=django_app),        # Django app
            Mount("/api", app=fastapi_app),    # FastAPI app
        ]
        super().__init__(routes=routes, **kwargs)

# Create the combined ASGI application instance
application = CombinedApp(django_app=django_app, fastapi_app=fastapi_app)



