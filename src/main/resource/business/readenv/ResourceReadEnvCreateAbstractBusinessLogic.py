from abc import abstractmethod

from src.main.common.default.DefaultInterface import DefaultInterface
from src.main.resource.entity.ResourceReadEnv import ResourceReadEnv


class ResourceReadEnvCreateAbstractBusinessLogic(DefaultInterface):
    @abstractmethod
    def create_abstraction(self,
        resource_definition: {},
        catalog_task_id: str
    ) -> ResourceReadEnv:
        pass