from injector import singleton

from src.main.catalog.entity.CatalogTask import CatalogTask
from src.main.catalog.storage.CatalogTaskStorage import CatalogTaskStorage

@singleton
class DataMapperCatalogTask(CatalogTaskStorage):
    __catalog_task_storage = dict()

    def insert(self, catalog_task: CatalogTask) -> None:
        self.__catalog_task_storage.__setitem__(catalog_task.id, catalog_task)


