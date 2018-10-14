from abc import abstractmethod

from src.main.catalog.entity.CatalogVar import CatalogVar
from src.main.common.default.DefaultInterface import DefaultInterface


class CatalogVarCreateBusinessLogic(DefaultInterface):
    @abstractmethod
    def create(self, catalog_var: CatalogVar) -> None:
        pass

    @abstractmethod
    def get_by_name(self, name: str) -> CatalogVar:
        pass