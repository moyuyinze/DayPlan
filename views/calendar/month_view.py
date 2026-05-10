"""月视图"""

from views.calendar.base_calendar_view import BaseCalendarView
from models.schedule import Schedule


class MonthView(BaseCalendarView):
    """以月为单位的网格日历"""

    def set_date_range(self, start, end):
        # TODO: 计算当月所有日期，按周排列成 6×7 网格
        ...

    def load_schedules(self, schedules: list[Schedule]):
        # TODO: 将日程卡片放置到对应日期格子中
        ...

    def refresh(self):
        # TODO
        ...
