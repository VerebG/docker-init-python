from abc import abstractmethod
from typing import Optional


class Resource(object):
    __id: str
    __catalog_task_id: str
    __state: str

    def __init__(self,
        id: str,
        catalog_task_id: str,
        state: str
    ) -> None:
        self.__id = id
        self.__catalog_task_id = catalog_task_id
        self.__state = state

    @property
    def id(self) -> str:
        return self.__id

    @property
    def catalog_task_id(self) -> str:
        return self.__catalog_task_id

    @property
    def state(self) -> str:
        return self.__state

    @abstractmethod
    def __eq__(self, other):
        pass

    @property
    @abstractmethod
    def resource_attr_to_comparison(self) -> set:
        pass

    @property
    @abstractmethod
    def can_register(self) -> Optional[str]:
        pass

    @property
    @abstractmethod
    def create_from_exist(self) -> str:
        pass
