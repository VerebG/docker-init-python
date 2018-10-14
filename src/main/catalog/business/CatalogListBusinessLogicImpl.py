from injector import singleton, inject

from src.main.catalog.business.CatalogListBusinessLogic import CatalogListBusinessLogic
from src.main.catalog.entity.Catalog import Catalog
from src.main.catalog.storage.CatalogStorage import CatalogStorage

@singleton
class CatalogListBusinessLogicImpl(CatalogListBusinessLogic):
    __catalog_storage: CatalogStorage

    @inject
    def __init__(self,
        catalog_storage: CatalogStorage
    ) -> None:
        self.__catalog_storage = catalog_storage

    def list(self) -> [Catalog]:
        return self.__catalog_storage.list()