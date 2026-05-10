"""悬浮小窗 —— 今日日程精简视图"""

from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt, QTimer


class FloatingWindow(QWidget):
    """置顶悬浮窗，展示今日日程摘要"""

    def __init__(self, parent=None):
        super().__init__(parent, Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        # TODO: 设置窗口标志（无边框 + 置顶）
        # TODO: 紧凑布局 — 日期 + 今日日程列表
        # TODO: 双击回到主窗口
        # TODO: 定时刷新（每分钟更新显示）
        ...

    def refresh_today(self):
        # TODO: 从 ScheduleService 获取今日日程并更新显示
        ...
