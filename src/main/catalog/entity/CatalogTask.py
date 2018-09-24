from typing import Optional

from src.main.common.random.RandomIdGenerator import RandomIdGenerator
from src.main.resource.entity.Resource import Resource


class CatalogTask(object):
    __random_id_generator: RandomIdGenerator
    __catalog_id: str
    __name: str
    __resource_definition: Resource
    __register: Optional[str]

    def __init__(self,
        random_id_generator: RandomIdGenerator,
        catalog_id: str,
        name: str,
        resource_definition: Resource,
        register: Optional[str]
    ) -> None:
        self.__id = random_id_generator.get()
        self.__catalog_id = catalog_id
        self.__name = name
        self.__resource_definition = resource_definition
        self.__register = register
