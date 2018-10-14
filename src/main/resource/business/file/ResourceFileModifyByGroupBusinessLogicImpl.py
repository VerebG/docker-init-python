from os import chown

from injector import singleton

from src.main.resource.business.file.ResourceFileModifyByGroupBusinessLogic import \
    ResourceFileModifyByGroupBusinessLogic
from src.main.resource.entity.ResourceFile import ResourceFile

@singleton
class ResourceFileModifyByGroupBusinessLogicImpl(ResourceFileModifyByGroupBusinessLogic):
    def modify(self, resource_file: ResourceFile) -> None:
        chown(resource_file.path.__str__(), -1, resource_file.group)