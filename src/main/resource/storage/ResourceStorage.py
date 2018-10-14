from abc import abstractmethod

from src.main.common.default.DefaultInterface import DefaultInterface
from src.main.resource.entity.Resource import Resource


class ResourceStorage(DefaultInterface):
    @abstractmethod
    def insert(self, resource: Resource) -> None:
        pass

    @abstractmethod
    def get_by_id(self, id: str) -> Resource:
        pass

    @abstractmethod
    def get_by_catalog_task_id(self, catalog_task_id: str) -> [Resource]:
        pass

    @abstractmethod
    def list(self) -> [Resource]:
        pass