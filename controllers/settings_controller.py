"""设置控制器"""

from config.settings_manager import SettingsManager
from utils.signal_bus import SignalBus


class SettingsController:
    """连接 SettingsDialog 与 SettingsManager"""

    def __init__(self, settings_manager: SettingsManager, signal_bus: SignalBus):
        self._mgr = settings_manager
        self._bus = signal_bus

    def apply_setting(self, key: str, value):
        # TODO: 调用 settings_manager.set() → 必要时通知相关 Service 刷新
        ...

    def load_settings(self) -> dict:
        # TODO: 返回当前所有设置项的 dict
        ...
