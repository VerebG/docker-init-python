from typing import Dict

from injector import singleton

from src.main.catalog.entity.CatalogVar import CatalogVar
from src.main.catalog.exception.CatalogVarAlreadyExistsException import CatalogVarAlreadyExistsException
from src.main.catalog.exception.CatalogVarNotFoundException import CatalogVarNotFoundException
from src.main.catalog.storage.CatalogVarStorage import CatalogVarStorage

@singleton
class DataMapperCatalogVar(CatalogVarStorage):
    __catalog_var_storage = dict()

    def insert(self, catalog_var: CatalogVar) -> None:
        if catalog_var.name in self.__catalog_var_storage:
            raise CatalogVarAlreadyExistsException(catalog_var.name)
        self.__catalog_var_storage.__setitem__(catalog_var.name, catalog_var.value)

    def get_by_name(self, name: str) -> CatalogVar:
        if not name in self.__catalog_var_storage:
            raise CatalogVarNotFoundException(name)
        return self.__catalog_var_storage.get(name)

    def list_all(self) -> Dict:
        return self.__catalog_var_storage

