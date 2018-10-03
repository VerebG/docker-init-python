from abc import abstractmethod

from src.main.catalog.entity.CatalogTask import CatalogTask
from src.main.common.default.DefaultInterface import DefaultInterface
from src.main.resource.entity.Resource import Resource


class CatalogTaskCreateBusinessLogic(DefaultInterface):
    @abstractmethod
    def create(self,
        name: str,
        resource_definition: Resource,
        register: str
    ) -> CatalogTask:
        pass