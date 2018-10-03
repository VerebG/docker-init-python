from abc import abstractmethod

from src.main.common.default.DefaultInterface import DefaultInterface
from src.main.resource.entity.Resource import Resource


class ResourceStorage(DefaultInterface):
    @abstractmethod
    def insert(self, resource: Resource) -> None:
        pass