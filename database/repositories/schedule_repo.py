"""日程仓储"""

from typing import Optional

from database.repositories.base_repo import BaseRepository
from models.schedule import Schedule
from models.schedule_filter import ScheduleFilter


class ScheduleRepository(BaseRepository[Schedule]):
    """Schedule 数据访问，继承 BaseRepository[Schedule]"""

    def __init__(self, db_manager):
        self._db = db_manager

    def get_by_id(self, id: int) -> Optional[Schedule]:
        # TODO
        ...

    def get_all(self) -> list[Schedule]:
        # TODO
        ...

    def get_by_date_range(self, start_date, end_date) -> list[Schedule]:
        # TODO: 查询指定日期范围内的日程（含展开后的重复日程）
        ...

    def search(self, filter: ScheduleFilter) -> list[Schedule]:
        # TODO: 根据筛选条件查询
        ...

    def insert(self, entity: Schedule) -> int:
        # TODO: 插入新日程，返回自增 ID
        ...

    def update(self, entity: Schedule) -> bool:
        # TODO: 更新日程
        ...

    def delete(self, id: int) -> bool:
        # TODO: 删除日程
        ...

    def set_completed(self, id: int, completed: bool) -> bool:
        # TODO: 切换完成状态
        ...

    def add_duration(self, id: int, seconds: int):
        # TODO: 累加计时秒数
        ...
