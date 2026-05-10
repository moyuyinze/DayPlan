"""应用级常量定义"""

APP_NAME = "DayPlan"
APP_VERSION = "1.0.0"

# 通知默认提前时间（分钟）
DEFAULT_NOTIFY_BEFORE = 15

# 兜底轮询间隔（毫秒），默认 5 分钟
POLLING_INTERVAL_MS = 5 * 60 * 1000

# 数据库文件名
DB_FILENAME = "dayplan.db"

# 设置 key 常量
SETTING_LANGUAGE = "language"
SETTING_THEME = "theme"
SETTING_AUTO_START = "auto_start"
SETTING_DEFAULT_NOTIFY = "default_notify_before"
