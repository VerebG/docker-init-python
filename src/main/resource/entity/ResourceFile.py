from pathlib import Path
from typing import Optional

from src.main.resource.entity.Resource import Resource

class ResourceFile(Resource):
    __path: Path
    __owner: int
    __group: int
    __mode: str
    __source: Path
    __content_checksum: str

    def __init__(self,
        id: str,
        catalog_task_id: str,
        state: str,
        path: Path,
        owner: Optional[int],
        group: Optional[int],
        mode: Optional[str],
        source: Optional[Path],
        content_checksum: Optional[str]
    ) -> None:
        super().__init__(id, catalog_task_id, state)
        self.__path = path
        self.__owner = owner
        self.__group = group
        self.__mode = mode
        self.__source = source
        self.__content_checksum = content_checksum

    @property
    def resource_attr_to_comparison(self):
        return [
            ('content', self.content_checksum),
            ('owner', self.owner),
            ('group', self.group),
            ('mode', self.mode)
        ]

    def __eq__(self, other: Resource):
        return [item for item in self.resource_attr_to_comparison if not item in other.resource_attr_to_comparison]

    @property
    def path(self) -> Path:
        return self.__path

    @property
    def owner(self) -> Optional[int]:
        return self.__owner

    @property
    def group(self) -> Optional[int]:
        return self.__group

    @property
    def mode(self) -> Optional[str]:
        return self.__mode

    @property
    def source(self) -> Optional[Path]:
        return self.__source

    @property
    def content_checksum(self) -> Optional[str]:
        return self.__content_checksum

    @property
    def can_register(self) -> Optional[str]:
        return None

    @property
    def create_from_exist(self) -> str:
        return self.path.__str__()

