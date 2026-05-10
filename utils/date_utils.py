"""日期计算工具函数"""

from datetime import date, datetime, timedelta
from models.enums import RepeatType
from models.schedule import Schedule


def get_week_range(reference_date: date) -> tuple[date, date]:
    """返回包含 reference_date 的周的 (周一, 周日)"""
    # TODO
    ...


def get_month_range(reference_date: date) -> tuple[date, date]:
    """返回包含 reference_date 的月的 (月初, 月末)"""
    # TODO
    ...


def expand_repeat_schedule(schedule: Schedule, start: date, end: date) -> list[Schedule]:
    """将一条重复日程模板展开为指定范围内的具体日程实例列表"""
    # TODO: 根据 schedule.repeat_type 计算所有出现日期
    # TODO: 排除 schedule_exceptions 中的日期
    ...


def is_cross_day(start: datetime, end: datetime) -> bool:
    """判断日程是否跨天"""
    # TODO
    ...
