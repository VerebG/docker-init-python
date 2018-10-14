from abc import abstractmethod

from src.main.common.default.DefaultInterface import DefaultInterface


class CatalogExecuteBusinessLogic(DefaultInterface):
    @abstractmethod
    def execute(self) -> None:
        pass