from injector import Module, singleton

from src.main.catalog.business.CatalogCreateBusinessLogic import CatalogCreateBusinessLogic
from src.main.catalog.business.CatalogCreateBusinessLogicImpl import CatalogCreateBusinessLogicImpl
from src.main.catalog.business.CatalogPrepareToApplyBusinessLogic import CatalogPrepareToApplyBusinessLogic
from src.main.catalog.business.CatalogPrepareToApplyBusinessLogicImpl import CatalogPrepareToApplyBusinessLogicImpl
from src.main.catalog.business.CatalogTaskCreateBusinessLogic import CatalogTaskCreateBusinessLogic
from src.main.catalog.business.CatalogTaskCreateBusinessLogicImpl import CatalogTaskCreateBusinessLogicImpl
from src.main.catalog.business.CatalogTaskListBusinessLogic import CatalogTaskListBusinessLogic
from src.main.catalog.business.CatalogTaskListBusinessLogicImpl import CatalogTaskListBusinessLogicImpl
from src.main.catalog.storage.CatalogStorage import CatalogStorage
from src.main.catalog.storage.CatalogTaskStorage import CatalogTaskStorage
from src.main.catalog.storage.DataMapperCatalog import DataMapperCatalog
from src.main.catalog.storage.DataMapperCatalogTask import DataMapperCatalogTask


class CatalogModule(Module):
    def configure(self, binder):

        #region Business
        binder.bind(interface=CatalogPrepareToApplyBusinessLogic, to=CatalogPrepareToApplyBusinessLogicImpl)
        binder.bind(CatalogPrepareToApplyBusinessLogicImpl, scope=singleton)

        binder.bind(interface=CatalogCreateBusinessLogic, to=CatalogCreateBusinessLogicImpl)
        binder.bind(CatalogCreateBusinessLogicImpl, scope=singleton)

        binder.bind(interface=CatalogTaskCreateBusinessLogic, to=CatalogTaskCreateBusinessLogicImpl)
        binder.bind(CatalogTaskCreateBusinessLogicImpl, scope=singleton)
        binder.bind(interface=CatalogTaskListBusinessLogic, to=CatalogTaskListBusinessLogicImpl)
        binder.bind(CatalogTaskListBusinessLogicImpl, scope=singleton)
        #endregion

        #region Storage
        binder.bind(interface=CatalogStorage, to=DataMapperCatalog)
        binder.bind(DataMapperCatalog, scope=singleton)

        binder.bind(interface=CatalogTaskStorage, to=DataMapperCatalogTask)
        binder.bind(DataMapperCatalogTask, scope=singleton)
        #endregion