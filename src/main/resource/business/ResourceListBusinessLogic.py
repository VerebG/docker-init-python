from abc import abstractmethod

from src.main.common.default.DefaultInterface import DefaultInterface
from src.main.resource.entity.Resource import Resource


class ResourceListBusinessLogic(DefaultInterface):
    @abstractmethod
    def list(self) -> [Resource]:
        pass