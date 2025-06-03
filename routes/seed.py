from fastapi import APIRouter
from pydantic import BaseModel
from controllers.seed import get_answer_from_seed
from controllers.seed import insert_seed_from_mento
from middlewares.auth_middleware import auth_middleware
def seed_route_logging():
    print("seed_route_logging")
    return "asd"

seed_router = APIRouter(tags=["Seed"], dependencies=[auth_middleware()])
@seed_router.get("/")
def get_answer():
    answer = get_answer_from_seed()
    return {"message": "get_seed api testing.", "answer": answer}

class SeedInput(BaseModel):
    question: str
    answer: str
@seed_router.post("/")
def insert_seed(seed: SeedInput):
    insert_result = insert_seed_from_mento(seed.question, seed.answer)
    return ""
