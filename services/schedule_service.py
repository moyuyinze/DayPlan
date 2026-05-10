"""日程业务逻辑 —— Factory 模式 + 领域服务"""

from datetime import date, datetime
from typing import Optional

from models.schedule import Schedule
from models.schedule_filter import ScheduleFilter
from database.repositories.schedule_repo import ScheduleRepository


class ScheduleService:
    """日程 CRUD + 重复日程展开 + 跨天处理"""

    def __init__(self, schedule_repo: ScheduleRepository):
        self._repo = schedule_repo

    def create_schedule(self, schedule: Schedule) -> int:
        """创建日程，根据 repeat_type 做工厂式构造"""
        # TODO: 校验字段 → 插入数据库 → 发射 signal_bus.schedule_updated
        ...

    def update_schedule(self, schedule: Schedule) -> bool:
        # TODO
        ...

    def delete_schedule(self, schedule_id: int) -> bool:
        # TODO
        ...

    def get_schedule(self, schedule_id: int) -> Optional[Schedule]:
        # TODO
        ...

    def get_schedules_by_range(self, start: date, end: date) -> list[Schedule]:
        """获取日期范围内所有日程（含重复日程展开）"""
        # TODO: 查询原始日程 → expand_repeat_schedule 展开 → 合并返回
        ...

    def search_schedules(self, filter: ScheduleFilter) -> list[Schedule]:
        # TODO
        ...

    def toggle_completed(self, schedule_id: int) -> bool:
        # TODO: 切换完成状态并发射信号
        ...
