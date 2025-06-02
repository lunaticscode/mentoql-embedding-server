import logging
from typing import Union
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from starlette.exceptions import HTTPException as StarletteHTTPException
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from routes import api_router
from pymilvus import connections
from utils.config import AppConfig

app = FastAPI()
@app.on_event("startup")
def connect_milvus():
    try:
        connections.connect(uri=AppConfig.MILVUS_URL, password=AppConfig.MILVUS_PASSWORD, user=AppConfig.MILVUS_USERNAME, token=AppConfig.MILVUS_TOKEN)
        print("Milvus connected successfully")
    except Exception as e:
        print("(!) Milvus connection failed")
        raise RuntimeError("Failed to connect Milvus") from e

@app.on_event("shutdown")
def connect_milvus():
    connections.disconnect(alias="default")

limiter = Limiter(key_func=get_remote_address, default_limits=["100/minute"])
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

origins = [
    "http://localhost:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api")
@app.get("/health-check", tags=["Health Check"])
def health_check():
    return {"message": "Don't worry, Already activated."}
@app.exception_handler(StarletteHTTPException)
async def custom_exception_handler(request: Request, exc: StarletteHTTPException):
    if exc.status_code == 404:
        return JSONResponse(status_code=404, content={"message": "Not found. Please check request path."})
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail}
    )

if __name__ == "__main__" :
    uvicorn.run("main:app", reload=True)