"""自定义标题栏（可选）"""

from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton


class TitleBar(QWidget):
    """可拖动的自定义标题栏，含窗口控制按钮"""

    def __init__(self, parent=None):
        super().__init__(parent)
        # TODO: 布局：应用名称 + spacer + 最小化/关闭按钮
        ...
