from os import chown

from injector import singleton

from src.main.resource.business.file.ResourceFileModifyByOwnerBusinessLogic import \
    ResourceFileModifyByOwnerBusinessLogic
from src.main.resource.entity.ResourceFile import ResourceFile

@singleton
class ResourceFileModifyByOwnerBusinessLogicImpl(ResourceFileModifyByOwnerBusinessLogic):
    def modify(self, resource_file: ResourceFile) -> None:
        chown(resource_file.path.__str__(), resource_file.owner, -1)