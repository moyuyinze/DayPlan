"""DayPlan 应用入口"""

import sys
import os

from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon

from config.constants import APP_NAME, DB_FILENAME
from config.settings_manager import SettingsManager
from database.db_manager import DBManager
from database.migrations import run_migrations
from database.repositories.schedule_repo import ScheduleRepository
from database.repositories.category_repo import CategoryRepository
from database.repositories.settings_repo import SettingsRepository
from services.schedule_service import ScheduleService
from services.notification_service import NotificationService
from services.timer_service import TimerService
from services.statistics_service import StatisticsService
from services.import_export_service import ImportExportService
from controllers.schedule_controller import ScheduleController
from controllers.settings_controller import SettingsController
from utils.signal_bus import SignalBus
from utils.logger import setup_logger
from views.main_window import MainWindow


def main():
    setup_logger(APP_NAME)

    app = QApplication(sys.argv)
    app.setApplicationName(APP_NAME)
    app.setOrganizationName("DayPlan")

    # 初始化基础设施
    db = DBManager()
    db_path = os.path.join(os.path.dirname(__file__), DB_FILENAME)
    db.connect(db_path)
    run_migrations(db)

    # 初始化仓储层
    schedule_repo = ScheduleRepository(db)
    category_repo = CategoryRepository(db)
    settings_repo = SettingsRepository(db)

    # 初始化服务层
    signal_bus = SignalBus()
    settings_mgr = SettingsManager()
    schedule_svc = ScheduleService(schedule_repo)
    timer_svc = TimerService()
    stats_svc = StatisticsService(schedule_repo, category_repo)
    notification_svc = NotificationService()
    import_export_svc = ImportExportService(schedule_repo, category_repo)

    # 初始化控制器
    schedule_ctrl = ScheduleController(schedule_svc, timer_svc, signal_bus)
    settings_ctrl = SettingsController(settings_mgr, signal_bus)

    # 启动通知服务
    notification_svc.init()

    # 显示主窗口
    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
