from injector import singleton, inject, Injector

from src.main.common.constant.Constant import Constant
from src.main.common.default.DefaultInterface import DefaultInterface
from src.main.resource.business.ResourceFileCreateAbstractionBusinessLogic import \
    ResourceFileCreateAbstractionBusinessLogic
from src.main.resource.business.ResourceSelectorBusinessLogic import ResourceSelectorBusinessLogic

@singleton
class ResourceSelectorBusinessLogicImpl(ResourceSelectorBusinessLogic):
    __resource_file_create_abstration_business_logic: ResourceFileCreateAbstractionBusinessLogic
    __injector: Injector
    __constant: Constant

    @inject
    def __init__(self,
        resource_file_create_abstration_business_logic: ResourceFileCreateAbstractionBusinessLogic,
        injector: Injector,
        constant: Constant
    ) -> None:
        self.__injector = injector
        self.__constant = constant
        self.__resource_file_create_abstration_business_logic = resource_file_create_abstration_business_logic

    def get_resource_abstraction_create_business_logic(self, resource_type: str) -> DefaultInterface:
        try:
            resource_abstraction_create_business_logic = self.__constant.available_resource_types[resource_type]
        except Exception:
            raise BaseException('{0} resource abstract create business logic not found'.format(resource_type))

        return self.__injector.get(resource_abstraction_create_business_logic)