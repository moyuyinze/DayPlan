"""关于弹窗"""

from PySide6.QtWidgets import QDialog


class AboutDialog(QDialog):
    """关于 DayPlan 的信息弹窗"""

    def __init__(self, parent=None):
        super().__init__(parent)
        # TODO: 应用名称/版本/作者
        # TODO: QLabel + 超链接（GitHub / 教程地址）
        ...
