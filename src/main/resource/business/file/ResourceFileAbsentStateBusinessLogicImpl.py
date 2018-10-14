from os import remove

from injector import singleton

from src.main.resource.business.file.ResourceFileAbsentStateBusinessLogic import ResourceFileAbsentStateBusinessLogic
from src.main.resource.entity.ResourceFile import ResourceFile

@singleton
class ResourceFileAbsentStateBusinessLogicImpl(ResourceFileAbsentStateBusinessLogic):
    def absent_state(self, resource_file: ResourceFile):
        remove(resource_file.path.__str__())