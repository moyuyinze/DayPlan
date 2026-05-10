"""侧边导航组件"""

from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from PySide6.QtCore import Signal


class Sidebar(QWidget):
    """侧边栏：导航按钮 + 置顶开关"""

    nav_changed = Signal(int)        # 请求切换 StackedWidget 页面索引
    pin_toggled = Signal()           # 请求切换置顶
    floating_toggled = Signal()      # 请求切换悬浮窗

    def __init__(self):
        super().__init__()
        # TODO: 创建 QVBoxLayout
        # TODO: 添加日历/统计/设置 导航按钮
        # TODO: 添加置顶/悬浮窗切换按钮
        ...
