import os
from pathlib import Path
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / "data"
UPLOAD_DIR = DATA_DIR / "uploads"
VECTOR_DIR = DATA_DIR / "vectors"
CHROMA_PERSIST_DIR = DATA_DIR / "chroma"

# 确保必要目录存在
for _d in [DATA_DIR, UPLOAD_DIR, VECTOR_DIR, CHROMA_PERSIST_DIR]:
    _d.mkdir(parents=True, exist_ok=True)


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # 存储模式：json（调试） / chroma（演示）
    STORE_MODE: Literal["json", "chroma"] = "json"

    # ChromaDB 配置
    CHROMA_HOST: str = "localhost"
    CHROMA_PORT: int = 8000
    CHROMA_COLLECTION_NAME: str = "rag_knowledge_base"

    # Embedding 配置
    EMBEDDING_MODEL: str = "BAAI/bge-small-zh"
    EMBEDDING_DEVICE: str = "cpu"

    # 文本分块配置
    CHUNK_SIZE: int = 512
    CHUNK_OVERLAP: int = 80

    # 检索配置
    TOP_K: int = 4
    SCORE_THRESHOLD: float = 0.4

    # DeepSeek API 配置
    DEEPSEEK_API_KEY: str = ""
    DEEPSEEK_BASE_URL: str = "https://api.deepseek.com"
    DEEPSEEK_MODEL: str = "deepseek-chat"
    DEEPSEEK_TEMPERATURE: float = 0.1
    DEEPSEEK_MAX_TOKENS: int = 1024

    # 文件上传限制
    MAX_FILE_SIZE_MB: int = 50
    ALLOWED_EXTENSIONS: set[str] = {"pdf", "txt", "md", "markdown"}


settings = Settings()
