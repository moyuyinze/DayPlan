"""主窗口 —— 侧边导航 + QStackedWidget + 系统托盘"""

from PySide6.QtWidgets import QMainWindow, QStackedWidget, QHBoxLayout, QWidget
from PySide6.QtCore import Signal

from views.sidebar import Sidebar
from views.floating_window import FloatingWindow


class MainWindow(QMainWindow):
    """应用主窗口，组装全局布局"""

    window_pinned = Signal(bool)   # 置顶状态切换

    def __init__(self):
        super().__init__()
        self._floating_window: FloatingWindow | None = None
        self._stacked = None
        self._sidebar = None
        self._tray_icon = None
        # TODO: init_ui() → 布局侧边栏 + StackedWidget
        # TODO: 设置系统托盘图标
        ...

    def toggle_pin(self):
        """切换桌面置顶状态"""
        # TODO: WindowStaysOnTopHint 切换
        ...

    def toggle_floating_window(self):
        """切换悬浮小窗显示/隐藏"""
        # TODO: 创建/显示/隐藏 FloatingWindow
        ...

    def closeEvent(self, event):
        # TODO: 最小化到托盘而非直接退出
        ...
