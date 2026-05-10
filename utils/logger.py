"""统一日志配置"""

import logging

_logger = None


def setup_logger(app_name: str = "DayPlan", level=logging.DEBUG):
    # TODO: 配置 StreamHandler + FileHandler
    ...


def get_logger() -> logging.Logger:
    # TODO: 返回全局 logger
    ...
