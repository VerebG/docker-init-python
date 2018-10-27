from grp import getgrnam
from hashlib import sha256
from pathlib import Path
from pwd import getpwnam
from stat import S_IMODE

from injector import singleton, inject
from jinja2 import Template

from src.main.catalog.business.CatalogVarListAllBusinessLogic import CatalogVarListAllBusinessLogic
from src.main.common.random.RandomIdGenerator import RandomIdGenerator
from src.main.common.logging.AppLogger import AppLogger
from src.main.resource.business.file.ResourceFileCreateAbstractionBusinessLogic import \
    ResourceFileCreateAbstractionBusinessLogic
from src.main.resource.entity.ResourceFile import ResourceFile
from src.main.resource.storage.ResourceStorage import ResourceStorage


@singleton
class ResourceFileCreateAbstractionBusinessLogicImpl(ResourceFileCreateAbstractionBusinessLogic):
    __logger: AppLogger
    __random_id_generator: RandomIdGenerator
    __resource_storage: ResourceStorage

    @inject
    def __init__(self,
        logger: AppLogger,
        random_id_generator: RandomIdGenerator,
        resource_storage: ResourceStorage
    ) -> None:
        self.__logger = logger
        self.__random_id_generator = random_id_generator
        self.__resource_storage = resource_storage

    def create_abstraction(self,
        resource_definition: {},
        catalog_task_id: str
    ) -> ResourceFile:
        self.__logger.catalog_task_resource_name = 'Unknow'
        self.__logger.format('%(levelname)s: /Catalog[%(catalog_name)s]/Task[%(catalog_task_name)s]/File[%(catalog_task_resource_name)s]: %(message)s')

        if 'path' in resource_definition:
            resource_definition['path'] = Path(resource_definition['path'])
            if resource_definition['path'].is_file():
                resource_definition['content_checksum'] = sha256(open(resource_definition['path'].__str__(), 'r', encoding="utf-8").read().encode('UTF-8')).hexdigest()
        else:
            self.__logger.critical('\'path\' paramater must be filled!')

        self.__logger.catalog_task_resource_name = resource_definition['path'].__str__()

        if not 'state' in resource_definition:
            resource_definition['state'] = 'present'
            self.__logger.info('State field is empty, I set to \'present\'')
        elif not resource_definition['state'] in ['present', 'absent']:
            self.__logger.critical('{0} state is not valid! Please set to \'present\' or \'absent \'!'.format(
                resource_definition['state']))

        if resource_definition['state'].__eq__('present'):

            if not 'owner' in resource_definition:
                resource_definition['owner'] = 0
                self.__logger.info('Owner does not define for this resource, I set to \'root\'')
            else:
                try:
                    resource_definition['owner'] = getpwnam(resource_definition['owner']).pw_uid
                except KeyError:
                    self.__logger.critical('{0} user not found in this system'.format(resource_definition['owner']))

            if not 'group' in resource_definition:
                resource_definition['group'] = 0
                self.__logger.info('Group does not define for this resource, I set to \'root\'')
            else:
                try:
                    resource_definition['group'] = getgrnam(resource_definition['group']).gr_gid
                except KeyError:
                    self.__logger.critical('{0} group not found in this system'.format(resource_definition['group']))

            if 'mode' in resource_definition:
                resource_definition['mode'] = "%04o" % S_IMODE(resource_definition['mode'])
            else:
                resource_definition['mode'] = '0600'
                self.__logger.info('Mode does not define for this resource, I set to 0600!')

            if 'source' in resource_definition:
                if not Path(resource_definition['source']).is_file():
                    self.__logger.critical('Source file not found')
            else:
                self.__logger.critical('\'source\' paramater must be filled!')

        __resource_file = ResourceFile(
            self.__random_id_generator.get(),
            catalog_task_id,
            resource_definition.get('state'),
            resource_definition.get('path'),
            resource_definition.get('owner', None),
            resource_definition.get('group', None),
            resource_definition.get('mode', None),
            resource_definition.get('source', None),
            resource_definition.get('content_checksum', None)
        )

        self.__resource_storage.insert(__resource_file)

        return __resource_file



