"""周视图"""

from views.calendar.base_calendar_view import BaseCalendarView
from models.schedule import Schedule


class WeekView(BaseCalendarView):
    """以周为单位的水平时间轴视图，类似 Google Calendar"""

    def set_date_range(self, start, end):
        # TODO: 周一至周日，7 列 + 时间轴
        ...

    def load_schedules(self, schedules: list[Schedule]):
        # TODO: 在时间轴上放置日程块
        ...

    def refresh(self):
        # TODO
        ...
