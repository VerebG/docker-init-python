from yaml import load
from pathlib import Path

from injector import inject, singleton

from src.main.catalog.business.CatalogCreateBusinessLogic import CatalogCreateBusinessLogic
from src.main.catalog.business.CatalogTaskCreateBusinessLogic import CatalogTaskCreateBusinessLogic
from src.main.catalog.entity.Catalog import Catalog
from src.main.catalog.storage.CatalogStorage import CatalogStorage
from src.main.common.constant.Constant import Constant
from src.main.common.logging.AppLogger import AppLogger
from src.main.common.random.RandomIdGenerator import RandomIdGenerator
from src.main.resource.business.ResourceSelectorBusinessLogic import ResourceSelectorBusinessLogic


@singleton
class CatalogCreateBusinessLogicImpl(CatalogCreateBusinessLogic):
    __logger: AppLogger
    __constant: Constant
    __random_id_generator: RandomIdGenerator
    __catalog_task_create_business_logic: CatalogTaskCreateBusinessLogic
    __resource_selector_business_logic: ResourceSelectorBusinessLogic
    __catalog_storage: CatalogStorage

    @inject
    def __init__(self,
        logger: AppLogger,
        constant: Constant,
        random_id_generator: RandomIdGenerator,
        catalog_task_create_business_logic: CatalogTaskCreateBusinessLogic,
        resource_selector_business_logic: ResourceSelectorBusinessLogic,
        catalog_storage: CatalogStorage
    ) -> None:
        self.__logger = logger
        self.__constant = constant
        self.__random_id_generator = random_id_generator
        self.__catalog_task_create_business_logic = catalog_task_create_business_logic
        self.__resource_selector_business_logic = resource_selector_business_logic
        self.__catalog_storage = catalog_storage

    def create(self, catalog_file: str) -> Catalog:
        __catalog_file = Path(catalog_file)

        if __catalog_file.is_file():
            if not (__catalog_file.match('*.yaml') or __catalog_file.match('*.yml')):
                self.__logger.critical('Catalog file must ending with .yml or .yaml!')
        else:
            self.__logger.critical('Catalog file does not exist!')

        __catalog_name = __catalog_file.parts[-1].split('.')[0]
        __catalog = Catalog(self.__random_id_generator.get(), __catalog_name)

        self.__logger.catalog = __catalog_name
        self.__logger.format('%(levelname)s: /Catalog[%(catalog_name)s]: %(message)s')

        with open(__catalog_file.__bytes__(), 'r') as stream:
            __read_catalog = load(stream)
            self.__logger.info('Catalog read successfully!')

        self.__catalog_storage.insert(__catalog)

        readed_task_id = 1
        for task in __read_catalog['tasks']:
            try:
                self.__logger.catalog_task_name = task['name']
            except KeyError:
                task['name'] = '#{0}'.format(readed_task_id)
                self.__logger.catalog_task_name = task['name']

            if not 'register' in task:
                task['register'] = None

            self.__logger.format('%(levelname)s: /Catalog[%(catalog_name)s]/Task[%(catalog_task_name)s]: %(message)s')

            __resource_type = (task.keys()-self.__constant.catalog_task_available_fields).pop()
            if not set(task.keys()).intersection(self.__constant.available_resource_types).__len__() == 1:
                self.__logger.critical('Unknown resource type {0}'.format(__resource_type))

            __catalog_task = self.__catalog_task_create_business_logic.create(__catalog.id, task['name'], task['register'])
            __resource_abstraction_create_business_logic = self.__resource_selector_business_logic.get_resource_abstraction_create_business_logic(__resource_type)
            __resource_abstraction_create_business_logic.create_abstraction(task[__resource_type], __catalog_task.id),

            readed_task_id+=1

        return __catalog