"""全局信号总线 —— Singleton + Observer 模式

解耦跨模块通信。各 Service 不直接依赖彼此的接口，
而是通过 SignalBus 发射和订阅事件。
"""

from PySide6.QtCore import QObject, Signal


class _SignalBus(QObject):
    """集中管理所有跨模块信号"""

    # 日程变更（创建/更新/删除后广播）
    schedule_updated = Signal()

    # 设置变更（key, new_value）
    setting_changed = Signal(str, object)

    # 分类变更
    category_updated = Signal()

    # 通知触发（schedule_id, title, message）
    notification_triggered = Signal(int, str, str)

    # 计时状态变更（schedule_id, is_running）
    timer_state_changed = Signal(int, bool)

    # 视图切换请求（ViewMode）
    view_mode_changed = Signal(object)


class SignalBus:
    """SignalBus Singleton"""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = _SignalBus()
        return cls._instance
