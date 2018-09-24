from abc import abstractmethod

from src.main.catalog.entity.Catalog import Catalog
from src.main.common.default.DefaultInterface import DefaultInterface


class CatalogStorage(DefaultInterface):
    @abstractmethod
    def insert(self, catalog: Catalog):
        pass

    def list(self) -> [Catalog]:
        pass
