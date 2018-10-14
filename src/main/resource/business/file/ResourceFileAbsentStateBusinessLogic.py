from abc import abstractmethod

from src.main.common.default.DefaultInterface import DefaultInterface
from src.main.resource.entity.ResourceFile import ResourceFile


class ResourceFileAbsentStateBusinessLogic(DefaultInterface):
    @abstractmethod
    def absent_state(self, resource_file: ResourceFile):
        pass