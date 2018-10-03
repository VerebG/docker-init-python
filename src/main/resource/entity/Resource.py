from abc import abstractmethod, ABC, ABCMeta

from src.main.common.default.DefaultInterface import DefaultInterface


class Resource(object):
    __id: str
    __catalog_task_id: str
    __state: str
    __checksum: str

    def __init__(self,
        id: str,
        catalog_task_id: str,
        state: str,
        checksum: str
    ) -> None:
        self.__id = id
        self.__catalog_task_id = catalog_task_id
        self.__state = state
        self.__checksum = checksum

    @property
    def id(self) -> str:
        return self.__id

    @property
    def catalog_task_id(self) -> str:
        return self.__catalog_task_id

    @property
    def state(self) -> str:
        return self.__state

    @property
    def checksum(self) -> str:
        return self.__checksum

    @property
    def PRESENT(self) -> str:
        return 'present'

    @property
    def ABSENT(self) -> str:
        return 'absent'

    def __eq__(self, other):
        pass
