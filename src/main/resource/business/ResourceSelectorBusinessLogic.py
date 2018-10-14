from abc import abstractmethod
from typing import Optional, Union

from src.main.common.default.DefaultInterface import DefaultInterface
from src.main.resource.entity.Resource import Resource


class ResourceSelectorBusinessLogic(DefaultInterface):
    @abstractmethod
    def get_resource_abstraction_create_business_logic(self, resource_type: str) -> DefaultInterface:
        pass

    @abstractmethod
    def get_resource_create_from_exist_business_logic(self, resource_type: Union[str, Resource]) -> DefaultInterface:
        pass
