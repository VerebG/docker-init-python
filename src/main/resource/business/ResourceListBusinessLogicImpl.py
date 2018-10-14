from injector import singleton, inject

from src.main.resource.business.ResourceListBusinessLogic import ResourceListBusinessLogic
from src.main.resource.entity.Resource import Resource
from src.main.resource.storage.ResourceStorage import ResourceStorage


@singleton
class ResourceListBusinessLogicImpl(ResourceListBusinessLogic):
    __resource_storage: ResourceStorage

    @inject
    def __init__(self,
        resource_storage: ResourceStorage
    ) -> None:
        self.__resource_storage = resource_storage

    def list(self) -> [Resource]:
        return self.__resource_storage.list()