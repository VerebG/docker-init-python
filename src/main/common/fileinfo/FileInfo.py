from grp import getgrgid
from pwd import getpwuid
from pathlib import Path
from os import stat, stat_result
from stat import S_IMODE


class FileInfo(object):
    __file_path: Path
    __file_stat: stat_result

    def __init__(self,
        file_path: str
    ) -> None:
        self.__file_path = Path(file_path)

        if not (self.__file_path.is_file() or self.__file_path.is_dir()):
            raise BaseException('Unable to get {0} info, because object is not found!'.format(self.__file_path))

        self.__file_stat = stat(self.__file_path.__str__())

    @property
    def owner(self) -> str:
        return getpwuid(self.__file_stat.st_uid).pw_name

    @property
    def owner_uid(self) -> int:
        return self.__file_stat.st_uid

    @property
    def group(self) -> str:
        return getgrgid(self.__file_stat.st_gid).gr_name

    @property
    def group_gid(self) -> int:
        return self.__file_stat.st_gid

    @property
    def mode(self) -> str:
        return "%04o" % S_IMODE(self.__file_stat.st_mode)
