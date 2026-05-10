"""日程列表项组件"""

from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Signal


class ScheduleListWidget(QWidget):
    """单条日程的展示卡片"""

    clicked = Signal(int)         # 点击时发射 schedule_id
    edit_requested = Signal(int)  # 请求编辑
    delete_requested = Signal(int)

    def __init__(self, schedule, parent=None):
        super().__init__(parent)
        self._schedule = schedule
        # TODO: 展示标题/时间/分类颜色/优先级图标/完成状态
        ...
