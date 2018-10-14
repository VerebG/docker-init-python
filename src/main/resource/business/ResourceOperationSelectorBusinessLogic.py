from abc import abstractmethod

from src.main.common.default.DefaultInterface import DefaultInterface
from src.main.resource.entity.Resource import Resource


class ResourceOperationSelectorBusinessLogic(DefaultInterface):
    @abstractmethod
    def get_resource_modify_operation_by_attribute(self,
        resource_type: Resource,
        resource_attribute: str
    ) -> DefaultInterface:
        pass

    @abstractmethod
    def get_resource_state_to_present(self, resource: Resource) -> DefaultInterface:
        pass

    @abstractmethod
    def get_resource_state_to_absent(self, resource: Resource) -> DefaultInterface:
        pass