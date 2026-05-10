"""启动画面"""

from PySide6.QtWidgets import QSplashScreen
from PySide6.QtCore import Qt


class SplashScreen(QSplashScreen):
    """应用启动时展示 2 秒的 Logo 画面"""

    def __init__(self):
        super().__init__()
        # TODO: 设置启动图、显示文字、2 秒后自动关闭
        ...
