"""分类管理页 —— QListWidget 增删改"""

from PySide6.QtWidgets import QWidget


class CategoryManager(QWidget):
    """独立分类管理页面"""

    def __init__(self, parent=None):
        super().__init__(parent)
        # TODO: QListWidget 展示所有分类
        # TODO: 新增 / 编辑 / 删除 分类
        ...
