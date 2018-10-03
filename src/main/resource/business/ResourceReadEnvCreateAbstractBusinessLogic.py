from abc import abstractmethod

from src.main.common.default.DefaultInterface import DefaultInterface


class ResourceReadEnvCreateAbstractBusinessLogic(DefaultInterface):
    @abstractmethod
    def create_abstraction(self, resource_definition: {}):
        pass