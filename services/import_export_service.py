"""日程导入导出服务 —— 备份恢复场景"""

import json
from pathlib import Path


class ImportExportService:
    """JSON 格式的日程数据导入导出"""

    def __init__(self, schedule_repo, category_repo):
        self._schedule_repo = schedule_repo
        self._category_repo = category_repo

    def export_to_json(self, file_path: Path) -> bool:
        """将全部日程数据导出为 JSON 文件"""
        # TODO: 查询所有 schedule + category → 转为 dict → json.dump
        ...

    def import_from_json(self, file_path: Path) -> int:
        """从 JSON 文件导入日程数据，返回导入条数"""
        # TODO: json.load → 解析 dict → 插入数据库
        ...
