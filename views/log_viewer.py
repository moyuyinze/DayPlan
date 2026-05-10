"""日志查看页 —— QPlainTextEdit 只读"""

from PySide6.QtWidgets import QWidget


class LogViewer(QWidget):
    """操作日志查看页面"""

    def __init__(self, parent=None):
        super().__init__(parent)
        # TODO: QPlainTextEdit 只读展示日志
        # TODO: 清空日志 / 导出日志按钮
        ...
