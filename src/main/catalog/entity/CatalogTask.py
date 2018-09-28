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

    def get_id(self) -> str:
        return self.__id

    def get_catalog_id(self) -> str:
        return self.__catalog_id

    def get_name(self) -> str:
        return self.__name

    def get_resource_definition(self) -> Resource:
        return self.__resource_definition

    def get_register(self) -> Optional[str]:
        return self.__register

    def __repr__(self):
        return 'CatalogTask(id: {0}, catalog_id: {1}, name: {2}, resource_definition: {3}, register: {4})'.format(self.get_id(), self.get_catalog_id(), self.get_name(), self.get_resource_definition(), self.get_register())
