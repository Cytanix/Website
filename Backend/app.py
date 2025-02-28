# Copyright (c) 2025 SpiritTheWalf and Cytanix
# All rights reserved.
#
# This software is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License
# To view a copy of this license, visit https://creativecommons.org/licenses/by-nc-sa/4.0/ or see the LICENSE file.
"""Defines the main app"""
from typing import Dict
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from routes import router as routes

ENVIRONMENT: str = "development"
api = FastAPI()
api.include_router(routes)
templates = Jinja2Templates(directory="../Frontend/templates")
api.mount("/assets", StaticFiles(directory="../Frontend/assets"))

@api.get("/", response_class=HTMLResponse) # type: ignore
async def root(request: Request) -> HTMLResponse:
    """Defines the root endpoint."""
    return templates.TemplateResponse("index.html", {"request": request})