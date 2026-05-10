from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

from .enums import Priority, RepeatType


@dataclass(slots=True)
class Schedule:
    """日程数据模型"""
    title: str
    start_time: datetime
    end_time: datetime
    id: Optional[int] = None
    description: str = ""
    location: str = ""
    is_cross_day: bool = False
    category_id: Optional[int] = None
    priority: Priority = Priority.NONE
    repeat_type: RepeatType = RepeatType.NONE
    repeat_interval: int = 1
    repeat_end_date: Optional[datetime] = None
    notify_before: Optional[int] = None       # 提前通知分钟数
    deadline_notify: bool = False             # 截止前一天通知
    is_completed: bool = False
    total_duration: int = 0                   # 累计计时秒数
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
