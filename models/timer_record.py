from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass(slots=True)
class TimerRecord:
    """计时记录——每次开始/暂停为一个记录"""
    schedule_id: int
    started_at: datetime
    id: Optional[int] = None
    ended_at: Optional[datetime] = None
    duration: int = 0          # 秒数，结束时计算
