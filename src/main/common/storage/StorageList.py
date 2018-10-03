from abc import abstractmethod
from typing import TypeVar, Generic, Optional

T = TypeVar('T')

class StorageList(Generic[T]):
    _storage = dict()

    def insert(self, element_id: str, element: T) -> None:
        self._storage[element_id] = element

    @abstractmethod
    def load_by_element_id(self, element_id: str) -> T:
        pass

    def load_by_element_attribute(self, condition: dict) -> Optional[T, T:list]:
        pass

    def load_all(self) -> [T]:
        self._storage.values()