from injector import singleton, inject, Injector

from src.main.common.constant.Constant import Constant
from src.main.common.default.DefaultInterface import DefaultInterface
from src.main.resource.business.ResourceOperationSelectorBusinessLogic import ResourceOperationSelectorBusinessLogic
from src.main.resource.entity.Resource import Resource


@singleton
class ResourceOperationSelectorBusinessLogicImpl(ResourceOperationSelectorBusinessLogic):
    __constant: Constant
    __injector: Injector

    @inject
    def __init__(self,
        constant: Constant,
        injector: Injector
    ) -> None:
        self.__constant = constant
        self.__injector = injector

    def get_resource_modify_operation_by_attribute(self,
        resource: Resource,
        resource_attribute: str
    ) -> DefaultInterface:
        for resource_type in self.__constant.available_resource_types:
            if isinstance(resource, self.__constant.available_resource_types[resource_type]['entity']):
                if self.__constant.available_resource_types[resource_type]['operation']['modify'][resource_attribute]:
                    return self.__injector.get(self.__constant.available_resource_types[resource_type]['operation']['modify'][resource_attribute])
                else:
                    raise BaseException('{0} resource can\'t modify its {1} attr'.format(resource_type, resource_attribute))

        raise BaseException('{0} resource not found its {1} attribute modification business logic'.format(resource, resource_attribute))

    def get_resource_state_to_present(self, resource: Resource) -> DefaultInterface:
        for resource_type in self.__constant.available_resource_types:
            if isinstance(resource, self.__constant.available_resource_types[resource_type]['entity']):
                if self.__constant.available_resource_types[resource_type]['operation']['present']:
                    return self.__injector.get(self.__constant.available_resource_types[resource_type]['operation']['present'])

        raise BaseException('{0} not have present business logic '.format(resource.__class__.__name__))

    def get_resource_state_to_absent(self, resource: Resource) -> DefaultInterface:
        for resource_type in self.__constant.available_resource_types:
            if isinstance(resource, self.__constant.available_resource_types[resource_type]['entity']):
                if self.__constant.available_resource_types[resource_type]['operation']['absent']:
                    return self.__injector.get(self.__constant.available_resource_types[resource_type]['operation']['absent'])

        raise BaseException('{0} not have absent business logic '.format(resource.__class__.__name__))

