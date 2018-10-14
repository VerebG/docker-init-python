from injector import Module, singleton

from src.main.resource.business.ResourceOperationSelectorBusinessLogic import ResourceOperationSelectorBusinessLogic
from src.main.resource.business.ResourceOperationSelectorBusinessLogicImpl import \
    ResourceOperationSelectorBusinessLogicImpl
from src.main.resource.business.file.ResourceFileAbsentStateBusinessLogic import ResourceFileAbsentStateBusinessLogic
from src.main.resource.business.file.ResourceFileAbsentStateBusinessLogicImpl import \
    ResourceFileAbsentStateBusinessLogicImpl
from src.main.resource.business.file.ResourceFileCreateAbstractionBusinessLogic import \
    ResourceFileCreateAbstractionBusinessLogic
from src.main.resource.business.file.ResourceFileCreateAbstractionBusinessLogicImpl import \
    ResourceFileCreateAbstractionBusinessLogicImpl
from src.main.resource.business.ResourceGetByCatalogTaskIdBusinessLogic import ResourceGetByCatalogTaskIdBusinessLogic
from src.main.resource.business.ResourceGetByCatalogTaskIdBusinessLogicImpl import \
    ResourceGetByCatalogTaskIdBusinessLogicImpl
from src.main.resource.business.ResourceGetByIdBusinessLogic import ResourceGetByIdBusinessLogic
from src.main.resource.business.ResourceGetByIdBusinessLogicImpl import ResourceGetByIdBusinessLogicImpl
from src.main.resource.business.ResourceListBusinessLogic import ResourceListBusinessLogic
from src.main.resource.business.ResourceListBusinessLogicImpl import ResourceListBusinessLogicImpl
from src.main.resource.business.file.ResourceFileCreateFromExistBusinessLogic import \
    ResourceFileCreateFromExistBusinessLogic
from src.main.resource.business.file.ResourceFileCreateFromExistBusinessLogicImpl import \
    ResourceFileCreateFromExistBusinessLogicImpl
from src.main.resource.business.file.ResourceFileModifyByContentBusinessLogic import \
    ResourceFileModifyByContentBusinessLogic
from src.main.resource.business.file.ResourceFileModifyByContentBusinessLogicImpl import \
    ResourceFileModifyByContentBusinessLogicImpl
from src.main.resource.business.file.ResourceFileModifyByGroupBusinessLogic import \
    ResourceFileModifyByGroupBusinessLogic
from src.main.resource.business.file.ResourceFileModifyByGroupBusinessLogicImpl import \
    ResourceFileModifyByGroupBusinessLogicImpl
from src.main.resource.business.file.ResourceFileModifyByModeBusinessLogic import ResourceFileModifyByModeBusinessLogic
from src.main.resource.business.file.ResourceFileModifyByModeBusinessLogicImpl import \
    ResourceFileModifyByModeBusinessLogicImpl
from src.main.resource.business.file.ResourceFileModifyByOwnerBusinessLogic import \
    ResourceFileModifyByOwnerBusinessLogic
from src.main.resource.business.file.ResourceFileModifyByOwnerBusinessLogicImpl import \
    ResourceFileModifyByOwnerBusinessLogicImpl
from src.main.resource.business.file.ResourceFilePresentStateBusinessLogic import ResourceFilePresentStateBusinessLogic
from src.main.resource.business.file.ResourceFilePresentStateBusinessLogicImpl import \
    ResourceFilePresentStateBusinessLogicImpl
from src.main.resource.business.readenv.ResourceReadEnvCreateAbstractBusinessLogic import \
    ResourceReadEnvCreateAbstractBusinessLogic
from src.main.resource.business.readenv.ResourceReadEnvCreateAbstractBusinessLogicImpl import \
    ResourceReadEnvCreateAbstractBusinessLogicImpl
from src.main.resource.business.ResourceSelectorBusinessLogic import ResourceSelectorBusinessLogic
from src.main.resource.business.ResourceSelectorBusinessLogicImpl import ResourceSelectorBusinessLogicImpl
from src.main.resource.business.readenv.ResourceReadEnvCreateFromExistBusinessLogic import \
    ResourceReadEnvCreateFromExistBusinessLogic
