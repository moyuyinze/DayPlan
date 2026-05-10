"""统计数据计算服务"""

from datetime import date
from dataclasses import dataclass


@dataclass
class CategoryStats:
    """分类统计"""
    category_id: int
    category_name: str
    color: str
    total_minutes: int
    percentage: float


@dataclass
class CompletionStats:
    """完成率统计"""
    total: int
    completed: int
    rate: float


class StatisticsService:
    """统计计算"""

    def __init__(self, schedule_repo, category_repo):
        self._schedule_repo = schedule_repo
        self._category_repo = category_repo

    def get_completion_rate(self, start: date, end: date) -> CompletionStats:
        # TODO: 计算指定范围内的完成率
        ...

    def get_category_distribution(self, start: date, end: date) -> list[CategoryStats]:
        # TODO: 计算各分类的时间占比（用于饼图）
        ...

    def get_daily_stats(self, reference_date: date) -> dict:
        # TODO: 单日详细统计
        ...
