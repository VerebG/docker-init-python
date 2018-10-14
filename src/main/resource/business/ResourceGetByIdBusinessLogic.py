from abc import abstractmethod

from src.main.common.default.DefaultInterface import DefaultInterface


class ResourceGetByIdBusinessLogic(DefaultInterface):
    @abstractmethod
    def get_by_id(self, id: str):
        pass