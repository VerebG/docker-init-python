from injector import singleton

from src.main.catalog.entity import CatalogTask
from src.main.catalog.storage.CatalogTaskStorage import CatalogTaskStorage

@singleton
class DataMapperCatalogTask(CatalogTaskStorage):
    __catalog_task_storage = [CatalogTask]

    def insert(self, catalog_task: CatalogTask) -> None:
        self.__catalog_task_storage.append(catalog_task)