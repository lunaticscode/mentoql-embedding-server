from fastapi import APIRouter
from routes.seed import seed_router
api_router = APIRouter()
api_router.include_router(seed_router, prefix="/seed")