from abc import abstractmethod

from src.main.catalog.entity import CatalogTask
from src.main.common.default.DefaultInterface import DefaultInterface


class CatalogTaskStorage(DefaultInterface):
    @abstractmethod
    def insert(self, catalog_task: CatalogTask) -> None:
        pass

    @abstractmethod
    def get_by_catalog_id(self, catalog_id: str) -> [CatalogTask]:
        pass

    @abstractmethod
    def list(self) -> [CatalogTask]:
        pass