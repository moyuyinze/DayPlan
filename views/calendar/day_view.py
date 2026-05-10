"""日视图"""

from views.calendar.base_calendar_view import BaseCalendarView
from models.schedule import Schedule


class DayView(BaseCalendarView):
    """单日时间线视图，按小时排列"""

    def set_date_range(self, start, end):
        # TODO
        ...

    def load_schedules(self, schedules: list[Schedule]):
        # TODO
        ...

    def refresh(self):
        # TODO
        ...
