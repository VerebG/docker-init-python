from abc import abstractmethod

from src.main.common.default.DefaultInterface import DefaultInterface
from src.main.resource.entity.ResourceFile import ResourceFile


class ResourceFileCreateAbstractionBusinessLogic(DefaultInterface):
    @abstractmethod
    def create_abstraction(self,
        resource_definition: {},
        catalog_task_id: str
    ) -> ResourceFile:
        pass