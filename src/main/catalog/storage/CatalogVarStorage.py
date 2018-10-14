from abc import abstractmethod
from typing import Dict

from src.main.catalog.entity.CatalogVar import CatalogVar
from src.main.common.default.DefaultInterface import DefaultInterface


class CatalogVarStorage(DefaultInterface):
    @abstractmethod
    def insert(self, catalog_var: CatalogVar) -> None:
        pass

    @abstractmethod
    def get_by_name(self, name: str) -> CatalogVar:
        pass

    @abstractmethod
    def list_all(self) -> Dict:
        pass