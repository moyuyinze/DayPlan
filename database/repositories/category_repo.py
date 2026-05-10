"""分类仓储"""

from typing import Optional

from database.repositories.base_repo import BaseRepository
from models.category import Category


class CategoryRepository(BaseRepository[Category]):
    """Category 数据访问"""

    def __init__(self, db_manager):
        self._db = db_manager

    def get_by_id(self, id: int) -> Optional[Category]:
        ...

    def get_all(self) -> list[Category]:
        ...

    def insert(self, entity: Category) -> int:
        ...

    def update(self, entity: Category) -> bool:
        ...

    def delete(self, id: int) -> bool:
        ...
