from logging import Logger
from pathlib import Path
from typing import Optional
from grp import getgrgid
from pwd import getpwuid, getpwnam

from src.main.resource.entity.ResourceFile import ResourceFile
from src.main.resource.helper import ResourceDefault


class ResourceFileCreateBusinessLogicImplement(object):
    __logger: Logger

    def __init__(self, logger: Logger) -> None:
        self.__logger = logger

    def create(self,
        name: Optional[str, None],
        state: Optional[str, None],
        path: Path,
        owner: Optional[str, None],
        group: Optional[str, None],
        mode: Optional[str, None],
        source: Optional[Path, None]
    ) -> ResourceFile:
        if name is None:
            name = '{0} state to {1}'.format(path, state)
            self.__logger.info('Name does not define, I\'ll generate to it')

        if not state is None:
            if not state in ['present', 'absent']:
                self.__logger.critical('{0} state is not valid! Please set to \'present\' or \'absent \'!'.format(state))
                exit(1)
        else:
            state = 'present'
            self.__logger.info('State field is empty, I set to \'present\'')

        if not path.is_file() or not path.is_dir():
            self.__logger.critical('{0} path is not exists in this system!'.format(path))
            exit(1)

        if not owner is None:
            try:
                getpwnam(owner).pw_uid
            except KeyError:
                self.__logger.critical('{0} user is not exists int this system!'.format(owner))
                exit(1)
        else:
            owner = ResourceDefault.RESOURCE_DEFAULT['file']['owner']
            self.__logger.info('Owner does not define for this resource, I set to \'root\'')