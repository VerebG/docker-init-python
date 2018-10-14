from abc import abstractmethod

from src.main.catalog.entity.CatalogTask import CatalogTask
from src.main.common.default.DefaultInterface import DefaultInterface


class CatalogTaskGetByCatalogIdBusinessLogic(DefaultInterface):
    @abstractmethod
    def get_by_catalog_id(self, catalog_id: str) -> [CatalogTask]:
        pass