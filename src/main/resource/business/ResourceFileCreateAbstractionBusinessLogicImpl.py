from grp import getgrnam
from hashlib import sha256
from pathlib import Path
from pwd import getpwnam
from injector import singleton, inject

from src.main.common.random.RandomIdGenerator import RandomIdGenerator
from src.main.common.logging.AppLogger import AppLogger
from src.main.resource.business.ResourceFileCreateAbstractionBusinessLogic import \
    ResourceFileCreateAbstractionBusinessLogic
from src.main.resource.entity.ResourceFile import ResourceFile


@singleton
class ResourceFileCreateAbstractionBusinessLogicImpl(ResourceFileCreateAbstractionBusinessLogic):
    __logger: AppLogger
    __random_id_generator: RandomIdGenerator

    @inject
    def __init__(self,
        logger: AppLogger,
        random_id_generator: RandomIdGenerator
    ) -> None:
        self.__logger = logger
        self.__random_id_generator = random_id_generator

    def create_abstraction(self,
        resource_definition: {},
        catalog_task_id: str
    ) -> ResourceFile:
        self.__logger.format('%(levelname)s: /Catalog[%(catalog_name)s]/Task[%(catalog_task_name)s]/File[Unknow]: %(message)s')

        if 'path' in resource_definition:
            resource_definition['path'] = Path(resource_definition['path'])
        else:
            self.__logger.critical('\'path\' paramater must be filled!')

        self.__logger.catalog_task_resource_name = resource_definition['path'].__str__()
        self.__logger.format('%(levelname)s: /Catalog[%(catalog_name)s]/Task[%(catalog_task_name)s]/File[%(catalog_task_resource_name)s]: %(message)s')

        if not 'state' in resource_definition:
            resource_definition['state'] = 'present'
            self.__logger.info('State field is empty, I set to \'present\'')
        elif not resource_definition['state'] in ['present', 'absent']:
            self.__logger.critical('{0} state is not valid! Please set to \'present\' or \'absent \'!'.format(
                resource_definition['state']))

        if resource_definition['state'].__eq__('present'):

            if 'owner' in resource_definition:
                try:
                    resource_definition['owner'] = getpwnam(resource_definition['owner']).pw_uid
                except KeyError:
                    self.__logger.critical('{0} user is not exists int this system!'.format(resource_definition['owner']))
            else:
                resource_definition['owner'] = '0'
                self.__logger.info('Owner does not define for this resource, I set to \'root\'')

            if 'group' in resource_definition:
                try:
                    resource_definition['group'] = getgrnam(resource_definition['group'])
                except KeyError:
                    self.__logger.critical('{0} group is not exists int this system!'.format(resource_definition['group']))
            else:
                resource_definition['owner'] = '0'
                self.__logger.info('Group does not define for this resource, I set to \'root\'')

            if not 'mode' in resource_definition:
                resource_definition['mode'] = '0644'
                self.__logger.info('Mode does not define for this resource, I set to 0644!')

            if 'source' in resource_definition:
                resource_definition['source'] = Path(resource_definition['source'])
            else:
                self.__logger.critical('\'source\' paramater must be filled!')

            resource_definition['source_file_checksum'] = sha256(open(resource_definition['source'],'rb').read()).hexdigest()

        return ResourceFile(
            self.__random_id_generator.get(),
            catalog_task_id,
            resource_definition.get('state'),
            resource_definition.get('path'),
            resource_definition.get('owner', None),
            resource_definition.get('group', None),
            resource_definition.get('mode', None),
            resource_definition.get('source', None),
            resource_definition.get('source_file_checksum', None)
        )



