from typing import Union

from injector import singleton, inject, Injector

from src.main.common.constant.Constant import Constant
from src.main.common.default.DefaultInterface import DefaultInterface
from src.main.resource.business.file.ResourceFileCreateAbstractionBusinessLogic import \
    ResourceFileCreateAbstractionBusinessLogic
from src.main.resource.business.ResourceSelectorBusinessLogic import ResourceSelectorBusinessLogic
from src.main.resource.entity.Resource import Resource


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
            resource_abstraction_create_business_logic = self.__constant.available_resource_types[resource_type]['abstraction']['create']
        except Exception:
            raise BaseException('{0} resource abstract create business logic not found'.format(resource_type))

        return self.__injector.get(resource_abstraction_create_business_logic)

    def get_resource_create_from_exist_business_logic(self, resource_type: Union[str, Resource]) -> DefaultInterface:
        try:
            return self.__injector.get(self.__constant.available_resource_types[resource_type]['from_exist'])
        except Exception:
            for resource_types in self.__constant.available_resource_types:
                if isinstance(resource_type, self.__constant.available_resource_types[resource_types]['entity']):
                    return self.__injector.get(self.__constant.available_resource_types[resource_types]['from_exist'])

        raise BaseException('Couldn\'t create {0} resource from exist object because business logic not found'.format(resource_type))

