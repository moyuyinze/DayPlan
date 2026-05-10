"""设置弹窗"""

from PySide6.QtWidgets import QDialog, QVBoxLayout


class SettingsDialog(QDialog):
    """模态设置窗口 —— 通知/语言/主题/开机自启"""

    def __init__(self, settings_manager, parent=None):
        super().__init__(parent)
        self._settings_mgr = settings_manager
        # TODO: 表单 — 默认通知提前时间（QSpinBox）
        # TODO: 语言选择（QComboBox: 中文/English）
        # TODO: 主题选择（QComboBox: 亮色/暗色）
        # TODO: 开机自启（QCheckBox）
        # TODO: 确定/取消按钮
        ...

    def apply_settings(self):
        # TODO: 收集表单值并调用 settings_manager.set()
        ...
