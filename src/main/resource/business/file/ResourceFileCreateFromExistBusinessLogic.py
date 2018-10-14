from abc import abstractmethod

from src.main.common.default.DefaultInterface import DefaultInterface
from src.main.resource.entity.ResourceFile import ResourceFile


class ResourceFileCreateFromExistBusinessLogic(DefaultInterface):
    @abstractmethod
    def create_from_exist(self,
        resource_file_abstraction: ResourceFile
    ) -> ResourceFile:
        pass
