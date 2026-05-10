"""设置仓储"""

from typing import Optional


class SettingsRepository:
    """应用设置 KV 存储"""

    def __init__(self, db_manager):
        self._db = db_manager

    def get(self, key: str, default: str = None) -> Optional[str]:
        # TODO
        ...

    def set(self, key: str, value: str):
        # TODO
        ...

    def get_all(self) -> dict[str, str]:
        # TODO
        ...
