from injector import singleton

from src.main.resource.entity.Resource import Resource
from src.main.resource.storage.ResourceStorage import ResourceStorage

@singleton
class DataMapperResource(ResourceStorage):
    __resource_storage = dict()

    def insert(self, resource: Resource) -> None:
        self.__resource_storage.__setitem__(resource.id, resource)
