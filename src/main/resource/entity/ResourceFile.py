from pathlib import Path
from typing import Optional

from src.main.resource.entity.Resource import Resource

class ResourceFile(Resource):
    __path: Path
    __owner: str
    __group: str
    __mode: str
    __source: Path
    __checksum: str

    def __init__(self,
        id: str,
        catalog_task_id: str,
        state: str,
        path: Path,
        owner: Optional[str],
        group: Optional[str],
        mode: Optional[str],
        source: Optional[Path],
        checksum: Optional[str]
    ) -> None:
        super().__init__(id, catalog_task_id, state, checksum)
        self.__path = path
        self.__owner = owner
        self.__group = group
        self.__mode = mode
        self.__source = source
        self.__checksum = checksum

    def __eq__(self, other):
        if isinstance(other, ResourceFile):
            return (
                (self.path == other.path) and
                (self.owner == other.owner) and
                (self.group == other.group) and
                (self.mode == other.mode) and
                (self.source == other.source) and
                (self.checksum == other.checksum)
            )
        else:
            return False

    @property
    def path(self) -> Path:
        return self.__path

    @property
    def owner(self) -> Optional[str]:
        return self.__owner

    @property
    def group(self) -> Optional[str]:
        return self.__group

    @property
    def mode(self) -> Optional[str]:
        return self.__mode

    @property
    def source(self) -> Optional[Path]:
        return self.__source

    @property
    def checksum(self) -> Optional[str]:
        return self.__checksum

