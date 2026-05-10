"""通知服务 —— Singleton + 混合模式

启动时：遍历所有未完成日程的 notify_before / deadline_notify，
       计算触发时间并为每个设置 QTimer.singleShot
运行时：低频轮询（每 5 分钟）做兜底检查，补注册遗漏的通知
"""

from PySide6.QtCore import QObject, QTimer


class NotificationService(QObject):
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
        self._active_timers: dict[int, list[QTimer]] = {}  # schedule_id → [singleShot timers]
        self._poll_timer = None
        self._initialized = True

    def init(self):
        """应用启动时调用：批量计算通知并设置 singleShot，启动轮询"""
        # TODO
        ...

    def refresh_schedule(self, schedule_id: int):
        """单个日程变更后：取消旧通知 → 重新计算注册"""
        # TODO
        ...

    def _poll_check(self):
        """兜底轮询：查询未来 10 分钟内的通知，补注册遗漏"""
        # TODO
        ...

    def _create_notification(self, title: str, message: str):
        """弹出系统通知（QSystemTrayIcon.showMessage）"""
        # TODO
        ...
