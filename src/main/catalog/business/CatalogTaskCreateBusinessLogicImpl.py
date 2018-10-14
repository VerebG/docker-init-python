from typing import Optional
from injector import inject

from src.main.catalog.business.CatalogTaskCreateBusinessLogic import CatalogTaskCreateBusinessLogic
from src.main.catalog.entity.CatalogTask import CatalogTask
from src.main.catalog.storage.CatalogTaskStorage import CatalogTaskStorage
from src.main.common.logging.AppLogger import AppLogger
from src.main.common.random.RandomIdGenerator import RandomIdGenerator


class CatalogTaskCreateBusinessLogicImpl(CatalogTaskCreateBusinessLogic):
    __logger: AppLogger
    __catalog_task_storage: CatalogTaskStorage
    __random_id_generator: RandomIdGenerator

    @inject
    def __init__(self,
        logger: AppLogger,
        catalog_task_storage: CatalogTaskStorage,
        random_id_generator: RandomIdGenerator
    ) -> None:
        self.__logger = logger
        self.__catalog_task_storage = catalog_task_storage
        self.__random_id_generator = random_id_generator

    def create(self,
        catalog_id: str,
        name: str,
        register: Optional[str]
    ) -> CatalogTask:
        __catalog_task = CatalogTask(
            self.__random_id_generator.get(),
            catalog_id,
            name,
            register
        )

        self.__catalog_task_storage.insert(__catalog_task)

        return __catalog_task