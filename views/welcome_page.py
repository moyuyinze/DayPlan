"""欢迎/概览页 —— 今日日程摘要 + 快捷操作"""

from PySide6.QtWidgets import QWidget


class WelcomePage(QWidget):
    """首页，显示今日日程概览和快捷入口"""

    def __init__(self, parent=None):
        super().__init__(parent)
        # TODO: 今日日程摘要卡片
        # TODO: 新建日程 / 查看统计 快捷按钮
        ...
