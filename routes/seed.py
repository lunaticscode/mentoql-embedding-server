from fastapi import APIRouter
from pydantic import BaseModel
from controllers.seed import get_answer_from_seed
from controllers.seed import insert_seed_from_mento
from middlewares.auth_middleware import auth_middleware

seed_router = APIRouter(tags=["Seed"])
@seed_router.get("/")
def get_answer():
    answer = get_answer_from_seed()
    return {"message": "get_seed api testing.", "answer": answer}

class SeedInput(BaseModel):
    question: str
    answer: str
@seed_router.post("/")
def insert_seed(seed: SeedInput, mento: dict = auth_middleware()):
    print(seed)
    mento_id = mento['mento_id']
    insert_result = insert_seed_from_mento(seed.question, seed.answer, mento_id)
    return ""
