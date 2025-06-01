from fastapi import APIRouter
seed_router = APIRouter(tags=["Seed"])
@seed_router.get("/")
def get_seed():
    return {"message": "get_seed api testing."}
