from abc import abstractmethod

from src.main.common.default.DefaultInterface import DefaultInterface


class CatalogPrepareToApplyBusinessLogic(DefaultInterface):
    @abstractmethod
    def prepare_to_apply(self, catalog_file: str) -> None:
        pass