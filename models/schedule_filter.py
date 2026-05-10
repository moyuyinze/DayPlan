from dataclasses import dataclass, field
from datetime import date
from typing import Optional


@dataclass(slots=True)
class ScheduleFilter:
    """日程筛选参数"""
    keyword: str = ""
    category_id: Optional[int] = None
    date_from: Optional[date] = None
    date_to: Optional[date] = None
    only_completed: Optional[bool] = None
