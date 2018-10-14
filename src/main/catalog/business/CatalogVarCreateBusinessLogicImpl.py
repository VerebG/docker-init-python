from injector import singleton, inject

from src.main.catalog.business.CatalogVarCreateBusinessLogic import CatalogVarCreateBusinessLogic
from src.main.catalog.entity.CatalogVar import CatalogVar
from src.main.catalog.storage.CatalogVarStorage import CatalogVarStorage


@singleton
class CatalogVarCreateBusinessLogicImpl(CatalogVarCreateBusinessLogic):
    __catalog_var_storage: CatalogVarStorage

    @inject
    def __init__(self,
        catalog_var_storage: CatalogVarStorage
    ) -> None:
        self.__catalog_var_storage = catalog_var_storage

    def create(self, catalog_var: CatalogVar) -> None:
        self.__catalog_var_storage.insert(catalog_var)

    def get_by_name(self, name: str) -> CatalogVar:
        return self.__catalog_var_storage.get_by_name(name)


