"""日历视图抽象基类 —— Strategy 模式"""

from abc import abstractmethod

from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal

from models.schedule import Schedule


class BaseCalendarView(QWidget):
    """所有日历视图（月/周/日）的抽象基类"""

    date_selected = Signal(object)                          # 选中某天
    schedule_clicked = Signal(int)                          # 点击日程
    schedule_dropped = Signal(int, object, object)          # 日程被拖拽：(schedule_id, new_start, new_end)
    view_change_requested = Signal(object)                  # 请求切换视图模式

    @abstractmethod
    def set_date_range(self, start, end):
        """设置当前显示的日期范围"""
        ...

    @abstractmethod
    def load_schedules(self, schedules: list[Schedule]):
        """加载日程数据并渲染"""
        ...

    @abstractmethod
    def refresh(self):
        """刷新当前视图"""
        ...
