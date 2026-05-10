"""日程计时服务 —— 跑表逻辑"""

from PySide6.QtCore import QObject, QTimer, Signal


class TimerService(QObject):
    """管理单个日程的计时（开始/暂停/停止）"""

    timer_tick = Signal(int, int)      # schedule_id, elpased_seconds
    timer_state = Signal(int, bool)    # schedule_id, is_running

    def __init__(self):
        super().__init__()
        self._active_schedule_id: int | None = None
        self._qt_timer = QTimer()
        self._qt_timer.timeout.connect(self._on_tick)
        self._elapsed = 0

    def start(self, schedule_id: int):
        # TODO: 开始计时
        ...

    def pause(self) -> int:
        """暂停计时，返回当前累计秒数"""
        # TODO
        ...

    def stop(self) -> int:
        """停止计时，保存 timer_record，返回总秒数"""
        # TODO
        ...

    def is_running(self) -> bool:
        # TODO
        ...

    def _on_tick(self):
        # TODO: 每秒更新 _elapsed，发射 timer_tick
        ...
