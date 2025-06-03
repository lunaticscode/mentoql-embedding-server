import os
from dotenv import load_dotenv
load_dotenv()

class AppConfig:
    OPENROUTER_AI_KEY: str = os.getenv("OPENROUTER_AI_KEY", "")
    MILVUS_URL: str = os.getenv("MILVUS_URL", "")
    MILVUS_TOKEN: str = os.getenv("MILVUS_TOKEN", "")
    MILVUS_USERNAME: str = os.getenv("MILVUS_USERNAME", "")
    MILVUS_PASSWORD: str = os.getenv("MILVUS_PASSWORD", "")
    JWT_SECRET: str = os.getenv("JWT_SECRET", "")
    JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM", "")

