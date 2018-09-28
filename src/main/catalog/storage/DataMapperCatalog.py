from collections import deque
from injector import singleton

from src.main.catalog.entity.Catalog import Catalog
from src.main.catalog.storage.CatalogStorage import CatalogStorage

@singleton
class DataMapperCatalog(CatalogStorage):
    __catalog_storage = deque()

    def insert(self, catalog: Catalog):
        self.__catalog_storage.append(catalog)

    def list(self) -> [Catalog]:
        list(self.__catalog_storage)


