from injector import inject, singleton

from src.main.catalog.business.CatalogCreateBusinessLogic import CatalogCreateBusinessLogic
from src.main.catalog.entity.Catalog import Catalog
from src.main.catalog.storage.CatalogStorage import CatalogStorage
from src.main.common.random.RandomIdGenerator import RandomIdGenerator

@singleton
class CatalogCreateBusinessLogicImpl(CatalogCreateBusinessLogic):
    __catalog_storage: CatalogStorage
    __random_id_generator: RandomIdGenerator

    @inject
    def __init__(self,
        random_id_generator: RandomIdGenerator,
        catalog_storage: CatalogStorage
    ) -> None:
        self.__random_id_generator = random_id_generator
        self.__catalog_storage = catalog_storage

    def create(self, name: str) -> Catalog:
        __catalog = Catalog(self.__random_id_generator.get(), name)

        self.__catalog_storage.insert(__catalog)

        return __catalog