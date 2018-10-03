from injector import singleton

from src.main.resource.business.ResourceReadEnvCreateAbstractBusinessLogic import \
    ResourceReadEnvCreateAbstractBusinessLogic

@singleton
class ResourceReadEnvCreateAbstractBusinessLogicImpl(ResourceReadEnvCreateAbstractBusinessLogic):
    def create_abstraction(self, resource_definition: {}):
        pass