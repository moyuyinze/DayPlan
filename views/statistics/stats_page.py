"""统计页面 —— 完成率 + 分类饼图 + 用时统计"""

from PySide6.QtWidgets import QWidget, QVBoxLayout
from services.statistics_service import StatisticsService


class StatsPage(QWidget):
    """数据统计展示页面"""

    def __init__(self, stats_service: StatisticsService, parent=None):
        super().__init__(parent)
        self._stats_service = stats_service
        # TODO: 完成率区域（日期范围选择 + 进度条/百分比）
        # TODO: 分类饼图（可用 Qt Charts 或 matplotlib）
        # TODO: 日程用时统计表格
        ...

    def refresh(self):
        # TODO: 重新计算并更新所有图表
        ...
