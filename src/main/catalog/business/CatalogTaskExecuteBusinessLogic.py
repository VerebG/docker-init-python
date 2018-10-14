from abc import abstractmethod

from src.main.catalog.entity.CatalogTaskAggregate import CatalogTaskAggregate
from src.main.common.default.DefaultInterface import DefaultInterface


class CatalogTaskExecuteBusinessLogic(DefaultInterface):
    @abstractmethod
    def execute(self, catalog_task_aggregate: CatalogTaskAggregate) -> None:
        pass