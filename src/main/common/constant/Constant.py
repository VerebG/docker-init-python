from injector import singleton

from src.main.resource.business.file.ResourceFileAbsentStateBusinessLogic import ResourceFileAbsentStateBusinessLogic
from src.main.resource.business.file.ResourceFileCreateAbstractionBusinessLogic import \
    ResourceFileCreateAbstractionBusinessLogic
from src.main.resource.business.file.ResourceFileCreateFromExistBusinessLogic import \
    ResourceFileCreateFromExistBusinessLogic
from src.main.resource.business.file.ResourceFileModifyByContentBusinessLogic import \
    ResourceFileModifyByContentBusinessLogic
from src.main.resource.business.file.ResourceFileModifyByGroupBusinessLogic import \
    ResourceFileModifyByGroupBusinessLogic
from src.main.resource.business.file.ResourceFileModifyByModeBusinessLogic import ResourceFileModifyByModeBusinessLogic
from src.main.resource.business.file.ResourceFileModifyByOwnerBusinessLogic import \
    ResourceFileModifyByOwnerBusinessLogic
from src.main.resource.business.file.ResourceFilePresentStateBusinessLogic import ResourceFilePresentStateBusinessLogic
from src.main.resource.business.readenv.ResourceReadEnvCreateAbstractBusinessLogic import \
    ResourceReadEnvCreateAbstractBusinessLogic
from src.main.resource.business.readenv.ResourceReadEnvCreateFromExistBusinessLogic import \
    ResourceReadEnvCreateFromExistBusinessLogic
from src.main.resource.entity.ResourceFile import ResourceFile
from src.main.resource.entity.ResourceReadEnv import ResourceReadEnv


@singleton
class Constant(object):
    @property
    def available_resource_types(self):
        return {
            'file': {
                'entity': ResourceFile,
                'abstraction': {
                    'create': ResourceFileCreateAbstractionBusinessLogic
                },
                'from_exist': ResourceFileCreateFromExistBusinessLogic,
                'operation': {
                    'present': ResourceFilePresentStateBusinessLogic,
                    'absent': ResourceFileAbsentStateBusinessLogic,
                    'modify': {
                        'content': ResourceFileModifyByContentBusinessLogic,
                        'owner': ResourceFileModifyByOwnerBusinessLogic,
                        'group': ResourceFileModifyByGroupBusinessLogic,
                        'mode': ResourceFileModifyByModeBusinessLogic
                    },
                }
            },
            'readenv': {
                'entity': ResourceReadEnv,
                'abstraction': {
                    'create': ResourceReadEnvCreateAbstractBusinessLogic
                },
                'from_exist': ResourceReadEnvCreateFromExistBusinessLogic
            }
        }

    @property
    def catalog_task_available_fields(self):
        return {
            'name': {
                'require': False,
                'default': '{{ id }}'
            },
            'register': {
                'require': False,
                'default': None
            },
        }
