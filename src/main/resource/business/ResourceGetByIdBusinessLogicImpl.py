from injector import singleton, inject

from src.main.resource.business.ResourceGetByIdBusinessLogic import ResourceGetByIdBusinessLogic
from src.main.resource.storage.ResourceStorage import ResourceStorage


@singleton
class ResourceGetByIdBusinessLogicImpl(ResourceGetByIdBusinessLogic):
    __resource_storage: ResourceStorage

    @inject
    def __init__(self,
        resource_storage: ResourceStorage
    ) -> None:
        self.__resource_storage = resource_storage

    def get_by_id(self, id: str):
        self.__resource_storage.get_by_id(id)

