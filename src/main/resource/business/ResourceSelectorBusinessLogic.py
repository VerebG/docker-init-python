from abc import abstractmethod

from src.main.common.default.DefaultInterface import DefaultInterface


class ResourceSelectorBusinessLogic(DefaultInterface):
    @abstractmethod
    def get_resource_abstraction_create_business_logic(self, resource_type: str) -> DefaultInterface:
        pass
