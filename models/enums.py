from enum import IntEnum, Enum


class Priority(IntEnum):
    """日程优先级"""
    NONE = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    URGENT = 4


class RepeatType(Enum):
    """重复类型"""
    NONE = "none"
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"


class ViewMode(Enum):
    """日历视图模式"""
    MONTH = "month"
    WEEK = "week"
    DAY = "day"
