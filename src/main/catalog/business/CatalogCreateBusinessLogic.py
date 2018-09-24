from abc import abstractmethod

from src.main.catalog.entity.Catalog import Catalog
from src.main.common.default.DefaultInterface import DefaultInterface

class CatalogCreateBusinessLogic(DefaultInterface):
    @abstractmethod
    def create(self, name: str) -> Catalog:
        pass