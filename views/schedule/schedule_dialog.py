"""创建/编辑日程弹窗"""

from PySide6.QtWidgets import QDialog
from models.schedule import Schedule


class ScheduleDialog(QDialog):
    """模态弹窗，用于创建和编辑日程"""

    def __init__(self, schedule: Schedule = None, parent=None):
        super().__init__(parent)
        self._schedule = schedule  # None = 新建，有值 = 编辑
        # TODO: 表单字段 — 标题/时间/地点/备注/分类/优先级/重复/通知
        ...

    def get_schedule(self) -> Schedule:
        """返回用户填入的 Schedule 对象"""
        # TODO
        ...
