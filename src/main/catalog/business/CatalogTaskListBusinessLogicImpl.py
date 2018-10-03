from injector import inject, singleton

from src.main.catalog.business.CatalogTaskListBusinessLogic import CatalogTaskListBusinessLogic
from src.main.catalog.entity.CatalogTask import CatalogTask
from src.main.catalog.storage.CatalogTaskStorage import CatalogTaskStorage

@singleton
class CatalogTaskListBusinessLogicImpl(CatalogTaskListBusinessLogic):
    __catalog_task_storage: CatalogTaskStorage

    @inject
    def __init__(self,
        catalog_task_storage: CatalogTaskStorage,
    ) -> None:
        self.__catalog_task_storage = catalog_task_storage

    def list(self) -> [CatalogTask]:
        return self.__catalog_task_storage.list()