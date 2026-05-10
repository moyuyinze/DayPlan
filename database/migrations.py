"""数据库迁移管理"""


def run_migrations(db_manager):
    """检查 db_version 表，按序执行未应用的迁移 SQL"""
    # TODO: 读取 migrations/ 下的 SQL 文件，按版本号排序
    # TODO: 只执行版本号大于当前 db_version 的迁移
    # TODO: 每次执行后在 db_version 表插入新版本号
    ...
