from collections import deque
from injector import singleton

from src.main.catalog.entity.Catalog import Catalog
from src.main.catalog.storage.CatalogStorage import CatalogStorage

@singleton
class DataMapperCatalog(CatalogStorage):
    __catalog_storage = dict()

    def insert(self, catalog: Catalog):
        self.__catalog_storage.__setitem__(catalog.id, catalog)

    def list(self) -> [Catalog]:
        return [catalog for catalog in self.__catalog_storage.values()]

