from injector import singleton, inject

from src.main.common.logging.AppLogger import AppLogger
from src.main.common.random.RandomIdGenerator import RandomIdGenerator
from src.main.resource.business.readenv.ResourceReadEnvCreateAbstractBusinessLogic import \
    ResourceReadEnvCreateAbstractBusinessLogic
from src.main.resource.entity.ResourceReadEnv import ResourceReadEnv
from src.main.resource.storage.ResourceStorage import ResourceStorage


@singleton
class ResourceReadEnvCreateAbstractBusinessLogicImpl(ResourceReadEnvCreateAbstractBusinessLogic):
    __logger: AppLogger
    __random_id_generator: RandomIdGenerator
    __resource_storage: ResourceStorage

    @inject
    def __init__(self,
        logger: AppLogger,
        random_id_generator: RandomIdGenerator,
        resource_storage: ResourceStorage
    ) -> None:
        self.__logger = logger
        self.__random_id_generator = random_id_generator
        self.__resource_storage = resource_storage

    def create_abstraction(self,
        resource_definition: {},
        catalog_task_id: str
    ) -> ResourceReadEnv:
        self.__logger.catalog_task_resource_name = 'Unknow'
        self.__logger.format('%(levelname)s: /Catalog[%(catalog_name)s]/Task[%(catalog_task_name)s]/Environment[%(catalog_task_resource_name)s]/Read: %(message)s')

        if not 'default' in resource_definition:
            resource_definition['default'] = ''
            self.__logger.warning('Default field is not filled, I set to empty string')

        if 'name' in resource_definition:
            # try:
            #     resource_definition['value'] = environ[resource_definition['name']]
            # except KeyError:
            #     resource_definition['value'] = resource_definition['default']
            self.__logger.catalog_task_resource_name = resource_definition['name']
        else:
            self.__logger.critical('Must fill environment name')

        __resource_storage = ResourceReadEnv(
            self.__random_id_generator.get(),
            catalog_task_id,
            'stateless',
            resource_definition['name'],
            None,
            resource_definition['default']
        )

        self.__resource_storage.insert(__resource_storage)

        return __resource_storage
