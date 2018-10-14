from abc import abstractmethod

from src.main.common.default.DefaultInterface import DefaultInterface
from src.main.resource.entity.ResourceFile import ResourceFile


class ResourceFileModifyByModeBusinessLogic(DefaultInterface):
    @abstractmethod
    def modify(self, resource_file: ResourceFile) -> None:
        pass