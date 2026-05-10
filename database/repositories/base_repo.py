"""仓储抽象基类 —— Repository 模式"""

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional

T = TypeVar("T")


class BaseRepository(ABC, Generic[T]):
    """通用仓储接口，定义 CRUD 操作"""

    @abstractmethod
    def get_by_id(self, id: int) -> Optional[T]:
        ...

    @abstractmethod
    def get_all(self) -> list[T]:
        ...

    @abstractmethod
    def insert(self, entity: T) -> int:
        ...

    @abstractmethod
    def update(self, entity: T) -> bool:
        ...

    @abstractmethod
    def delete(self, id: int) -> bool:
        ...
