from typing import List

from injector import singleton, inject

from src.main.resource.business.ResourceGetByCatalogTaskIdBusinessLogic import ResourceGetByCatalogTaskIdBusinessLogic
from src.main.resource.entity.Resource import Resource
from src.main.resource.storage.ResourceStorage import ResourceStorage


@singleton
class ResourceGetByCatalogTaskIdBusinessLogicImpl(ResourceGetByCatalogTaskIdBusinessLogic):
    __resource_storage: ResourceStorage

    @inject
    def __init__(self,
        resource_storage: ResourceStorage
    ) -> None:
        self.__resource_storage = resource_storage

    def get_by_catalog_task_id(self, catalog_task_id: str) -> List[Resource]:
        return self.__resource_storage.get_by_catalog_task_id(catalog_task_id)