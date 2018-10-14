from injector import Module, singleton

from src.main.catalog.business.CatalogCreateBusinessLogic import CatalogCreateBusinessLogic
from src.main.catalog.business.CatalogCreateBusinessLogicImpl import CatalogCreateBusinessLogicImpl
from src.main.catalog.business.CatalogExecuteBusinessLogic import CatalogExecuteBusinessLogic
from src.main.catalog.business.CatalogExecuteBusinessLogicImpl import CatalogExecuteBusinessLogicImpl
from src.main.catalog.business.CatalogListBusinessLogic import CatalogListBusinessLogic
from src.main.catalog.business.CatalogListBusinessLogicImpl import CatalogListBusinessLogicImpl
from src.main.catalog.business.CatalogTaskCreateBusinessLogic import CatalogTaskCreateBusinessLogic
from src.main.catalog.business.CatalogTaskCreateBusinessLogicImpl import CatalogTaskCreateBusinessLogicImpl
from src.main.catalog.business.CatalogTaskExecuteBusinessLogic import CatalogTaskExecuteBusinessLogic
from src.main.catalog.business.CatalogTaskExecuteBusinessLogicImpl import CatalogTaskExecuteBusinessLogicImpl
from src.main.catalog.business.CatalogTaskGetByCatalogIdBusinessLogic import CatalogTaskGetByCatalogIdBusinessLogic
from src.main.catalog.business.CatalogTaskGetByCatalogIdBusinessLogicImpl import \
    CatalogTaskGetByCatalogIdBusinessLogicImpl
from src.main.catalog.business.CatalogTaskListBusinessLogic import CatalogTaskListBusinessLogic
from src.main.catalog.business.CatalogTaskListBusinessLogicImpl import CatalogTaskListBusinessLogicImpl
from src.main.catalog.business.CatalogVarCreateBusinessLogic import CatalogVarCreateBusinessLogic
from src.main.catalog.business.CatalogVarCreateBusinessLogicImpl import CatalogVarCreateBusinessLogicImpl
from src.main.catalog.business.CatalogVarListAllBusinessLogic import CatalogVarListAllBusinessLogic
from src.main.catalog.business.CatalogVarListAllBusinessLogicImpl import CatalogVarListAllBusinessLogicImpl
from src.main.catalog.storage.CatalogStorage import CatalogStorage
from src.main.catalog.storage.CatalogTaskStorage import CatalogTaskStorage
from src.main.catalog.storage.CatalogVarStorage import CatalogVarStorage
from src.main.catalog.storage.DataMapperCatalog import DataMapperCatalog
from src.main.catalog.storage.DataMapperCatalogTask import DataMapperCatalogTask
from src.main.catalog.storage.DataMapperCatalogVar import DataMapperCatalogVar


class CatalogModule(Module):
    def configure(self, binder):

        #region Business
        binder.bind(interface=CatalogCreateBusinessLogic, to=CatalogCreateBusinessLogicImpl)
        binder.bind(CatalogCreateBusinessLogicImpl, scope=singleton)
        binder.bind(interface=CatalogListBusinessLogic, to=CatalogListBusinessLogicImpl)
        binder.bind(CatalogListBusinessLogicImpl)
        binder.bind(interface=CatalogExecuteBusinessLogic, to=CatalogExecuteBusinessLogicImpl)
        binder.bind(CatalogExecuteBusinessLogicImpl, scope=singleton)

        binder.bind(interface=CatalogTaskCreateBusinessLogic, to=CatalogTaskCreateBusinessLogicImpl)
        binder.bind(CatalogTaskCreateBusinessLogicImpl, scope=singleton)
        binder.bind(interface=CatalogTaskListBusinessLogic, to=CatalogTaskListBusinessLogicImpl)
        binder.bind(CatalogTaskListBusinessLogicImpl, scope=singleton)
        binder.bind(interface=CatalogTaskGetByCatalogIdBusinessLogic, to=CatalogTaskGetByCatalogIdBusinessLogicImpl)
        binder.bind(CatalogTaskGetByCatalogIdBusinessLogicImpl, scope=singleton)
        binder.bind(interface=CatalogTaskExecuteBusinessLogic, to=CatalogTaskExecuteBusinessLogicImpl)
        binder.bind(CatalogTaskExecuteBusinessLogicImpl, scope=singleton)

        binder.bind(interface=CatalogVarCreateBusinessLogic, to=CatalogVarCreateBusinessLogicImpl)
        binder.bind(CatalogVarCreateBusinessLogicImpl, scope=singleton)
        binder.bind(interface=CatalogVarListAllBusinessLogic, to=CatalogVarListAllBusinessLogicImpl)
        binder.bind(CatalogVarListAllBusinessLogicImpl, scope=singleton)
        #endregion

        #region Storage
        binder.bind(interface=CatalogStorage, to=DataMapperCatalog)
        binder.bind(DataMapperCatalog, scope=singleton)

        binder.bind(interface=CatalogTaskStorage, to=DataMapperCatalogTask)
        binder.bind(DataMapperCatalogTask, scope=singleton)

        binder.bind(interface=CatalogVarStorage, to=DataMapperCatalogVar)
        binder.bind(DataMapperCatalogVar, scope=singleton)
        #endregion