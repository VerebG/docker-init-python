from injector import singleton

from src.main.resource.entity.Resource import Resource
from src.main.resource.storage.ResourceStorage import ResourceStorage

@singleton
class DataMapperResource(ResourceStorage):
    __resource_storage = dict()

    def insert(self, resource: Resource) -> None:
        self.__resource_storage.__setitem__(resource.id, resource)

    def get_by_id(self, id: str) -> Resource:
        return self.__resource_storage.get(id)

    def get_by_catalog_task_id(self, catalog_task_id: str) -> [Resource]:
        return [resource for resource in self.__resource_storage.values() if resource.catalog_task_id.__eq__(catalog_task_id)]

    def list(self) -> [Resource]:
        return list(self.__resource_storage.values())


