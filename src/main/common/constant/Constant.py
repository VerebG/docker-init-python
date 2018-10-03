from injector import singleton

from src.main.resource.business.ResourceFileCreateAbstractionBusinessLogic import \
    ResourceFileCreateAbstractionBusinessLogic
from src.main.resource.business.ResourceReadEnvCreateAbstractBusinessLogic import \
    ResourceReadEnvCreateAbstractBusinessLogic
from src.main.resource.entity.Resource import Resource


@singleton
class Constant(object):
    @property
    def __resource_global_fields(self):
        return {
            'state': {
                'require': False,
                'default': Resource.PRESENT
            },
        }

    @property
    def available_resource_types(self):
        return {
            'file': ResourceFileCreateAbstractionBusinessLogic,
            'readenv': ResourceReadEnvCreateAbstractBusinessLogic
        }

    @property
    def catalog_task_available_fields(self):
        return {
            'name': {
                'require': False,
                'default': '%(id)'
            },
            'register': {
                'require': False,
                'default': None
            },
        }
