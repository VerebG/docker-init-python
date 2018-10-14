from os import chmod

from src.main.resource.business.file.ResourceFileModifyByModeBusinessLogic import ResourceFileModifyByModeBusinessLogic
from src.main.resource.entity.ResourceFile import ResourceFile


class ResourceFileModifyByModeBusinessLogicImpl(ResourceFileModifyByModeBusinessLogic):
    def modify(self, resource_file: ResourceFile) -> None:
        chmod(resource_file.path.__str__(), int(resource_file.mode, 8))