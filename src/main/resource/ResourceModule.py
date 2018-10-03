from injector import Module, singleton

from src.main.resource.business.ResourceFileCreateAbstractionBusinessLogic import \
    ResourceFileCreateAbstractionBusinessLogic
from src.main.resource.business.ResourceFileCreateAbstractionBusinessLogicImpl import \
    ResourceFileCreateAbstractionBusinessLogicImpl
from src.main.resource.business.ResourceReadEnvCreateAbstractBusinessLogic import \
    ResourceReadEnvCreateAbstractBusinessLogic
from src.main.resource.business.ResourceReadEnvCreateAbstractBusinessLogicImpl import \
    ResourceReadEnvCreateAbstractBusinessLogicImpl
from src.main.resource.business.ResourceSelectorBusinessLogic import ResourceSelectorBusinessLogic
from src.main.resource.business.ResourceSelectorBusinessLogicImpl import ResourceSelectorBusinessLogicImpl
from src.main.resource.storage.DataMapperResource import DataMapperResource
from src.main.resource.storage.ResourceStorage import ResourceStorage


class ResourceModule(Module):
    def configure(self, binder):
        #region Business
        binder.bind(interface=ResourceSelectorBusinessLogic, to=ResourceSelectorBusinessLogicImpl)
        binder.bind(ResourceSelectorBusinessLogicImpl, scope=singleton)

        binder.bind(interface=ResourceFileCreateAbstractionBusinessLogic, to=ResourceFileCreateAbstractionBusinessLogicImpl)
        binder.bind(ResourceFileCreateAbstractionBusinessLogicImpl, scope=singleton)

        binder.bind(interface=ResourceReadEnvCreateAbstractBusinessLogic, to=ResourceReadEnvCreateAbstractBusinessLogicImpl)
        binder.bind(ResourceReadEnvCreateAbstractBusinessLogicImpl, scope=singleton)
        #endregion

        #region Storage
        binder.bind(interface=ResourceStorage, to=DataMapperResource)
        binder.bind(DataMapperResource, scope=singleton)
        #endregion