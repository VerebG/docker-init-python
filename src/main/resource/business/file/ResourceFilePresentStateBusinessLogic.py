from abc import abstractmethod

from src.main.common.default.DefaultInterface import DefaultInterface
from src.main.resource.entity.ResourceFile import ResourceFile


class ResourceFilePresentStateBusinessLogic(DefaultInterface):
    @abstractmethod
    def present_state(self, resource_file: ResourceFile) -> None:
        pass