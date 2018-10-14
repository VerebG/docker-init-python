from typing import Dict

from injector import singleton, inject

from src.main.catalog.business.CatalogVarListAllBusinessLogic import CatalogVarListAllBusinessLogic
from src.main.catalog.storage.CatalogVarStorage import CatalogVarStorage


@singleton
class CatalogVarListAllBusinessLogicImpl(CatalogVarListAllBusinessLogic):
    __catalog_var_storage: CatalogVarStorage

    @inject
    def __init__(self, catalog_var_storage: CatalogVarStorage) -> None:
        self.__catalog_var_storage = catalog_var_storage

    def list_all(self) -> Dict:
        return self.__catalog_var_storage.list_all()

