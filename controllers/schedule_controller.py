"""日程控制器 —— MVC 中的 C，协调 Service 与 View

Command 模式预留：可将每个操作封装为 ICommand 对象以支持 undo/redo
"""

from abc import ABC, abstractmethod
from datetime import datetime

from models.schedule import Schedule
from services.schedule_service import ScheduleService
from services.timer_service import TimerService
from utils.signal_bus import SignalBus


class ICommand(ABC):
    """Command 模式接口，预留 undo/redo 扩展"""
    @abstractmethod
    def execute(self):
        ...
    @abstractmethod
    def undo(self):
        ...


class ScheduleController:
    """日程操作控制器，连接 View 信号与 Service 逻辑"""

    def __init__(
        self,
        schedule_service: ScheduleService,
        timer_service: TimerService,
        signal_bus: SignalBus,
    ):
        self._schedule_svc = schedule_service
        self._timer_svc = timer_service
        self._bus = signal_bus
        self._undo_stack: list[ICommand] = []
        self._redo_stack: list[ICommand] = []

    def create_schedule(self, schedule: Schedule):
        # TODO: 调用 service → 发射 signal → 推入 undo_stack
        ...

    def update_schedule(self, schedule: Schedule):
        # TODO
        ...

    def delete_schedule(self, schedule_id: int):
        # TODO
        ...

    def on_drag_drop(self, schedule_id: int, new_start: datetime, new_end: datetime):
        """处理日程拖拽，更新开始/结束时间"""
        # TODO: 校验时间 → 更新数据库 → 发射信号
        ...

    def start_timer(self, schedule_id: int):
        # TODO: 调用 TimerService.start()
        ...

    def pause_timer(self):
        # TODO
        ...

    def stop_timer(self):
        # TODO: 停止计时 → 保存 timer_record → 累加 total_duration
        ...

    def undo(self):
        # TODO: 从 undo_stack 弹出并执行 undo
        ...

    def redo(self):
        # TODO
        ...
