from abc import abstractmethod

from src.main.catalog.entity.Catalog import Catalog
from src.main.common.default.DefaultInterface import DefaultInterface


class CatalogListBusinessLogic(DefaultInterface):
    @abstractmethod
    def list(self) -> [Catalog]:
        pass