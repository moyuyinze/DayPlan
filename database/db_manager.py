"""数据库连接管理器 —— Singleton 模式"""


class DBManager:
    """管理 SQLite 连接、建表、事务"""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        self._connection = None
        self._initialized = True

    def connect(self, db_path: str):
        # TODO: 建立 SQLite 连接，启用 WAL 模式和外键约束
        ...

    def execute(self, sql: str, params=None):
        # TODO: 执行单条 SQL
        ...

    def transaction(self):
        # TODO: 返回上下文管理器，支持 with 语句自动 commit/rollback
        ...

    def close(self):
        # TODO: 关闭连接
        ...
