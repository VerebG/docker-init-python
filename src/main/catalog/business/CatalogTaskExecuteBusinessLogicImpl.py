from injector import singleton, inject

from src.main.catalog.business.CatalogTaskExecuteBusinessLogic import CatalogTaskExecuteBusinessLogic
from src.main.catalog.business.CatalogVarCreateBusinessLogic import CatalogVarCreateBusinessLogic
from src.main.catalog.entity.CatalogTaskAggregate import CatalogTaskAggregate
from src.main.catalog.entity.CatalogVar import CatalogVar
from src.main.resource.business.ResourceOperationSelectorBusinessLogic import ResourceOperationSelectorBusinessLogic
from src.main.resource.business.ResourceSelectorBusinessLogic import ResourceSelectorBusinessLogic


@singleton
class CatalogTaskExecuteBusinessLogicImpl(CatalogTaskExecuteBusinessLogic):
    __resource_selector_business_logic: ResourceSelectorBusinessLogic
    __catalog_var_create_business_logic: CatalogVarCreateBusinessLogic
    __resource_operation_selector_business_logic: ResourceOperationSelectorBusinessLogic

    @inject
    def __init__(self,
        resource_selector_business_logic: ResourceSelectorBusinessLogic,
        catalog_var_create_business_logic: CatalogVarCreateBusinessLogic,
        resource_operation_selector_business_logic: ResourceOperationSelectorBusinessLogic
    ) -> None:
        self.__resource_selector_business_logic = resource_selector_business_logic
        self.__catalog_var_create_business_logic = catalog_var_create_business_logic
        self.__resource_operation_selector_business_logic = resource_operation_selector_business_logic

    def execute(self, catalog_task_aggregate: CatalogTaskAggregate) -> None:
        for resource in catalog_task_aggregate.resources:
            __exist_resource = self.__resource_selector_business_logic.get_resource_create_from_exist_business_logic(resource).create_from_exist(resource)

            if resource.state.__eq__('present'):
                if __exist_resource.state.__eq__('present'):
                    for what_should_i_change in resource.__eq__(__exist_resource):
                        field, value = what_should_i_change
                        self.__resource_operation_selector_business_logic.get_resource_modify_operation_by_attribute(resource, field).modify(resource)
                elif __exist_resource.state is 'absent':
                        self.__resource_operation_selector_business_logic.get_resource_state_to_present(resource).present_state(resource)
            elif resource.state.__eq__('absent'):
                if __exist_resource.state is 'present':
                    self.__resource_operation_selector_business_logic.get_resource_state_to_absent(resource).absent_state(resource)
            elif resource.state.__eq__('stateless'):
                pass #not do


            if not catalog_task_aggregate.register is None and not __exist_resource.can_register in [None, '']:
                self.__catalog_var_create_business_logic.create(
                    CatalogVar(
                        catalog_task_aggregate.register,
                        __exist_resource.can_register
                    )
                )
