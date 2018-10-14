from injector import inject, singleton

from src.main.catalog.entity.CatalogTask import CatalogTask
from src.main.resource.business.ResourceGetByCatalogTaskIdBusinessLogic import ResourceGetByCatalogTaskIdBusinessLogic
from src.main.resource.entity.Resource import Resource

@singleton
class CatalogTaskAggregate(CatalogTask):
    __resources: []

    @inject
    def __init__(self,
        catalog_task: CatalogTask,
        resource_get_by_catalog_task_id_business_logic: ResourceGetByCatalogTaskIdBusinessLogic
    ) -> None:
        super().__init__(
            catalog_task.id,
            catalog_task.catalog_id,
            catalog_task.name,
            catalog_task.register
        )

        self.__resources = resource_get_by_catalog_task_id_business_logic.get_by_catalog_task_id(catalog_task.id)

    @property
    def resources(self) -> [Resource]:
        return self.__resources