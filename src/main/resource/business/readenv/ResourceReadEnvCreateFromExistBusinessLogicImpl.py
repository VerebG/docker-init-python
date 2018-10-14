from os import environ

from injector import singleton

from src.main.resource.business.readenv.ResourceReadEnvCreateFromExistBusinessLogic import \
    ResourceReadEnvCreateFromExistBusinessLogic
from src.main.resource.entity.ResourceReadEnv import ResourceReadEnv

@singleton
class ResourceReadEnvCreateFromExistBusinessLogicImpl(ResourceReadEnvCreateFromExistBusinessLogic):
    def create_from_exist(self,
        resource_read_env_abstraction: ResourceReadEnv
    ) -> ResourceReadEnv:
        try:
            return ResourceReadEnv(
                '',
                '',
                '',
                resource_read_env_abstraction.create_from_exist,
                environ[resource_read_env_abstraction.create_from_exist],
                None
            )
        except KeyError:
            return ResourceReadEnv(
                '',
                '',
                '',
                resource_read_env_abstraction.create_from_exist,
                resource_read_env_abstraction.default_value,
                None
            )