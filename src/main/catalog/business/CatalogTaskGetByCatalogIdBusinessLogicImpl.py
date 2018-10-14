from injector import singleton, inject

from src.main.catalog.business.CatalogTaskGetByCatalogIdBusinessLogic import CatalogTaskGetByCatalogIdBusinessLogic
from src.main.catalog.entity.CatalogTask import CatalogTask
from src.main.catalog.storage.CatalogTaskStorage import CatalogTaskStorage

@singleton
class CatalogTaskGetByCatalogIdBusinessLogicImpl(CatalogTaskGetByCatalogIdBusinessLogic):
    __catalog_task_storage: CatalogTaskStorage

    @inject
    def __init__(self,
        catalog_task_storage: CatalogTaskStorage
    ) -> None:
        self.__catalog_task_storage = catalog_task_storage

    def get_by_catalog_id(self, catalog_id: str) -> [CatalogTask]:
        return self.__catalog_task_storage.get_by_catalog_id(catalog_id)