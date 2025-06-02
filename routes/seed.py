from fastapi import APIRouter
from controllers.seed import get_answer_from_seed
seed_router = APIRouter(tags=["Seed"])
@seed_router.get("/")
def get_answer():
    answer = get_answer_from_seed()
    return {"message": "get_seed api testing.", "answer": answer}
