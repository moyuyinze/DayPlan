"""开机自启服务 —— Windows 注册表操作"""


class AutoStartService:
    """通过 HKCU\Software\Microsoft\Windows\CurrentVersion\Run 实现开机自启"""

    _REG_PATH = r"Software\Microsoft\Windows\CurrentVersion\Run"

    def enable(self):
        # TODO: 写入注册表
        ...

    def disable(self):
        # TODO: 删除注册表项
        ...

    def is_enabled(self) -> bool:
        # TODO: 检查注册表项是否存在
        ...
