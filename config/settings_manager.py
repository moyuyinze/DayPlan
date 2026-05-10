"""设置管理器 —— Singleton 模式"""
from PySide6.QtCore import QObject, Signal, QSettings


class SettingsManager(QObject):
    """全局设置管理，使用 QSettings 做存储，变更时发射信号通知各模块"""

    settings_changed = Signal(str, object)  # key, new_value

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        super().__init__()
        self._settings = QSettings("DayPlan", "DayPlan")
        self._initialized = True

    def get(self, key: str, default=None):
        # TODO: 从 QSettings 读取
        ...

    def set(self, key: str, value):
        # TODO: 写入 QSettings 并发射 settings_changed 信号
        ...

    def reset(self, key: str):
        # TODO: 重置某项设置为默认值
        ...
