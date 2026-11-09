from datetime import datetime
from typing import Any, Literal

from pydantic import BaseModel, Field


class Chunk(BaseModel):
    """文档分块：解析+分块后入库的最小单位"""

    text: str = Field(..., description="分块文本内容")
    file_name: str = Field(..., description="来源文件名")
    chunk_id: str = Field(..., description="分块唯一ID，如 file_hash_index")
    index: int = Field(..., ge=0, description="该文件内的分块序号，从0开始")
    metadata: dict[str, Any] = Field(default_factory=dict)


class SearchResult(BaseModel):
    """检索结果：向量召回后用于证据溯源和Prompt组装"""

    chunk: Chunk
    score: float = Field(..., ge=0.0, le=1.0, description="相似度分数，越大越相关")


class ChatMessage(BaseModel):
    """会话消息"""

    role: Literal["user", "assistant", "system"]
    content: str
    timestamp: datetime = Field(default_factory=datetime.now)
    sources: list[SearchResult] = Field(default_factory=list)
