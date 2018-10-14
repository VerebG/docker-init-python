from injector import singleton

from src.main.catalog.entity.CatalogTask import CatalogTask
from src.main.catalog.storage.CatalogTaskStorage import CatalogTaskStorage

@singleton
class DataMapperCatalogTask(CatalogTaskStorage):
    __catalog_task_storage = dict()

    def insert(self, catalog_task: CatalogTask) -> None:
        self.__catalog_task_storage.__setitem__(catalog_task.id, catalog_task)

    def get_by_catalog_id(self, catalog_id: str) -> [CatalogTask]:
        return [catalog_task for catalog_task in self.__catalog_task_storage.values() if catalog_task.catalog_id.__eq__(catalog_id)]




