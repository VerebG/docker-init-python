from abc import abstractmethod

from src.main.common.default.DefaultInterface import DefaultInterface

class CatalogCreateBusinessLogic(DefaultInterface):
    @abstractmethod
    def create(self, catalog_file: str):
        pass