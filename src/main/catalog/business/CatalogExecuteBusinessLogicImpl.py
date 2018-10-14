from injector import singleton, inject
from pprint import pprint

from src.main.catalog.business.CatalogExecuteBusinessLogic import CatalogExecuteBusinessLogic
from src.main.catalog.business.CatalogListBusinessLogic import CatalogListBusinessLogic
from src.main.catalog.business.CatalogTaskExecuteBusinessLogic import CatalogTaskExecuteBusinessLogic
from src.main.catalog.business.CatalogTaskGetByCatalogIdBusinessLogic import CatalogTaskGetByCatalogIdBusinessLogic
from src.main.catalog.entity.CatalogAggregate import CatalogAggregate
from src.main.catalog.entity.CatalogTaskAggregate import CatalogTaskAggregate
from src.main.common.logging.AppLogger import AppLogger
from src.main.resource.business.ResourceGetByCatalogTaskIdBusinessLogic import ResourceGetByCatalogTaskIdBusinessLogic


@singleton
class CatalogExecuteBusinessLogicImpl(CatalogExecuteBusinessLogic):
    __logger: AppLogger
    __catalog_list_business_logic: CatalogListBusinessLogic
    __catalog_task_get_by_catalog_id_business_logic: CatalogTaskGetByCatalogIdBusinessLogic
    __resource_get_by_catalog_task_id_business_logic: ResourceGetByCatalogTaskIdBusinessLogic
    __catalog_task_execute_business_logic: CatalogTaskExecuteBusinessLogic

    @inject
    def __init__(self,
        logger: AppLogger,
        catalog_list_business_logic: CatalogListBusinessLogic,
        catalog_task_get_by_catalog_id_business_logic: CatalogTaskGetByCatalogIdBusinessLogic,
        resource_get_by_catalog_task_id_business_logic: ResourceGetByCatalogTaskIdBusinessLogic,
        catalog_task_execute_business_logic: CatalogTaskExecuteBusinessLogic
    ) -> None:
        self.__logger = logger
        self.__catalog_list_business_logic = catalog_list_business_logic
        self.__catalog_task_get_by_catalog_id_business_logic = catalog_task_get_by_catalog_id_business_logic
        self.__resource_get_by_catalog_task_id_business_logic = resource_get_by_catalog_task_id_business_logic
        self.__catalog_task_execute_business_logic = catalog_task_execute_business_logic

    def execute(self) -> None:
        for catalog in self.__catalog_list_business_logic.list():
            __catalog_aggregate = CatalogAggregate(catalog, self.__catalog_task_get_by_catalog_id_business_logic)

            self.__logger.catalog = __catalog_aggregate.name
            self.__logger.format('%(levelname)s: /Catalog[%(catalog_name)s]/execute: %(message)s')
            self.__logger.info('{0} task(s) founded'.format(len(__catalog_aggregate.catalog_tasks)))

            for catalog_task in __catalog_aggregate.catalog_tasks:
                __catalog_task_aggregate = CatalogTaskAggregate(catalog_task, self.__resource_get_by_catalog_task_id_business_logic)

                self.__logger.catalog_task_name = __catalog_task_aggregate.name
                self.__logger.format('%(levelname)s: /Catalog[%(catalog_name)s]/Task[%(catalog_task_name)s]/execute: %(message)s')
                self.__logger.info('{0} resource founded'.format(len(__catalog_task_aggregate.resources)))

                self.__catalog_task_execute_business_logic.execute(__catalog_task_aggregate)




