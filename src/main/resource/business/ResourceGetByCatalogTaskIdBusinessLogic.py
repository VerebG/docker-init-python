from abc import abstractmethod

from src.main.common.default.DefaultInterface import DefaultInterface
from src.main.resource.entity.Resource import Resource


class ResourceGetByCatalogTaskIdBusinessLogic(DefaultInterface):
    @abstractmethod
    def get_by_catalog_task_id(self, catalog_task_id: str) -> [Resource]:
        pass