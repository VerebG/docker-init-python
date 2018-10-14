from injector import singleton, inject

from src.main.resource.business.file.ResourceFileModifyByContentBusinessLogic import \
    ResourceFileModifyByContentBusinessLogic
from src.main.resource.business.file.ResourceFileModifyByGroupBusinessLogic import \
    ResourceFileModifyByGroupBusinessLogic
from src.main.resource.business.file.ResourceFileModifyByModeBusinessLogic import ResourceFileModifyByModeBusinessLogic
from src.main.resource.business.file.ResourceFileModifyByOwnerBusinessLogic import \
    ResourceFileModifyByOwnerBusinessLogic
from src.main.resource.business.file.ResourceFilePresentStateBusinessLogic import ResourceFilePresentStateBusinessLogic
from src.main.resource.entity.ResourceFile import ResourceFile


@singleton
class ResourceFilePresentStateBusinessLogicImpl(ResourceFilePresentStateBusinessLogic):
    __resource_file_modify_by_content: ResourceFileModifyByContentBusinessLogic
    __resource_file_modify_by_owner: ResourceFileModifyByOwnerBusinessLogic
    __resource_file_modify_by_group: ResourceFileModifyByGroupBusinessLogic
    __resource_file_modify_by_mode: ResourceFileModifyByModeBusinessLogic

    @inject
    def __init__(self,
        resource_file_modify_by_content: ResourceFileModifyByContentBusinessLogic,
        resource_file_modify_by_owner: ResourceFileModifyByOwnerBusinessLogic,
        resource_file_modify_by_group: ResourceFileModifyByGroupBusinessLogic,
        resource_file_modify_by_mode: ResourceFileModifyByModeBusinessLogic
    ) -> None:
        self.__resource_file_modify_by_content = resource_file_modify_by_content
        self.__resource_file_modify_by_owner = resource_file_modify_by_owner
        self.__resource_file_modify_by_group = resource_file_modify_by_group
        self.__resource_file_modify_by_mode = resource_file_modify_by_mode

    def present_state(self, resource_file: ResourceFile) -> None:
        self.__resource_file_modify_by_content.modify(resource_file)
        self.__resource_file_modify_by_owner.modify(resource_file)
        self.__resource_file_modify_by_group.modify(resource_file)
        self.__resource_file_modify_by_mode.modify(resource_file)