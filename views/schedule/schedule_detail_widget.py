"""日程详情面板"""

from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Signal


class ScheduleDetailWidget(QWidget):
    """点击日程后显示的详情面板（含计时操作）"""

    timer_start = Signal(int)
    timer_pause = Signal(int)
    timer_stop = Signal(int)

    def __init__(self, parent=None):
        super().__init__(parent)
        # TODO: 显示标题/时间/描述/地点/备注/计时状态/计时操作按钮
        ...
