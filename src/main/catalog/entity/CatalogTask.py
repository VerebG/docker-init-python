from typing import Optional

from src.main.common.random.RandomIdGenerator import RandomIdGenerator
from src.main.resource.entity.Resource import Resource


class CatalogTask(object):
    __catalog_id: str
    __id: str
    __name: str
    __register: Optional[str]

    def __init__(self,
        id: str,
        catalog_id: str,
        name: str,
        register: Optional[str]
    ) -> None:
        self.__id = id
        self.__catalog_id = catalog_id
        self.__name = name
        self.__register = register

    @property
    def id(self) -> str:
        return self.__id

    @property
    def catalog_id(self) -> str:
        return self.__catalog_id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def register(self) -> Optional[str]:
        return self.__register

    # def __repr__(self):
    #     return 'CatalogTask(id: {0}, catalog_id: {1}, name: {2}, resource_definition: {3}, register: {4})'.format(self.id, self.catalog_id, self.name, self.register)
