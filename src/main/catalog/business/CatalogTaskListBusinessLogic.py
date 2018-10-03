from abc import abstractmethod

from src.main.catalog.entity.CatalogTask import CatalogTask
from src.main.common.default.DefaultInterface import DefaultInterface


class CatalogTaskListBusinessLogic(DefaultInterface):
    @abstractmethod
    def list(self) -> [CatalogTask]:
        pass