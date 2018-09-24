import pprint

import yaml
from pathlib import Path

from injector import inject, singleton

from src.main.catalog.business.CatalogCreateBusinessLogic import CatalogCreateBusinessLogic
from src.main.catalog.business.CatalogPrepareToApplyBusinessLogic import CatalogPrepareToApplyBusinessLogic
from src.main.catalog.business.CatalogTaskCreateBusinessLogic import CatalogTaskCreateBusinessLogic
from src.main.common.logging.AppLogger import AppLogger
from src.main.common.random.RandomIdGenerator import RandomIdGenerator

@singleton
class CatalogPrepareToApplyBusinessLogicImpl(CatalogPrepareToApplyBusinessLogic):
    __logger: AppLogger
    __catalog_create_business_logic: CatalogCreateBusinessLogic
    __catalog_task_create_business_logic: CatalogTaskCreateBusinessLogic

    @inject
    def __init__(self,
        logger: AppLogger,
        catalog_create_business_logic: CatalogCreateBusinessLogic,
        catalog_task_create_business_logic: CatalogTaskCreateBusinessLogic
    ) -> None:
        self.__logger = logger
        self.__catalog_create_business_logic = catalog_create_business_logic
        self.__catalog_task_create_business_logic = catalog_task_create_business_logic

    def prepare_to_apply(self, catalog_file: str) -> None:
        __catalog_file = Path(catalog_file)

        if __catalog_file.is_file():
            if not (__catalog_file.match('*.yaml') or __catalog_file.match('*.yml')):
                self.__logger.critical('Catalog file must ending with .yml or .yaml!')
                exit(1)
        else:
            self.__logger.critical('Catalog file does not exist!')
            exit(1)

        __catalog_name = __catalog_file.parts[-1].split('.')[0]
        __catalog = self.__catalog_create_business_logic.create(__catalog_name)

        with open(__catalog_file.__bytes__(), 'r') as stream:
            __read_catalog = yaml.load(stream)

        for task in __read_catalog['tasks']:
            if 'register' in task:
                __task_register = task['register']
            else:
                __task_register = None

            self.__catalog_task_create_business_logic.create(
                __catalog.get_id(),
                task['name'],
                None,
                __task_register
            )
