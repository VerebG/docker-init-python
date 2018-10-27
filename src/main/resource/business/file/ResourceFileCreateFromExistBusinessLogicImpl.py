from injector import singleton, inject
from hashlib import sha256

from jinja2 import Template

from src.main.catalog.business.CatalogVarListAllBusinessLogic import CatalogVarListAllBusinessLogic
from src.main.common.fileinfo.FileInfo import FileInfo
from src.main.resource.business.file.ResourceFileCreateFromExistBusinessLogic import \
    ResourceFileCreateFromExistBusinessLogic
from src.main.resource.entity.ResourceFile import ResourceFile

@singleton
class ResourceFileCreateFromExistBusinessLogicImpl(ResourceFileCreateFromExistBusinessLogic):
    __catalog_var_list_all_business_logic: CatalogVarListAllBusinessLogic

    @inject
    def __init__(self, catalog_var_list_all_business_logic: CatalogVarListAllBusinessLogic) -> None:
        self.__catalog_var_list_all_business_logic = catalog_var_list_all_business_logic

    def create_from_exist(self,
        resource_file_abstraction: ResourceFile
    ) -> ResourceFile:
        if resource_file_abstraction.path.is_file():
            __file_info = FileInfo(resource_file_abstraction.path.__str__())
            __source_content_checksum = None

            if not resource_file_abstraction.source in [None, '']:
                with open(resource_file_abstraction.source.__str__()) as file:
                    template = Template(file.read())
                __source_content_checksum = sha256(template.render(self.__catalog_var_list_all_business_logic.list_all(), 'r', encoding="utf-8").encode('UTF-8')).hexdigest()

            return ResourceFile(
                '',
                '',
                'present',
                resource_file_abstraction.path,
                __file_info.owner_uid,
                __file_info.group_gid,
                __file_info.mode,
                None,
                __source_content_checksum
            )
        else:
            return ResourceFile(
                '',
                '',
                'absent',
                resource_file_abstraction.path,
                None,
                None,
                None,
                None,
                None
            )