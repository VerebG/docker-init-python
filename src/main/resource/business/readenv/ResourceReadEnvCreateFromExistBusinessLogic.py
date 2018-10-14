from abc import abstractmethod

from src.main.common.default.DefaultInterface import DefaultInterface
from src.main.resource.entity.ResourceReadEnv import ResourceReadEnv


class ResourceReadEnvCreateFromExistBusinessLogic(DefaultInterface):
    @abstractmethod
    def create_from_exist(self,
        resource_read_env_abstraction: ResourceReadEnv
    ) -> ResourceReadEnv:
        pass