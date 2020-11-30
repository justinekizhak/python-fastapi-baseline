from fastapi import APIRouter

from .endpoints import demo

api_router = APIRouter()

api_router.include_router(demo.router, prefix="/demo", tags=["Demo"])
