"""日历头部导航栏"""

from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QLabel
from PySide6.QtCore import Signal


class CalendarHeader(QWidget):
    """年月切换 / 今天按钮 / 视图模式切换"""

    date_changed = Signal(object)          # 当前显示日期变更
    view_mode_changed = Signal(object)     # ViewMode 切换

    def __init__(self, parent=None):
        super().__init__(parent)
        # TODO: 左箭头 / 日期显示 / 右箭头 / 今天按钮 / 月周日切换按钮
        ...