from src.main.resource.business.readenv.ResourceReadEnvCreateFromExistBusinessLogicImpl import \
    ResourceReadEnvCreateFromExistBusinessLogicImpl
from src.main.resource.storage.DataMapperResource import DataMapperResource
from src.main.resource.storage.ResourceStorage import ResourceStorage


class ResourceModule(Module):
    def configure(self, binder):
        #region Business
        binder.bind(interface=ResourceSelectorBusinessLogic, to=ResourceSelectorBusinessLogicImpl)
        binder.bind(ResourceSelectorBusinessLogicImpl, scope=singleton)
        binder.bind(interface=ResourceListBusinessLogic, to=ResourceListBusinessLogicImpl)
        binder.bind(ResourceListBusinessLogicImpl, scope=singleton)
        binder.bind(interface=ResourceGetByIdBusinessLogic, to=ResourceGetByIdBusinessLogicImpl)
        binder.bind(ResourceGetByIdBusinessLogicImpl, scope=singleton)
        binder.bind(interface=ResourceGetByCatalogTaskIdBusinessLogic, to=ResourceGetByCatalogTaskIdBusinessLogicImpl)
        binder.bind(ResourceGetByCatalogTaskIdBusinessLogicImpl, scope=singleton)
        binder.bind(interface=ResourceOperationSelectorBusinessLogic, to=ResourceOperationSelectorBusinessLogicImpl)
        binder.bind(ResourceOperationSelectorBusinessLogicImpl, scope=singleton)

        binder.bind(interface=ResourceFileCreateAbstractionBusinessLogic, to=ResourceFileCreateAbstractionBusinessLogicImpl)
        binder.bind(ResourceFileCreateAbstractionBusinessLogicImpl, scope=singleton)
        binder.bind(interface=ResourceFileCreateFromExistBusinessLogic, to=ResourceFileCreateFromExistBusinessLogicImpl)
        binder.bind(ResourceFileCreateFromExistBusinessLogicImpl, scope=singleton)
        binder.bind(interface=ResourceFileModifyByContentBusinessLogic, to=ResourceFileModifyByContentBusinessLogicImpl)
        binder.bind(ResourceFileModifyByContentBusinessLogicImpl, scope=singleton)
        binder.bind(interface=ResourceFileModifyByOwnerBusinessLogic, to=ResourceFileModifyByOwnerBusinessLogicImpl)
        binder.bind(ResourceFileModifyByOwnerBusinessLogicImpl, scope=singleton)
        binder.bind(interface=ResourceFileModifyByModeBusinessLogic, to=ResourceFileModifyByModeBusinessLogicImpl)
        binder.bind(ResourceFileModifyByModeBusinessLogicImpl, scope=singleton)
        binder.bind(interface=ResourceFileModifyByGroupBusinessLogic, to=ResourceFileModifyByGroupBusinessLogicImpl)
        binder.bind(ResourceFileModifyByGroupBusinessLogicImpl, scope=singleton)
        binder.bind(interface=ResourceFilePresentStateBusinessLogic, to=ResourceFilePresentStateBusinessLogicImpl)
        binder.bind(ResourceFilePresentStateBusinessLogicImpl, scope=singleton)
        binder.bind(interface=ResourceFileAbsentStateBusinessLogic, to=ResourceFileAbsentStateBusinessLogicImpl)
        binder.bind(ResourceFileAbsentStateBusinessLogicImpl, scope=singleton)

        binder.bind(interface=ResourceReadEnvCreateFromExistBusinessLogic, to=ResourceReadEnvCreateFromExistBusinessLogicImpl)
        binder.bind(ResourceReadEnvCreateFromExistBusinessLogicImpl, scope=singleton)
        binder.bind(interface=ResourceReadEnvCreateAbstractBusinessLogic, to=ResourceReadEnvCreateAbstractBusinessLogicImpl)
        binder.bind(ResourceReadEnvCreateAbstractBusinessLogicImpl, scope=singleton)
        #endregion

        #region Storage
        binder.bind(interface=ResourceStorage, to=DataMapperResource)
        binder.bind(DataMapperResource, scope=singleton)
        #endregion