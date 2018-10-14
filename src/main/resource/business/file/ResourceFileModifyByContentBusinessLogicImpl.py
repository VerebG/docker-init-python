from injector import singleton, inject
from jinja2 import Template

from src.main.catalog.business.CatalogVarListAllBusinessLogic import CatalogVarListAllBusinessLogic
from src.main.resource.business.file.ResourceFileModifyByContentBusinessLogic import \
    ResourceFileModifyByContentBusinessLogic
from src.main.resource.entity.ResourceFile import ResourceFile


@singleton
class ResourceFileModifyByContentBusinessLogicImpl(ResourceFileModifyByContentBusinessLogic):
    __catalog_var_list_all_business_logic: CatalogVarListAllBusinessLogic

    @inject
    def __init__(self, catalog_var_list_all_business_logic: CatalogVarListAllBusinessLogic) -> None:
        self.__catalog_var_list_all_business_logic = catalog_var_list_all_business_logic

    def modify(self, resource_file: ResourceFile) -> None:

        with open(resource_file.source.__str__()) as file:
            template = Template(file.read())

        template.stream(self.__catalog_var_list_all_business_logic.list_all()).dump(resource_file.path.__str__(), encoding='UTF-8')

