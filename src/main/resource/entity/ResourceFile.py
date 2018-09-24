from pathlib import Path
from typing import Optional

from src.main.resource.entity.Resource import Resource

class ResourceFile(Resource):
    __path: Path
    __owner: str
    __group: str
    __mode: str
    __source: Path

    def __init__(self,
        name: str,
        state: str,
        path: Path,
        owner: str,
        group: str,
        mode: str,
        source: Path,
        checksum: str
    ) -> None:
        super().__init__(name, state, checksum)
        self.__path = path
        self.__owner = owner
        self.__group = group
        self.__mode = mode
        self.__source = source

    def __eq__(self, other):
        if isinstance(other, ResourceFile):
            return (
                (self.get_path() == other.get_path()) and
                (self.get_owner() == other.get_owner()) and
                (self.get_group() == other.get_group()) and
                (self.get_mode() == other.get_mode()) and
                (self.get_source() == other.get_source()) and
                (self.get_checksum() == other.get_checksum())
            )
        else:
            return False

    def get_path(self) -> Path:
        return self.__path

    def get_owner(self) -> str:
        return self.__owner

    def get_group(self) -> str:
        return self.__group

    def get_mode(self) -> str:
        return self.__mode

    def get_source(self) -> Path:
        return self.__source
