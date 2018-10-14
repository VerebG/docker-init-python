from src.main.catalog.business.CatalogTaskGetByCatalogIdBusinessLogic import CatalogTaskGetByCatalogIdBusinessLogic
from src.main.catalog.entity.Catalog import Catalog
from src.main.catalog.entity.CatalogTask import CatalogTask


class CatalogAggregate(Catalog):
    __catalog_tasks: [CatalogTask]

    def __init__(self,
        catalog: Catalog,
        catalog_task_get_by_catalog_id_business_logic: CatalogTaskGetByCatalogIdBusinessLogic
    ) -> None:
        super().__init__(
            catalog.id,
            catalog.name
        )

        self.__catalog_tasks = catalog_task_get_by_catalog_id_business_logic.get_by_catalog_id(catalog.id)

    @property
    def catalog_tasks(self) -> [CatalogTask]:
        return self.__catalog_tasks