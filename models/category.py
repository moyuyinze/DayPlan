from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass(slots=True)
class Category:
    """分类数据模型"""
    name: str
    id: Optional[int] = None
    color: str = "#4A90D9"
    icon: str = ""
    sort_order: int = 0
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
